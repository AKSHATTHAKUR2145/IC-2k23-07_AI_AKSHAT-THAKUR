"""BFS maze solver. 0 = free cell, 1 = wall."""
from collections import deque

def solve_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    q=deque([start]); parent={start:None}
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        r,c=q.popleft()
        if (r,c)==goal:
            path=[]
            cur=goal
            while cur is not None: path.append(cur); cur=parent[cur]
            return path[::-1]
        for dr,dc in directions:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==0 and (nr,nc) not in parent:
                parent[(nr,nc)]=(r,c); q.append((nr,nc))
    return None

if __name__=="__main__":
    grid=[[0,0,1,0],[1,0,1,0],[0,0,0,0],[0,1,1,0]]
    print(solve_maze(grid,(0,0),(3,3)))
