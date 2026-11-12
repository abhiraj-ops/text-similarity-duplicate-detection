# System Architecture

## Text Comparison Pipeline

```
USER INPUT → TEXT PREPROCESSING → TOKENIZATION → TF-IDF VECTORIZATION → COSINE SIMILARITY → DUPLICATE DETECTION → RESULT CLASSIFICATION → STREAMLIT DASHBOARD
```

## Components

1. **Preprocessing Module:** Cleans and normalizes text
2. **Similarity Module:** Computes TF-IDF vectors and cosine similarity
3. **UI Module:** Streamlit interface for user interaction
