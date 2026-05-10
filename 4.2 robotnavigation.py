from heapq import heappush, heappop


def best_first_robot_navigation(grid, start, goal):
    def heuristic(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])

    pq = [(heuristic(start), start)]
    visited = set()
    parent = {}
    cost_so_far = {start: 0}

    while pq:
        _, current = heappop(pq)
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        visited.add(current)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = current[0] + dr, current[1] + dc
            if (
                0 <= nr < len(grid)
                and 0 <= nc < len(grid[0])
                and grid[nr][nc] != 1
                and (nr, nc) not in visited
            ):
                new_cost = cost_so_far[current] + 1
                if (nr, nc) not in cost_so_far or new_cost < cost_so_far[(nr, nc)]:
                    cost_so_far[(nr, nc)] = new_cost
                    parent[(nr, nc)] = current
                    heappush(pq, (heuristic((nr, nc)), (nr, nc)))

    return None


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
goal = (4, 4)

path = best_first_robot_navigation(grid, start, goal)
if path:
    print(f"Path found with {len(path) - 1} moves:")
    for pos in path:
        print(pos)
else:
    print("No path found")
