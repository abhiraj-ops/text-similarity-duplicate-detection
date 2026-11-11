# 🔍 Text Similarity & Duplicate Detection

> A complete, runnable NLP application that compares two sentences/questions and detects whether they are **Duplicate**, **Similar**, or **Different**.

Built with **Python**, **NLTK**, **scikit-learn (TF-IDF + Cosine Similarity)**, **pandas**, and **Streamlit**.

---

## 📁 Project Structure

```text
text-similarity-duplicate-detection/
│
├── app/
│   ├── __init__.py
│   ├── config.py             # thresholds, paths, NLTK settings
│   ├── core/
│   │   ├── __init__.py
│   │   ├── preprocessing.py  # text cleaning, tokenization, stopword removal, lemmatization
│   │   └── similarity.py     # TF-IDF vectorization, cosine similarity, classification
│   └── ui/
│       ├── __init__.py
│       └── streamlit_app.py  # Streamlit dashboard
│
├── data/
│   └── sample_questions.csv  # sample question dataset for batch comparison
│
├── tests/
│   ├── __init__.py
│   └── test_similarity.py    # pytest unit tests
│
├── notebooks/.gitkeep
├── scripts/.gitkeep
├── screenshots/.gitkeep
│
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Installation & Setup (VS Code)

### Prerequisites
- Python 3.10 or later
- Git
- VS Code (recommended)

### Step 1: Open the folder in VS Code
```bash
cd C:\Users\ABHISHEK\Documents\NewProject
code .
```

### Step 2: Create a virtual environment
```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### Step 4: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Run the application
```bash
streamlit run app/ui/streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 🧪 Running Tests

```bash
pytest
```

Tests cover:
- Identical text → score 1.0
- Different text → low score
- Empty text → score 0.0
- Classification thresholds (Duplicate / Similar / Different)

---

## 🎯 How It Works

| Step | Description |
|------|-------------|
| 1 | User enters two sentences/questions |
| 2 | Text is cleaned (lowercase, remove special characters) |
| 3 | Text is tokenized into words |
| 4 | Stopwords are removed |
| 5 | Words are lemmatized to root form |
| 6 | TF-IDF converts text into numerical vectors |
| 7 | Cosine similarity is calculated (0 to 1) |
| 8 | Result is classified as Duplicate / Similar / Different |

**Classification thresholds:**
- **Duplicate:** score ≥ 0.80 (🔴)
- **Similar:** score ≥ 0.50 (🟡)
- **Different:** score < 0.50 (🟢)

---

## 👥 Team Workflow (3 Members)

This project is set up so multiple members can commit code:

1. **Member 1** — works on `app/core/preprocessing.py`
2. **Member 2** — works on `app/core/similarity.py`
3. **Member 3** — works on `app/ui/streamlit_app.py`

Each member:
1. Creates their own branch: `git checkout -b feature/member-name`
2. Makes changes and commits: `git add . && git commit -m "..."`
3. Pushes to GitHub: `git push origin feature/member-name`
4. Opens a Pull Request to merge into `main`

**Do not push to GitHub yet** — finish local development first, then push when ready.

---

## 📄 License

MIT License. See `LICENSE` for details.

---

<p align="center">
  <b>Text Similarity & Duplicate Detection</b><br>
  Built with Python, NLTK, scikit-learn & Streamlit
</p>
