def edit_distance(s1, s2):
    if len(s1) < len(s2):
        return edit_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    prev_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def spell_check(word, dictionary):
    word_lower = word.lower()

    for dict_word in dictionary:
        if word_lower == dict_word:
            return dict_word, 0

    best_match = None
    best_dist = 999

    for dict_word in dictionary:
        if abs(len(word_lower) - len(dict_word)) > 2:
            continue
        dist = edit_distance(word_lower, dict_word)
        if dist < best_dist:
            best_dist = dist
            best_match = dict_word

    return best_match, best_dist


dictionary = [
    "this",
    "is",
    "a",
    "test",
    "sentence",
    "the",
    "book",
    "interesting",
    "python",
    "great",
    "language",
    "programming",
    "learn",
    "want",
    "too",
    "cat",
    "dog",
    "fish",
    "bird",
    "happy",
    "sad",
    "run",
    "walk",
    "eat",
]

test_sentences = ["Ths is a testt sentence", "Ths book is intersting"]

print("Spell Checker")
print("Dictionary:", dictionary)
print()

for sentence in test_sentences:
    print(f"Original:  {sentence}")
    words = sentence.split()
    corrected = []
    changes = []

    for word in words:
        result, dist = spell_check(word, dictionary)
        corrected.append(result)
        if dist > 0:
            changes.append(f"{word} -> {result}")

    print(f"Corrected: {' '.join(corrected)}")
    print(f"Changes:   {changes}")
    print()
