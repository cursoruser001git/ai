def magic_square():
    print("--- Magic Square Generator (Siamese Method) ---")
    
    try:
        n = int(input("Enter an ODD number for the size of the square (e.g., 3, 5, 7): "))
    except ValueError:
        print("Invalid input.")
        return

    if n % 2 == 0:
        print("Error: The Siamese method only works for ODD numbers.")
        return

    magic_matrix = [[0 for _ in range(n)] for _ in range(n)]


    i = 0
    j = n // 2

    num = 1
    while num <= n * n:
        magic_matrix[i][j] = num
        num += 1

        new_i, new_j = (i - 1), (j + 1)

        if new_i < 0:
            new_i = n - 1
        if new_j == n:
            new_j = 0

        if magic_matrix[new_i][new_j] != 0:
            i += 1
        else:
            i, j = new_i, new_j

    magic_constant = (n * (n**2 + 1)) // 2
    print(f"\nMagic Constant for size {n}x{n} is: {magic_constant}\n")

    print("Generated Magic Square:")
    for row in magic_matrix:
        print("  ".join(f"{x:2d}" for x in row))
    
    print("\n--- Verification ---")
    print(f"Sum of Row 0: {sum(magic_matrix[0])}")
    col_sum = sum(row[0] for row in magic_matrix)
    print(f"Sum of Col 0: {col_sum}")

if __name__ == "__main__":
    magic_square()