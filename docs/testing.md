# Testing

## Planned Evaluation Areas

- Text preprocessing correctness
- Similarity score calculation
- Duplicate detection accuracy
- Classification performance (Precision, Recall, F1-score)
- Performance on unseen examples

## Test Cases

| Test | Expected Result |
|------|-----------------|
| Identical text | Score = 1.0 |
| Different text | Score < 0.5 |
| Empty text | Score = 0.0 |
| Similar text | Score ≥ 0.5 |
| Duplicate text | Score ≥ 0.8 |
