import sys
from collections import deque
input = sys.stdin.readline

N,E,S,D,K = map(int,input().split())

adj_list = [[] for i in range(N+1)]
for i in range(E) :
    U,V = map(int,input().split())
    adj_list[U].append(V)

def bfs(s) :
    visited = [False]*(N+1)
    parent = [-1]*(N+1)
    dist = [-1]*(N+1)
    q = deque([s])
    visited[s] = True
    dist[s] = 0
    while q:
        node = q.popleft()
        for neighbor in adj_list[node] :
            if not visited[neighbor] :
                visited[neighbor] = True
                parent[neighbor] = node
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
    return parent, dist

par1,dist1 = bfs(S)
par2,dist2 = bfs(K)

if dist1[K] == -1 or dist2[D] == -1 :
    print(-1)
else :
    path1 = []
    curr = K
    while curr != -1 :
        path1.append(curr)
        curr = par1[curr]
    path1.reverse()

    path2 = []
    curr = D
    while curr != -1 :
        path2.append(curr)
        curr = par2[curr]
    path2.reverse()

    path = path1 + path2[1:]
    print(len(path)-1)
    print(*path)
