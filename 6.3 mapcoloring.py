def solve_map_coloring():
    graph = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
        "T": [],
    }
    colors = ["red", "green", "blue"]
    assignment = {}

    def backtrack():
        if len(assignment) == len(graph):
            return True

        node = min(graph.keys(), key=lambda x: x not in assignment)
        for color in colors:
            if is_safe(node, color):
                assignment[node] = color
                if backtrack():
                    return True
                del assignment[node]
        return False

    def is_safe(node, color):
        for neighbor in graph[node]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True

    if backtrack():
        print("Map Coloring Solution (Australia):")
        for region, color in sorted(assignment.items()):
            print(f"  {region}: {color}")
    else:
        print("No solution")


solve_map_coloring()
