from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.core.preprocessing import preprocess
from app.config import (
    SIMILARITY_THRESHOLD_DUPLICATE,
    SIMILARITY_THRESHOLD_SIMILAR,
)

_vectorizer = TfidfVectorizer()


def classify(score: float) -> str:
    """Classify a similarity score into Duplicate / Similar / Different."""
    if score >= SIMILARITY_THRESHOLD_DUPLICATE:
        return "Duplicate"
    if score >= SIMILARITY_THRESHOLD_SIMILAR:
        return "Similar"
    return "Different"


def compute_similarity(text1: str, text2: str) -> float:
    """Compute cosine similarity (0 to 1) between two text strings."""
    if not text1 or not text2:
        return 0.0

    p1 = preprocess(text1)
    p2 = preprocess(text2)

    if not p1 or not p2:
        return 0.0

    tfidf_matrix = _vectorizer.fit_transform([p1, p2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return float(similarity)


def compare_with_label(text1: str, text2: str):
    """Return (score, label) for a pair of texts."""
    score = compute_similarity(text1, text2)
    return score, classify(score)


def batch_compare(reference: str, candidates: list):
    """Compare a reference text against many candidates. Returns sorted results."""
    results = []
    for candidate in candidates:
        score, label = compare_with_label(reference, candidate)
        results.append(
            {
                "candidate": candidate,
                "score": round(score, 4),
                "label": label,
            }
        )
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
