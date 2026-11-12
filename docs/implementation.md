# Implementation

This document describes the implementation details of the Text Similarity & Duplicate Detection project.

## Text Preprocessing Pipeline

The preprocessing module handles:
- Text cleaning (lowercase, special character removal)
- Tokenization using NLTK
- Stopword removal
- Lemmatization using WordNetLemmatizer

## Similarity Calculation

The similarity module implements:
- TF-IDF vectorization using scikit-learn
- Cosine similarity computation
- Classification into Duplicate / Similar / Different based on thresholds

## Streamlit UI

The UI module provides:
- Dual text input interface
- Real-time similarity scoring
- Batch comparison against sample dataset
- Comparison history tracking
