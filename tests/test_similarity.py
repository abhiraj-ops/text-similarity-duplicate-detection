import pytest

from app.core.similarity import compare_with_label, classify, compute_similarity


def test_compute_similarity_identical():
    score = compute_similarity("hello world", "hello world")
    assert score == pytest.approx(1.0)


def test_compute_similarity_different():
    score = compute_similarity("hello world", "goodbye universe")
    assert 0.0 <= score < 0.5


def test_compute_similarity_empty():
    assert compute_similarity("", "hello") == 0.0
    assert compute_similarity("hello", "") == 0.0
    assert compute_similarity("", "") == 0.0


def test_classify_thresholds():
    assert classify(0.9) == "Duplicate"
    assert classify(0.8) == "Duplicate"
    assert classify(0.6) == "Similar"
    assert classify(0.5) == "Similar"
    assert classify(0.3) == "Different"
    assert classify(0.0) == "Different"


def test_compare_with_label_returns_tuple():
    score, label = compare_with_label("capital of France", "capital city of France")
    assert isinstance(score, float)
    assert label in ("Duplicate", "Similar", "Different")
