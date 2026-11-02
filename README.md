# 🔍 Text Similarity & Duplicate Detection

> An Intelligent NLP-Based System for Comparing Text and Detecting Duplicate Questions.

## 📌 Project Overview

Text Similarity and Duplicate Detection is a Natural Language Processing (NLP) application designed to compare two sentences or questions and identify how similar their meanings are.

The system processes user-provided text, converts it into numerical representations, and calculates similarity scores using NLP and machine learning techniques.

It aims to identify exact duplicates, semantically similar questions, and completely different text inputs.

**Project Number:** 5  
**Group:** 1  
**Domain:** Natural Language Processing (NLP)  
**Project Type:** Capstone Project  
**Project Status:** 🚧 Under Development

---

## 📌 1. Problem Statement

With the increasing amount of digital information, duplicate and semantically similar questions frequently appear across educational platforms, discussion forums, websites, and databases.

Manually identifying duplicate questions is time-consuming and inefficient.

Traditional keyword matching methods often fail to recognize sentences that have different words but convey the same meaning.

This project aims to develop an intelligent text similarity system that compares two text inputs, calculates their similarity, and identifies duplicate or semantically similar content using Natural Language Processing techniques.

## 🎯 2. Project Objectives

- Develop an NLP-based text similarity application.
- Collect and process sentence/question datasets.
- Perform text cleaning and preprocessing.
- Convert text into numerical representations.
- Implement TF-IDF vectorization.
- Calculate similarity using Cosine Similarity.
- Detect duplicate and semantically similar questions.
- Display similarity scores through an interactive interface.
- Evaluate the system using unseen text examples.

## ✨ 3. Planned Features

| Feature | Description |
|---|---|
| Dual Text Input | Enter two sentences or questions |
| Text Preprocessing | Clean and normalize text |
| TF-IDF Vectorization | Convert text into numerical vectors |
| Similarity Calculation | Calculate cosine similarity |
| Duplicate Detection | Identify duplicate questions |
| Similarity Classification | Classify text as Duplicate, Similar or Different |
| Similarity Score | Display a percentage-based score |
| Interactive Dashboard | User-friendly Streamlit interface |
| Evaluation | Test performance on unseen examples |

## 🧠 4. NLP Concepts Used

- Text Preprocessing
- Tokenization
- Lowercase Normalization
- Stopword Removal
- Stemming and Lemmatization
- Feature Extraction
- TF-IDF Vectorization
- Cosine Similarity
- Semantic Similarity
- Duplicate Detection
- Model Evaluation

## ⚙️ 5. System Architecture

### Text Comparison Pipeline

1. User Input: Accept two sentences or questions.
2. Text Cleaning: Remove unnecessary characters and normalize text.
3. Tokenization: Break sentences into individual tokens.
4. Feature Extraction: Convert text into numerical vectors using TF-IDF.
5. Similarity Calculation: Calculate cosine similarity between vectors.
6. Classification: Determine whether the text is duplicate, similar, or different.
7. Result Display: Show similarity score and classification.

### Architecture Overview

```text
       USER INPUT
      (Two Sentences)
             |
             v
      TEXT PREPROCESSING
             |
             v
       TOKENIZATION
             |
             v
      TF-IDF VECTORIZATION
             |
             v
     COSINE SIMILARITY
             |
             v
     DUPLICATE DETECTION
             |
             v
     RESULT CLASSIFICATION
             |
       +-----+-----+
       |     |     |
       v     v     v
    DUPLICATE SIMILAR DIFFERENT
             |
             v
      STREAMLIT DASHBOARD
```

## 🛠️ 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NLTK | Text preprocessing |
| Scikit-learn | TF-IDF and similarity algorithms |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Streamlit | User interface |
| Matplotlib | Data visualization |
| Pytest | Software testing |
| Git & GitHub | Version control |

## 📁 7. Project Structure

```text
text-similarity-duplicate-detection/
│
├── app/
│   ├── core/
│   ├── ui/
│   └── config.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── evaluation/
│
├── docs/
├── notebooks/
├── scripts/
├── tests/
├── screenshots/
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 8. Installation and Setup

### Prerequisites

- Python 3.10 or later
- Git
- pip
- VS Code or PyCharm

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR-USERNAME/text-similarity-duplicate-detection.git
```

### Step 2: Navigate to Project

```bash
cd text-similarity-duplicate-detection
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run Application

```bash
streamlit run app/ui/streamlit_app.py
```

*Application execution instructions will be finalized when the implementation is ready.*

## 🧪 9. Testing and Evaluation

The system will be evaluated using different sentence pairs and question datasets.

Planned evaluation areas:

- Text preprocessing correctness
- Similarity score calculation
- Duplicate detection accuracy
- Classification performance
- Precision
- Recall
- F1-score
- Confusion Matrix
- Performance on unseen examples

## 🗺️ 10. Development Roadmap

- [ ] Repository setup and project planning
- [ ] Dataset collection
- [ ] Text preprocessing implementation
- [ ] TF-IDF vectorization
- [ ] Cosine similarity implementation
- [ ] Duplicate detection logic
- [ ] Similarity classification
- [ ] Streamlit interface development
- [ ] Testing and evaluation
- [ ] Performance improvement
- [ ] Documentation
- [ ] Final project deployment

## 🔮 11. Future Enhancements

- Sentence Transformers integration.
- Advanced semantic similarity detection.
- Multilingual text comparison.
- Document-level duplicate detection.
- Batch question comparison.
- Duplicate detection dashboard.
- API integration for external applications.

## 👥 12. Contributors

**Project:** Text Similarity and Duplicate Detection  
**Project Number:** 5  
**Group:** 1

| Contributor | Role |
|---|---|
| Member 1 | To be updated |
| Member 2 | To be updated |
| Member 3 | To be updated |

## 📄 13. License

This project is intended to be distributed under the MIT License. See the `LICENSE` file for details.

---

<p align="center">

**Text Similarity & Duplicate Detection**

*Making Text Comparison Smarter with NLP.*

Built with Python, Natural Language Processing and Machine Learning.

</p>
