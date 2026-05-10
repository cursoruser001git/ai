#3,5,4; 6,4,2; 7,3,5
from collections import deque

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

def water_jug_bfs(cap1, cap2, target):
    # Sanity Checks
    if target > max(cap1, cap2):
        print("Error: Target cannot exceed jug capacity.")
        return None
    if target % gcd(cap1, cap2) != 0:
        print("Error: No solution possible (GCD rule).")
        return None

    # Queue for BFS: stores (current_state, path_history)
    # State is (jug1_amount, jug2_amount)
    queue = deque()
    start_state = (0, 0)
    queue.append((start_state, [start_state]))
    
    visited = set()
    visited.add(start_state)
    
    print(f"\n--- BFS Solving (Shortest Path) ---")

    while queue:
        current_state, path = queue.popleft() # Dequeue (FIFO)
        j1, j2 = current_state

        # Check Goal
        if j1 == target or j2 == target:
            return path

        # Generate all possible next moves
        moves = []
        moves.append((cap1, j2)) # Fill 1
        moves.append((j1, cap2)) # Fill 2
        moves.append((0, j2))    # Empty 1
        moves.append((j1, 0))    # Empty 2
        
        # Pour 1 -> 2
        pour_1_to_2 = min(j1, cap2 - j2)
        moves.append((j1 - pour_1_to_2, j2 + pour_1_to_2))
        
        # Pour 2 -> 1
        pour_2_to_1 = min(j2, cap1 - j1)
        moves.append((j1 + pour_2_to_1, j2 - pour_2_to_1))

        for move in moves:
            if move not in visited:
                visited.add(move)
                queue.append((move, path + [move]))

    return None

if __name__ == "__main__":
    try:
        c1 = int(input("Jug 1 Capacity: "))
        c2 = int(input("Jug 2 Capacity: "))
        goal = int(input("Target Amount: "))
        
        path = water_jug_bfs(c1, c2, goal)
        
        if path:
            print(f"\nSUCCESS: Target of {goal}L reached in {len(path)-1} moves.")
            print("=" * 50)
            
            for i, state in enumerate(path):
                # Calculate action
                if i == 0:
                    action = "STARTING STATE"
                else:
                    action = get_action_name(path[i-1], state, c1, c2)
                
                j1, j2 = state
                
                # Print nicely formatted block
                print(f"STEP {i}: {action}")
                print(f"   (Jug A: {j1}L, Jug B: {j2}L)")
                
                # Print an arrow unless it's the last step
                if i < len(path) - 1:
                    print("         │")
                    print("         ▼")
            print("=" * 50)
    except ValueError:
        print("Invalid input.")