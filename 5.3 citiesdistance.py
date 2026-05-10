from heapq import heappush, heappop


def astar_cities(cities, distances, start, goal):
    def heuristic(city):
        return abs(cities[city][0] - cities[goal][0]) + abs(
            cities[city][1] - cities[goal][1]
        )

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

        if current in distances:
            for neighbor in distances[current]:
                new_g = g + distances[current][neighbor]
                if neighbor not in visited or visited[neighbor] > new_g:
                    parent[neighbor] = current
                    heappush(pq, (heuristic(neighbor) + new_g, new_g, neighbor))

    return None, None


cities = {"A": (0, 0), "B": (2, 3), "C": (5, 5), "D": (8, 2), "E": (10, 8)}

distances = {
    "A": {"B": 4, "C": 7},
    "B": {"A": 4, "C": 3, "D": 5},
    "C": {"A": 7, "B": 3, "D": 2, "E": 4},
    "D": {"B": 5, "C": 2, "E": 3},
    "E": {"C": 4, "D": 3},
}

path, cost = astar_cities(cities, distances, "A", "E")
if path:
    print("Shortest path:", " -> ".join(path))
    print(f"Total distance: {cost}")
else:
    print("No path found")
