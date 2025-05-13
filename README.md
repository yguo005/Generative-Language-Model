# Foundations of AI - Assignment 1


## Assignment Overview

This assignment involved building an N-gram language model and exploring the impact of training data on its performance. The model was tested using medical record data, and its behavior was observed with both relevant and irrelevant prompts.

## Impact of Training Dataset on the Model

The choice of training dataset significantly affects the performance and behavior of a language model.

For this assignment, a model was presumably trained or tested using medical record data.
*   When prompts relevant to medical records (e.g., "patient," "physical") were used, the model generated contextually relevant text.
*   Conversely, when prompts not present in the medical record data (e.g., "for information on our return policy") were used, the generated text appeared to be a concatenation of random characters.

This demonstrates that models trained on specific types of data learn the patterns, vocabulary, and unique characteristics of that dataset. Popular language models often use diverse datasets like Wikipedia or OpenWebText (derived from web pages) to handle a wide range of topics. However, the content and quality of training data can introduce biases, affecting the model's output.

The provided screenshots demonstrate this:
*   With **n=3** and the prompt "patient," the model generated text related to medical scenarios.
*   With **n=5** and the prompt "physical," the model again generated medically relevant text.
*   With **n=20** and the prompt "for information on our return policy" (likely outside the scope of medical training data), the generated text was less coherent, illustrating the model's limitations when faced with out-of-domain prompts.


## Resources Used

*   **Statistical Language Model: N-gram to calculate the Probability of word sequence using Python**
    *   **URL:** `https://medium.com/codex/statistical-language-model-n-gram-to-calculate-the-probability-of-word-sequence-using-python-2e54a1084250`
    *   **Description:** This article was useful for understanding how to calculate the probability of word sequences using N-grams in Python.

## Reflections

*   **Most Difficult Part:**
    *   Determining the appropriate data structure for storing N-grams and their respective probabilities.

*   **Most Rewarding Part:**
    *   Successfully designing a model that could generate content based on an input prompt and character probabilities.
    *   Being able to generate content after entering a prompt.

*   **What was Learned:**
    *   How to build a nested dictionary, likely for storing the N-gram model.


## Screenshots (Illustrative)

The assignment submission includes screenshots demonstrating the model's output:
*   **`n=3` (prompt: "patient"):** Generated text like "patient scan confirmed white blood cell..."
*   **`n=5` (prompt: "physical"):** Generated text like "physical examination revealed tenderness in the lower right quadrant..."
*   **`n=20` (prompt: "for information on our return policy"):** Generated less coherent text, indicating the prompt was likely outside the training data's domain.

These examples showcase the N-gram probabilities for character sequences and the generated text.
