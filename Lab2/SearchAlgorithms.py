"""BFS, DFS, Hill Climbing, Greedy Best-First Search and A*."""
from collections import deque
import heapq

GRAPH = {
    "A": {"B": 1, "C": 4}, "B": {"D": 2, "E": 5},
    "C": {"F": 1}, "D": {"G": 3}, "E": {"G": 1}, "F": {"G": 2}, "G": {}
}
H = {"A": 6, "B": 4, "C": 3, "D": 2, "E": 1, "F": 2, "G": 0}

def reconstruct(parent, goal):
    path = []
    while goal is not None:
        path.append(goal); goal = parent.get(goal)
    return path[::-1]

def bfs(graph, start, goal):
    q=deque([start]); parent={start:None}
    while q:
        u=q.popleft()
        if u==goal: return reconstruct(parent,goal)
        for v in graph[u]:
            if v not in parent: parent[v]=u; q.append(v)
    return None

def dfs(graph, start, goal):
    stack=[start]; parent={start:None}
    while stack:
        u=stack.pop()
        if u==goal: return reconstruct(parent,goal)
        for v in reversed(list(graph[u])):
            if v not in parent: parent[v]=u; stack.append(v)
    return None

def hill_climbing(graph, heuristic, start, goal):
    path=[start]; current=start
    while current != goal:
        candidates=list(graph[current])
        if not candidates: return path
        nxt=min(candidates,key=lambda x:heuristic[x])
        if heuristic[nxt] >= heuristic[current]: return path # local optimum
        current=nxt; path.append(current)
    return path

def greedy_best_first(graph, heuristic, start, goal):
    pq=[(heuristic[start],start)]; parent={start:None}; visited=set()
    while pq:
        _,u=heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        if u==goal: return reconstruct(parent,goal)
        for v in graph[u]:
            if v not in parent: parent[v]=u
            heapq.heappush(pq,(heuristic[v],v))
    return None

def astar(graph, heuristic, start, goal):
    pq=[(heuristic[start],0,start)]; parent={start:None}; g={start:0}
    while pq:
        _,cost,u=heapq.heappop(pq)
        if u==goal: return reconstruct(parent,goal),cost
        if cost != g[u]: continue
        for v,w in graph[u].items():
            new_cost=cost+w
            if new_cost < g.get(v,float("inf")):
                g[v]=new_cost; parent[v]=u
                heapq.heappush(pq,(new_cost+heuristic[v],new_cost,v))
    return None,None

if __name__=="__main__":
    for name,fn in [("BFS",bfs),("DFS",dfs)]:
        print(name,fn(GRAPH,"A","G"))
    print("Hill climbing:",hill_climbing(GRAPH,H,"A","G"))
    print("Greedy:",greedy_best_first(GRAPH,H,"A","G"))
    print("A*:",astar(GRAPH,H,"A","G"))
