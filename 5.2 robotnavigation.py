from heapq import heappush, heappop


def astar_robot_navigation(grid, start, goal):
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    pq = [(heuristic(start), 0, start)]
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

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
                new_g = g + 1
                if (nr, nc) not in visited or visited[(nr, nc)] > new_g:
                    parent[(nr, nc)] = current
                    heappush(pq, (heuristic((nr, nc)) + new_g, new_g, (nr, nc)))

    return None, None


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
goal = (4, 4)

path, cost = astar_robot_navigation(grid, start, goal)
if path:
    print(f"Path found with {cost} moves:")
    for pos in path:
        print(pos)
else:
    print("No path found")
