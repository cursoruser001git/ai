def print_board(board):
    for row in board:
        print(" | ".join(row))
    print()


def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def is_full(board):
    return all(cell != " " for row in board for cell in row)


def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves


def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "O"
            best = max(best, minimax(board, depth + 1, False))
            board[move[0]][move[1]] = " "
        return best
    else:
        best = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X"
            best = min(best, minimax(board, depth + 1, True))
            board[move[0]][move[1]] = " "
        return best


def best_move(board):
    best_val = -float("inf")
    move = None
    for m in get_available_moves(board):
        board[m[0]][m[1]] = "O"
        val = minimax(board, 0, False)
        board[m[0]][m[1]] = " "
        if val > best_val:
            best_val = val
            move = m
    return move


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe - You are X, AI is O")
    print_board(board)

    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Invalid move")
            continue

        if check_winner(board):
            print_board(board)
            print("You win!")
            break
        if is_full(board):
            print_board(board)
            print("Draw!")
            break

        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = "O"

        print_board(board)
        if check_winner(board):
            print("AI wins!")
            break
        if is_full(board):
            print("Draw!")
            break


play_game()
