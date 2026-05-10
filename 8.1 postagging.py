def pos_tagging(sentence):
    pos_rules = {
        "the": "DT",
        "a": "DT",
        "an": "DT",
        "cat": "NN",
        "dog": "NN",
        "bird": "NN",
        "fish": "NN",
        "runs": "VB",
        "eats": "VB",
        "flies": "VB",
        "swims": "VB",
        "quickly": "RB",
        "slowly": "RB",
        "happily": "RB",
        "big": "JJ",
        "small": "JJ",
        "blue": "JJ",
    }
    words = sentence.split()
    tagged = []
    for word in words:
        pos = pos_rules.get(word.lower(), "NN")
        tagged.append((word, pos))
    return tagged


def advanced_pos_tag(sentence):
    words = sentence.split()
    tagged = []
    for word in words:
        lower = word.lower()
        if lower in ["the", "a", "an"]:
            pos = "DT"
        elif lower in ["i", "you", "he", "she", "it", "we", "they"]:
            pos = "PRP"
        elif lower.endswith("ing"):
            pos = "VBG"
        elif lower.endswith("ed"):
            pos = "VBD"
        elif lower.endswith("ly"):
            pos = "RB"
        elif lower.endswith("s") and len(lower) > 2:
            pos = "NNS"
        elif lower in ["is", "are", "was", "were", "be", "been", "being"]:
            pos = "VB"
        else:
            pos = "NN"
        tagged.append((word, pos))
    return tagged


sentences = [
    "The cat runs quickly",
    "The dog eats food",
    "A big bird flies slowly",
    "The fish swims happily",
]

print("POS Tagging Results:")
for sent in sentences:
    print(f"\nSentence: {sent}")
    print("Simple:", pos_tagging(sent))
    print("Advanced:", advanced_pos_tag(sent))
