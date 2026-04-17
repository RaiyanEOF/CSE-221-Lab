import sys
from collections import deque
input = sys.stdin.readline

N,E,S,D = map(int,input().split())
U = list(map(int,input().split()))
V = list(map(int,input().split()))

adj_list = [[] for i in range(N+1)]
for i in range(E) :
    adj_list[U[i]].append(V[i])
    adj_list[V[i]].append(U[i])

for i in range(1,N+1) :
    adj_list[i].sort()

visited = [False]*(N+1)
parent = [-1]*(N+1)
dist = [-1]*(N+1)

q = deque()
q.append(S)
visited[S] = True
dist[S] = 0

while q :
    node = q.popleft()
    if node==D :
        break
    for neighbor in adj_list[node] :
        if not visited[neighbor] :
            visited[neighbor] = True
            parent[neighbor] = node
            dist[neighbor] = dist[node] + 1
            q.append(neighbor)

if not visited[D] :
    print(-1)
else :
    path = []
    curr = D
    while curr != -1 :
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    print(dist[D])
    print(*path)
