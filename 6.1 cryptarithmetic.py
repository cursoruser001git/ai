def solve_cryptarithm():
    def backtrack(index, assignment):
        if index == len(letters):
            return validate(assignment)

        letter = letters[index]
        if letter in assignment:
            return backtrack(index + 1, assignment)

        for digit in range(10):
            if digit not in used:
                if (letter == first_letter or letter == second_letter) and digit == 0:
                    continue
                used.add(digit)
                assignment[letter] = digit
                if backtrack(index + 1, assignment):
                    return True
                del assignment[letter]
                used.remove(digit)
        return False

    def validate(assignment):
        s1 = int("".join(str(assignment[c]) for c in word1))
        s2 = int("".join(str(assignment[c]) for c in word2))
        s3 = int("".join(str(assignment[c]) for c in result))
        return s1 + s2 == s3

    problem = "SEND + MORE = MONEY"
    parts = problem.replace("=", "").replace("+", " ").split()
    word1, word2, result = parts[0], parts[1], parts[2]
    letters = list(set(word1 + word2 + result))
    first_letter = word1[0]
    second_letter = word2[0]
    used = set()
    assignment = {}

    if backtrack(0, assignment):
        print("Solution found:")
        for letter in sorted(assignment.items(), key=lambda x: -x[1]):
            print(f"{letter[0]} = {letter[1]}")
        print(f"{word1}: {int(''.join(str(assignment[c]) for c in word1))}")
        print(f"{word2}: +{int(''.join(str(assignment[c]) for c in word2))}")
        print(f"{result}: {int(''.join(str(assignment[c]) for c in result))}")
    else:
        print("No solution")


solve_cryptarithm()
