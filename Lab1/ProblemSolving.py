"""Missionaries & Cannibals and Vacuum Cleaner world."""

from collections import deque

def missionaries_cannibals():
    # state = (missionaries_left, cannibals_left, boat_side); side 0 left, 1 right
    start, goal = (3, 3, 0), (0, 0, 1)
    moves = [(2,0),(0,2),(1,1),(1,0),(0,1)]
    def safe(m, c):
        mr, cr = 3-m, 3-c
        return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (mr == 0 or mr >= cr)
    q = deque([(start, [start])]); seen = {start}
    while q:
        s, path = q.popleft()
        if s == goal: return path
        m,c,side = s
        for dm,dc in moves:
            nm,nc = (m-dm,c-dc) if side == 0 else (m+dm,c+dc)
            ns = (nm,nc,1-side)
            if safe(nm,nc) and ns not in seen:
                seen.add(ns); q.append((ns,path+[ns]))
    return None

def vacuum_cleaner(initial=("Dirty","Dirty"), start=0):
    rooms = list(initial); position = start; actions = []
    for _ in range(10):
        if rooms[position] == "Dirty":
            rooms[position] = "Clean"; actions.append(f"Suck room {position}")
        elif position == 0:
            position = 1; actions.append("Move Right")
        elif position == 1:
            position = 0; actions.append("Move Left")
        if all(x == "Clean" for x in rooms): break
    return actions, rooms

if __name__ == "__main__":
    print("Missionaries & Cannibals:", missionaries_cannibals())
    print("Vacuum:", vacuum_cleaner())
