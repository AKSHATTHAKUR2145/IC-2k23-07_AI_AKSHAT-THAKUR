"""Lab 1: Water Jug Problem using BFS. Jugs have capacities 4L and 3L."""
from collections import deque

def water_jug(cap_a=4, cap_b=3, target=2):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path
        states = {
            (cap_a, b), (a, cap_b), (0, b), (a, 0),
            (a - min(a, cap_b-b), b + min(a, cap_b-b)),
            (a + min(b, cap_a-a), b - min(b, cap_a-a))
        }
        for nxt in states:
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None

if __name__ == "__main__":
    print("Water jug solution (4L, 3L; target 2L):")
    print(" -> ".join(map(str, water_jug())))
