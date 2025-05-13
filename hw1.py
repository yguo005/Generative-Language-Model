import random

class CharNGramLanguageModel:
    END = None

    def __init__(self, n, training_text):
        self.n = n 
        # ngram_cnt: outer dictionary: key is a string of n characters from the training text, value is another dictionary
        self.ngram_cnt = {}
        self.context_cnt = {}
        self.single_char_freq = {}
        self.train_model(training_text) 

    def train_model(self, text):
        text += '\0'  # Append a null character to signal the end of the text
        # range: ensure there are enough n characters left to form a context (e.g.last 3 characters)
        for i in range(len(text) - self.n):
            # slice notation extracts a substring from index i to i+self.n (not inclusive)
            context = text[i:i+self.n]
            if i+self.n < len(text):
                next_char = text[i+self.n]  
            else: self.END

            if context not in self.ngram_cnt:
                #[context]: key in the ngram_cnt dictionary
                self.ngram_cnt[context] = {}
            #[next_char]: is the key in the inner dictionary, value is the count of the next character after the context
            #.get(next_char, 0): if next_char is not in the dictionary, return 0
            self.ngram_cnt[context][next_char] = self.ngram_cnt[context].get(next_char, 0) + 1
            self.context_cnt[context] = self.context_cnt.get(context, 0) + 1

            # Update single character frequency
            self.single_char_freq[next_char] = self.single_char_freq.get(next_char, 0) + 1

        # Convert counts to probabilities for n-grams
        for context, next_chars in self.ngram_cnt.items():
            total = self.context_cnt[context]
            #char: count / total: creates a key-value pair in the new dictionary. char: The key, a character that follows the context. count / total: The value, probability of char following the context
            #char is a key in the dictionary that is the value associated with the context key in self.ngram_cnt
            #.items():returns a view object that displays a list of a dictionary's key-value tuple pairs
            #next_chars: a dictionary where keys are characters that follow the context and values are their counts
            self.ngram_cnt[context] = {char: count / total for char, count in next_chars.items()}

        # Convert single character counts to probabilities
        total_chars = sum(self.single_char_freq.values())
        self.single_char_freq = {char: count / total_chars for char, count in self.single_char_freq.items()}

    def generate_character(self, prompt):
        if len(prompt) < self.n:
            return ''  
        #extract a substring of length self.n taken from the end of prompt
        # why from the end? the recent context is more relevant for predicting the next character in the sequence
        current_context = prompt[-self.n:]  

        if current_context not in self.ngram_cnt:
            # Handle sequences not found in the training dataset

            #This line unpacks the result of the zip function into two variables: chars and weights. chars: a tuple containing all the keys (characters) from self.single_char_freq.weights:a tuple containing all the values (frequencies) from self.single_char_freq.
            # *self.single_char_freq.items():The * operator is used to unpack the items in the dictionary into separate arguments.This means that each key-value pair in self.single_char_freq.items() is passed as a separate argument to the zip function.
            # zip function example: zip(('a', 0.5), ('b', 0.3), ('c', 0.2)) results in (('a', 'b', 'c'), (0.5, 0.3, 0.2))
            chars, weights = zip(*self.single_char_freq.items())
            #[0]: random.choices function returns a list, select the first element of this list
            return random.choices(chars, weights)[0]

        next_chars = self.ngram_cnt[current_context]
        chars, weights = zip(*next_chars.items())
        return random.choices(chars, weights)[0]

    def generate(self, prompt):
        if len(prompt) < self.n:
            print(f"Prompt must be at least {self.n} characters long.")
            return ""
        result = prompt
        while True:
            next_char = self.generate_character(result)
            if next_char == '\0':
                break
            result += next_char
        # Ensure the null character is not included
        if result.endswith('\0'):
            result = result[:-1]
        return result

def main():
    dataset_file = "stranger"
    with open(dataset_file, "r") as file:
        dataset = file.read()

    for n in [3, 5, 20]:
        print(f"\nTesting with n = {n}")
        model = CharNGramLanguageModel(n, dataset)

        user_prompt = input(f"Enter a prompt (at least {n} characters): ")  
        generated_text = model.generate(user_prompt)
        print("Generated text:", generated_text)
        
        # Print the n-gram probabilities for verification
        print("N-gram probabilities:")
        for context, next_chars in model.ngram_cnt.items():
            print(f"{context}: {next_chars}")

if __name__ == "__main__":
    main()