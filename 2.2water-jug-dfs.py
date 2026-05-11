def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_action_name(old_state, new_state, cap1, cap2):
    """Identifies the action taken between two states."""
    j1_old, j2_old = old_state
    j1_new, j2_new = new_state
    
    if j1_new == cap1 and j1_old != cap1: return "Fill Jug 1"
    if j2_new == cap2 and j2_old != cap2: return "Fill Jug 2"
    if j1_new == 0 and j1_old != 0:       return "Empty Jug 1"
    if j2_new == 0 and j2_old != 0:       return "Empty Jug 2"
    if j1_new < j1_old:                   return "Pour Jug 1 -> Jug 2"
    if j2_new < j2_old:                   return "Pour Jug 2 -> Jug 1"
    return "Start"

def water_jug_dfs(cap1, cap2, target):
    if target > max(cap1, cap2) or target % gcd(cap1, cap2) != 0:
        print("Error: No solution possible.")
        return None

    stack = []
    start_state = (0, 0)
    stack.append((start_state, [start_state]))
    
    visited = set()
    visited.add(start_state)
    
    print(f"\n--- DFS Solving (Deep Path) ---")

    while stack:
        current_state, path = stack.pop() 
        j1, j2 = current_state

        if j1 == target or j2 == target:
            return path

        
        moves = []
        moves.append((cap1, j2)) 
        moves.append((j1, cap2)) 
        moves.append((0, j2))    
        moves.append((j1, 0))    
        
        
        pour_1_to_2 = min(j1, cap2 - j2)
        moves.append((j1 - pour_1_to_2, j2 + pour_1_to_2))
        
        
        pour_2_to_1 = min(j2, cap1 - j1)
        moves.append((j1 + pour_2_to_1, j2 - pour_2_to_1))

        for move in moves:
            if move not in visited:
                visited.add(move)
                stack.append((move, path + [move]))

    return None

if __name__ == "__main__":
    try:
        c1 = int(input("Jug 1 Capacity: "))
        c2 = int(input("Jug 2 Capacity: "))
        goal = int(input("Target Amount: "))
        
        path = water_jug_dfs(c1, c2, goal)
        
        if path:
            print(f"\nSUCCESS: Target of {goal}L reached in {len(path)-1} moves.")
            print("=" * 50)
            
            for i, state in enumerate(path):
                if i == 0:
                    action = "STARTING STATE"
                else:
                    action = get_action_name(path[i-1], state, c1, c2)
                
                j1, j2 = state
                
                print(f"STEP {i}: {action}")
                print(f"   (Jug A: {j1}L, Jug B: {j2}L)")
                
                if i < len(path) - 1:
                    print("         │")
                    print("         ▼")
            print("=" * 50)
    except ValueError:
        print("Invalid input.")
