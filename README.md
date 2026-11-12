# 🔍 Text Similarity & Duplicate Detection

> **Your University's Knowledge, One Conversation Away.**

Text Similarity & Duplicate Detection is a Natural Language Processing (NLP) application designed to compare two sentences or questions and identify how similar their meanings are.

The system processes user-provided text, converts it into numerical representations, and calculates similarity scores using NLP and machine learning techniques.

It aims to identify exact duplicates, semantically similar questions, and completely different text inputs.

---

## 📌 1. Problem Statement

University students frequently struggle to find accurate academic information because it is distributed across multiple documents, PDF files, notices, and university portals.

Finding a specific piece of information often requires students to manually open several documents, search through multiple pages, and identify the relevant information themselves.

Traditional keyword-based searching may also fail when students phrase their questions differently from the wording used in official documents.

This project aims to address this problem by building an intelligent text similarity system that understands natural language queries and identifies duplicate or semantically similar content using Natural Language Processing techniques.

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

| Feature                       | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| Dual Text Input               | Enter two sentences or questions                             |
| Text Preprocessing            | Clean and normalize extracted text                           |
| TF-IDF Vectorization          | Convert text into numerical vectors                          |
| Similarity Calculation        | Calculate cosine similarity                                  |
| Duplicate Detection           | Identify duplicate questions                                 |
| Similarity Classification     | Classify text as Duplicate, Similar or Different             |
| Similarity Score              | Display a percentage-based score                             |
| Interactive Chat Interface    | Allow users to communicate naturally with the assistant      |
| Source Citations              | Display document names and page references                   |
| Hallucination Control         | Handle questions when supporting information is unavailable  |

*These features are planned and will be implemented incrementally.*

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

1. **User Input:** Accept two sentences or questions.
2. **Text Cleaning:** Remove unnecessary characters and normalize text.
3. **Tokenization:** Break sentences into individual tokens.
4. **Feature Extraction:** Convert text into numerical vectors using TF-IDF.
5. **Similarity Calculation:** Calculate cosine similarity between vectors.
6. **Classification:** Determine whether the text is duplicate, similar, or different.
7. **Result Display:** Show similarity score and classification.

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

| Technology            | Purpose                                           |
| --------------------- | ------------------------------------------------- |
| Python                | Core programming language                         |
| NLTK                  | Natural Language Processing                       |
| Scikit-learn          | TF-IDF and similarity algorithms                  |
| Pandas                | Dataset handling                                  |
| NumPy                 | Numerical operations                              |
| Streamlit             | Interactive user interface                        |
| Matplotlib            | Data visualization                                |
| Pytest                | Software testing                                  |
| Git & GitHub          | Version control and collaboration                 |

## 📁 7. Project Structure

```text
text-similarity-duplicate-detection/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── preprocessing.py
│   │   └── similarity.py
│   └── ui/
│       ├── __init__.py
│       └── streamlit_app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample_docs/
│
├── docs/
│   ├── implementation.md
│   ├── methodology.md
│   ├── problem_statement.md
│   ├── requirements.md
│   ├── system_architecture.md
│   ├── testing.md
│   └── user_manual.md
│
├── scripts/
├── tests/
│   ├── __init__.py
│   └── test_similarity.py
│
├── notebooks/
│   └── .gitkeep
├── screenshots/
│   └── .gitkeep
│
├── anirudh_core.ipynb
├── aaditya_core.ipynb
├── anshuman_core.ipynb
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 🚀 8. Installation and Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- Git
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/abhiraj-ops/text-similarity-duplicate-detection.git
```

### Step 2: Navigate to the Project

```bash
cd text-similarity-duplicate-detection
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**

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

## 🧪 9. Testing and Evaluation

The project will be evaluated using a collection of test questions and academic documents.

Planned evaluation areas include:

- Document extraction correctness
- Text preprocessing correctness
- Retrieval relevance
- Recall@K
- Mean Reciprocal Rank (MRR)
- Answer correctness
- Source citation correctness
- Unsupported question handling
- Response latency

The evaluation process will help identify weaknesses in retrieval quality and answer generation.

## 🗺️ 10. Development Roadmap

- [X] Project planning and requirements analysis
- [X] NLP fundamentals and methodology
- [X] Text preprocessing implementation
- [X] TF-IDF vectorization
- [X] Cosine similarity implementation
- [X] Duplicate detection logic
- [X] Similarity classification
- [X] Streamlit frontend development
- [X] Testing and evaluation
- [X] Final documentation and deployment

## 🔮 11. Future Enhancements

Potential future improvements include:

- Sentence Transformers integration.
- Advanced semantic similarity detection.
- Multilingual text comparison.
- Document-level duplicate detection.
- Batch question comparison.
- Duplicate detection dashboard.
- API integration for external applications.

## 👥 12. Contributors

**Project:** Text Similarity & Duplicate Detection

| Contributor | Role |
|-------------|------|
| Anirudh Core | Frontend |
| Aaditya Core | Backend |
| Anshuman Core | NLP Core & Testing |

## 📄 13. License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
<p align="center">
  <b>Text Similarity & Duplicate Detection</b>
  <br/>
  Built with Python, Natural Language Processing and Machine Learning.
</p>
