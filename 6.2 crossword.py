def solve_crossword():
    slots = ["_C___", "C___", "_O___"]
    words = ["CAT", "DOG", "COW", "COD", "COG", "COY"]

    def backtrack(slot_idx, assignment):
        if slot_idx == len(slots):
            return all(len(s) == len(w) for s, w in zip(slots, assignment))

        slot = slots[slot_idx]
        for word in words:
            if len(word) != len(slot):
                continue
            valid = True
            for i, char in enumerate(slot):
                if char != "_" and char != word[i]:
                    valid = False
                    break
            if valid:
                assignment.append(word)
                if backtrack(slot_idx + 1, assignment):
                    print(f"Solution: {assignment}")
                    return True
                assignment.pop()
        return False

    print("Crossword puzzle: fill in words")
    print("Slots:", slots)
    print("Words:", words)
    print()
    backtrack(0, [])


def solve_crossword_simple():
    horizontal = ["_R_", "__T", "S__"]
    vertical = ["_S_", "R__", "_T_"]
    words = ["CAT", "CAR", "SAT", "ART", "SET", "ARTIST"]

    def fits(word, pattern):
        return len(word) == len(pattern) and all(
            p == "_" or p == w for p, w in zip(pattern, word)
        )

    solutions = []
    for h1 in words:
        if fits(h1, horizontal[0]):
            for h2 in words:
                if fits(h2, horizontal[1]):
                    for h3 in words:
                        if fits(h3, horizontal[2]):
                            cross = True
                            for i in range(len(h1)):
                                v = vertical[i] if len(vertical) > i else ""
                                if v and len(v) >= len(h3) and not fits(h3[i], v):
                                    cross = False
                                    break
                            if cross:
                                solutions.append((h1, h2, h3))

    print("Horizontal:", horizontal)
    print("Vertical:", vertical)
    print()
    print("Solutions:")
    for sol in solutions:
        print(f"  {sol[0]}")
        print(f"  {sol[1]}")
        print(f"  {sol[2]}")
        print()


solve_crossword_simple()
