import copy

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def print_puzzle(state):
    print("+---+---+---+")
    for row in state:
        print("|", end="")
        for val in row:
            if val == 0:
                print("   |", end="")
            else:
                print(f" {val} |", end="")
        print("\n+---+---+---+")


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_row = (val - 1) // 3
                goal_col = (val - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance


def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count


def get_neighbors(state):
    neighbors = []
    bi, bj = find_blank(state)
    directions = [(-1, 0, "UP"), (1, 0, "DOWN"), (0, -1, "LEFT"), (0, 1, "RIGHT")]

    for di, dj, move in directions:
        ni, nj = bi + di, bj + dj
        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = copy.deepcopy(state)
            new_state[bi][bj], new_state[ni][nj] = new_state[ni][nj], new_state[bi][bj]
            neighbors.append((new_state, move))

    return neighbors


def hill_climbing(initial_state):
    current = copy.deepcopy(initial_state)
    current_h = manhattan_distance(current)
    visited = {state_to_tuple(current)}
    step = 0

    print("=" * 44)
    print("  8-PUZZLE - HILL CLIMBING SOLUTION")
    print("=" * 44)

    print(f"\nGoal State:")
    print_puzzle(goal_state)

    print(f"\nInitial State  [h = {current_h}]:")
    print_puzzle(current)

    while current_h != 0:
        neighbors = get_neighbors(current)

        best_state = None
        best_h = current_h
        best_move = None

        for neighbor, move in neighbors:
            key = state_to_tuple(neighbor)
            if key not in visited:
                h = manhattan_distance(neighbor)
                if h < best_h:
                    best_h = h
                    best_state = neighbor
                    best_move = move

        if best_state is None:
            print("\n*** Stuck at a local minimum! ***")
            print(f"    Steps taken      : {step}")
            print(f"    Heuristic value  : {current_h}")
            print("    Hill Climbing cannot guarantee a")
            print("    solution due to local minima.\n")
            return None

        current = best_state
        current_h = best_h
        visited.add(state_to_tuple(current))
        step += 1

        print(f"Step {step}:  Move blank {best_move}  [h = {current_h}]")
        print_puzzle(current)

    print("=" * 44)
    print(f"  GOAL REACHED in {step} step(s)!")
    print("=" * 44)
    return step


if __name__ == "__main__":
    initial1 = [[1, 2, 3], [4, 5, 0], [7, 8, 6]]

    initial2 = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]

    initial3 = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

    print("Choose an initial state:")
    print("1)  Easy    ->", initial1)
    print("2)  Medium  ->", initial2)
    print("3)  Hard    ->", initial3)
    print("4)  Custom input")

    choice = input("\nEnter choice (1/2/3/4): ").strip()

    if choice == "1":
        state = initial1
    elif choice == "2":
        state = initial2
    elif choice == "3":
        state = initial3
    elif choice == "4":
        print("Enter 9 values row-wise (0 for blank):")
        state = []
        for i in range(3):
            row = list(map(int, input(f"  Row {i + 1}: ").split()))
            state.append(row)
    else:
        print("Invalid choice - using Easy example.")
        state = initial1

    print()
    hill_climbing(state)
