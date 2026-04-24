import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
adj = [[] for i in range(N + 1)]

for i in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def bfs(start):
    dist = [-1]*(N + 1)
    parent = [-1]*(N + 1)  
    q = deque([start])
    dist[start] = 0   
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                parent[neighbor] = node
                q.append(neighbor)    
    far_node = start
    for i in range(1,N+1):
        if dist[i] > dist[far_node]:
            far_node = i  
    return far_node, dist, parent

A, dist1, par1 = bfs(1)
B, dist2, par2 = bfs(A)
print(dist2[B])
print(A, B)
