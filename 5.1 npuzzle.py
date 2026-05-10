from heapq import heappush, heappop


def astar_n_puzzle(start, goal, size=3):
    def get_neighbors(state):
        pos = state.index(0)
        row, col = pos // size, pos % size
        moves = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size:
                new_pos = nr * size + nc
                new_state = list(state)
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                moves.append(tuple(new_state))
        return moves

    def manhattan(state):
        dist = 0
        for i in range(size * size):
            if state[i] != 0:
                target_row = (state[i] - 1) // size
                target_col = (state[i] - 1) % size
                curr_row, curr_col = i // size, i % size
                dist += abs(curr_row - target_row) + abs(curr_col - target_col)
        return dist

    pq = [(manhattan(start), 0, start)]
    visited = {}
    parent = {}

    while pq:
        f, g, current = heappop(pq)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], g

        if current in visited and visited[current] <= g:
            continue
        visited[current] = g

        for neighbor in get_neighbors(current):
            if neighbor not in visited or visited[neighbor] > g + 1:
                parent[neighbor] = current
                heappush(pq, (manhattan(neighbor) + g + 1, g + 1, neighbor))

    return None, None


start = (1, 2, 3, 4, 5, 6, 7, 8, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 0, 8)

path, moves = astar_n_puzzle(start, goal)
if path:
    print(f"Solved in {moves} moves")
    for state in path:
        for i in range(3):
            print(state[i * 3 : (i + 1) * 3])
        print()
