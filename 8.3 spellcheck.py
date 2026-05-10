dictionary = {
    "about",
    "above",
    "across",
    "action",
    "after",
    "again",
    "air",
    "also",
    "answer",
    "around",
    "away",
    "before",
    "begin",
    "being",
    "below",
    "between",
    "birth",
    "black",
    "book",
    "both",
    "break",
    "bring",
    "build",
    "called",
    "case",
    "change",
    "child",
    "city",
    "close",
    "come",
    "could",
    "country",
    "course",
    "different",
    "does",
    "down",
    "during",
    "each",
    "earth",
    "even",
    "every",
    "example",
    "follow",
    "form",
    "found",
    "give",
    "good",
    "great",
    "group",
    "had",
    "hand",
    "have",
    "head",
    "help",
    "here",
    "high",
    "him",
    "his",
    "home",
    "house",
    "how",
    "human",
    "important",
    "into",
    "just",
    "keep",
    "kind",
    "know",
    "large",
    "last",
    "later",
    "learn",
    "left",
    "let",
    "life",
    "light",
    "line",
    "little",
    "live",
    "look",
    "made",
    "make",
    "many",
    "may",
    "mean",
    "might",
    "more",
    "most",
    "move",
    "much",
    "must",
    "name",
    "need",
    "never",
    "new",
    "next",
    "night",
    "number",
    "off",
    "old",
    "once",
    "only",
    "open",
    "order",
    "other",
    "our",
    "out",
    "over",
    "own",
    "part",
    "people",
    "place",
    "plant",
    "point",
    "public",
    "put",
    "read",
    "real",
    "right",
    "run",
    "same",
    "say",
    "set",
    "should",
    "show",
    "side",
    "since",
    "small",
    "some",
    "sound",
    "still",
    "story",
    "study",
    "such",
    "take",
    "tell",
    "than",
    "that",
    "their",
    "them",
    "then",
    "there",
    "these",
    "thing",
    "think",
    "this",
    "those",
    "three",
    "through",
    "time",
    "too",
    "turn",
    "under",
    "use",
    "very",
    "want",
    "water",
    "way",
    "week",
    "well",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "will",
    "with",
    "without",
    "word",
    "work",
    "world",
    "would",
    "write",
    "year",
    "young",
    "your",
}


def edit_distance(s1, s2):
    if len(s1) < len(s2):
        return edit_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)

    prev_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        curr_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = prev_row[j + 1] + 1
            deletions = curr_row[j] + 1
            substitutions = prev_row[j] + (c1 != c2)
            curr_row.append(min(insertions, deletions, substitutions))
        prev_row = curr_row
    return prev_row[-1]


def get_suggestions(word, max_distance=2):
    suggestions = []
    for dict_word in dictionary:
        dist = edit_distance(word.lower(), dict_word)
        if dist <= max_distance:
            suggestions.append((dict_word, dist))
    return sorted(suggestions, key=lambda x: x[1])


def spell_check(sentence):
    words = sentence.split()
    corrected = []
    suggestions = []

    for word in words:
        clean = "".join(c for c in word if c.isalnum())
        if clean.lower() in dictionary:
            corrected.append(word)
        else:
            sug = get_suggestions(clean)
            if sug:
                corrected.append(sug[0][0])
                suggestions.append((word, sug[0][0]))
            else:
                corrected.append(word)

    return " ".join(corrected), suggestions


test_sentences = [
    "Ths is a testt sentence",
    "I wnt to learn programming",
    "Ths book is intersting",
    "Pythn is a great lnguage",
]

print("Spell Checker:")
for sent in test_sentences:
    corrected, suggs = spell_check(sent)
    print(f"\nOriginal: {sent}")
    print(f"Corrected: {corrected}")
    if suggs:
        print("Changes:", suggs)
