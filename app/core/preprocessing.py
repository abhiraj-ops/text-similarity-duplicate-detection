import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from app.config import NLTK_DOWNLOADS


def _ensure_nltk_resources():
    """Download required NLTK data quietly if missing."""
    for resource in NLTK_DOWNLOADS:
        try:
            if resource in ("punkt_tab", "punkt"):
                nltk.data.find(f"tokenizers/{resource}")
            else:
                nltk.data.find(f"corpora/{resource}")
        except LookupError:
            nltk.download(resource, quiet=True)


_ensure_nltk_resources()

_stop_words = set(stopwords.words("english"))
_lemmatizer = WordNetLemmatizer()


def clean_text(text: str) -> str:
    """Lowercase and remove non-alphabetic characters and extra spaces."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str):
    """Split text into word tokens."""
    return word_tokenize(text)


def remove_stopwords(tokens):
    """Remove English stopwords from a token list."""
    return [t for t in tokens if t not in _stop_words]


def lemmatize(tokens):
    """Lemmatize a list of tokens to their root form."""
    return [_lemmatizer.lemmatize(t) for t in tokens]


def preprocess(text: str) -> str:
    """Full preprocessing pipeline: clean -> tokenize -> stopword removal -> lemmatize."""
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize(tokens)
    return " ".join(tokens)
