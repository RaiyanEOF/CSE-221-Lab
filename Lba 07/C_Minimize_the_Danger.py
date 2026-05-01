import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n,e = map(int, input().split())
adj = [[] for i in range(n+1)]
for i in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w)) 

dist = [INF]*(n+1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v,w in adj[u]:
        new_danger = max(dist[u],w)
        if new_danger < dist[v]:
            dist[v] = new_danger
            heapq.heappush(pq, (dist[v], v))

for i in range(1,n+1):
    if dist[i] == INF:
        print(-1, end=" ")
    else:
        print(dist[i], end=" ")
