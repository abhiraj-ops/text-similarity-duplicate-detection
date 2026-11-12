# Methodology

This document outlines the NLP methodology used in the project.

## Approach

The project follows a traditional NLP approach:
1. Text is cleaned and normalized
2. Tokens are extracted using NLTK's word_tokenize
3. Stopwords are removed
4. Words are lemmatized to their root form
5. TF-IDF converts text to numerical vectors
6. Cosine similarity measures similarity between vectors

## Classification Thresholds

- **Duplicate:** Similarity score ≥ 0.80
- **Similar:** Similarity score ≥ 0.50
- **Different:** Similarity score < 0.50
