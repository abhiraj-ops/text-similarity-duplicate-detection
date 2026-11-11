import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
SAMPLE_DATA_PATH = DATA_DIR / "sample_questions.csv"

# Similarity classification thresholds
SIMILARITY_THRESHOLD_DUPLICATE = 0.80
SIMILARITY_THRESHOLD_SIMILAR = 0.50

# NLTK resources to download
NLTK_DOWNLOADS = ["stopwords", "punkt_tab", "wordnet", "omw-1.4"]

# App metadata
APP_TITLE = "Text Similarity & Duplicate Detection"
APP_ICON = "🔍"
