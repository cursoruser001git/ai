from heapq import heappush, heappop


def bfs_8puzzle(start, goal):
    def get_neighbors(state):
        pos = state.index(0)
        moves = []
        row, col = pos // 3, pos % 3
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_pos = nr * 3 + nc
                new_state = list(state)
                new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]
                moves.append(tuple(new_state))
        return moves

    def heuristic(state):
        count = 0
        for i in range(9):
            if state[i] != 0 and state[i] != goal[i]:
                count += 1
        return count

    pq = [(heuristic(start), 0, start)]
    visited = {start: 0}
    parent = {}

    while pq:
        _, cost, current = heappop(pq)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], cost

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = cost + 1
                parent[neighbor] = current
                heappush(pq, (heuristic(neighbor), cost + 1, neighbor))

    return None, None


start = (1, 2, 3, 4, 5, 6, 7, 8, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 0, 8)

path, steps = bfs_8puzzle(start, goal)
if path:
    print(f"Solved in {steps} moves")
    for state in path:
        for i in range(3):
            print(state[i * 3 : (i + 1) * 3])
        print()
