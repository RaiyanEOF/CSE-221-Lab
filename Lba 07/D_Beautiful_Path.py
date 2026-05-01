import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n, e, s, dest = map(int, input().split())
weight = [0] + list(map(int, input().split()))
adj = [[] for i in range(n + 1)]
for i in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)

dist = [INF]*(n + 1)
dist[s] = weight[s]
pq = [(dist[s], s)]

while pq:
    curd, u = heapq.heappop(pq) 
    if curd > dist[u]:
        continue
    for v in adj[u]:
        new_cost = dist[u] + weight[v]
        if new_cost < dist[v]:
            dist[v] = new_cost
            heapq.heappush(pq, (dist[v], v))

if dist[dest] == INF:
    print(-1)
else:
    print(dist[dest])
