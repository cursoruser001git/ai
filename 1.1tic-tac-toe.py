def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def check_draw(board):
    return ' ' not in board

def tic_tac_toe():
    board = [' ' for _ in range(9)]
    current_player = 'X'
    game_running = True

    print("--- Tic Tac Toe (Non-AI) ---")
    print("Positions are numbered 1-9 (Top-left to Bottom-right).")

    while game_running:
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if move < 0 or move > 8 or board[move] != ' ':
            print("Invalid move. Spot already taken or out of range.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_running = False
        elif check_draw(board):
            print_board(board)
            print("It's a Draw!")
            game_running = False
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()