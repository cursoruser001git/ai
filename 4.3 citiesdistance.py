from heapq import heappush, heappop


def best_first_cities(cities, distances, start, goal):
    def heuristic(city):
        return abs(cities[city][0] - cities[goal][0]) + abs(
            cities[city][1] - cities[goal][1]
        )

    pq = [(heuristic(start), start)]
    visited = set()
    parent = {}

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

        if current in distances:
            for neighbor in distances[current]:
                if neighbor not in visited:
                    parent[neighbor] = current
                    heappush(pq, (heuristic(neighbor), neighbor))

    return None


cities = {"A": (0, 0), "B": (2, 3), "C": (5, 5), "D": (8, 2), "E": (10, 8)}

distances = {
    "A": {"B": 4, "C": 7},
    "B": {"A": 4, "C": 3, "D": 5},
    "C": {"A": 7, "B": 3, "D": 2, "E": 4},
    "D": {"B": 5, "C": 2, "E": 3},
    "E": {"C": 4, "D": 3},
}

path = best_first_cities(cities, distances, "A", "E")
if path:
    print("Shortest path:", " -> ".join(path))
    total = 0
    for i in range(len(path) - 1):
        total += distances[path[i]][path[i + 1]]
    print(f"Total distance: {total}")
else:
    print("No path found")
