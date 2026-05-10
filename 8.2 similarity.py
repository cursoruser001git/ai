def tokenize(text):
    return set(text.lower().split())


def jaccard_similarity(s1, s2):
    tokens1 = tokenize(s1)
    tokens2 = tokenize(s2)
    intersection = len(tokens1 & tokens2)
    union = len(tokens1 | tokens2)
    return intersection / union if union > 0 else 0


def cosine_similarity(s1, s2):
    tokens1 = tokenize(s1)
    tokens2 = tokenize(s2)
    all_tokens = tokens1 | tokens2

    vec1 = [1 if t in tokens1 else 0 for t in all_tokens]
    vec2 = [1 if t in tokens2 else 0 for t in all_tokens]

    dot = sum(a * b for a, b in zip(vec1, vec2))
    mag1 = sum(a * a for a in vec1) ** 0.5
    mag2 = sum(b * b for b in vec2) ** 0.5

    return dot / (mag1 * mag2) if mag1 * mag2 > 0 else 0


def word_overlap(s1, s2):
    tokens1 = tokenize(s1)
    tokens2 = tokenize(s2)
    common = tokens1 & tokens2
    return (
        len(common) / min(len(tokens1), len(tokens2))
        if min(len(tokens1), len(tokens2)) > 0
        else 0
    )


pairs = [
    ("the cat is sleeping", "the cat sleeps"),
    ("python is a programming language", "java is a programming language"),
    ("machine learning is ai", "deep learning is ai"),
    ("the quick brown fox", "the slow red fox"),
]

print("Similarity Scores:")
for s1, s2 in pairs:
    print(f"\nText 1: {s1}")
    print(f"Text 2: {s2}")
    print(f"  Jaccard: {jaccard_similarity(s1, s2):.4f}")
    print(f"  Cosine:  {cosine_similarity(s1, s2):.4f}")
    print(f"  Word Overlap: {word_overlap(s1, s2):.4f}")
