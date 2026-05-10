def print_solution(board, n):
    print(f"\nSolution for {n}-Queens:")
    for row in board:
        line = ["Q" if x == 1 else "." for x in row]
        print(" ".join(line))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    if row >= n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve_n_queens_util(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

def n_queens():
    print("--- N-Queens Solver (Backtracking) ---")
    try:
        n = int(input("Enter the value of N (e.g., 4, 8): "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens_util(board, 0, n):
        print("Solution does not exist")
    else:
        print_solution(board, n)

if __name__ == "__main__":
    n_queens()