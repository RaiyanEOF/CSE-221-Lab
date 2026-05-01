import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n,e = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
adj = [[] for i in range(n+1)]
for i in range(e):
    adj[u[i]].append((v[i],w[i]))

dist = [[INF, INF] for i in range(n+1)]
dist[1][0] = 0
dist[1][1] = 0
pq = [(0, 1, 0), (0, 1, 1)]

while pq:
    d, node, p = heapq.heappop(pq)
    if d > dist[node][p]:
        continue
    for nxt, wt in adj[node]:
        np = wt % 2
        if np != p:  
            nd = d + wt
            if nd < dist[nxt][np]:
                dist[nxt][np] = nd
                heapq.heappush(pq, (nd, nxt, np))
ans = min(dist[n][0], dist[n][1])
print(ans if ans < INF else -1)
