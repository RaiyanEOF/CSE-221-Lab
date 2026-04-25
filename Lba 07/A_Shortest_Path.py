import sys, heapq
input = sys.stdin.readline
N, M, S, D = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))
g = [[] for _ in range(N+1)]
for i in range(M):
    g[u[i]].append((v[i], w[i]))
INF = float('inf')
dist = [INF]*(N+1)
par = [-1]*(N+1)
dist[S] = 0
pq = [(0, S)]
while pq:
    d, x = heapq.heappop(pq)
    if d > dist[x]:
        continue
    for nx, wt in g[x]:
        if d + wt < dist[nx]:
            dist[nx] = d + wt
            par[nx] = x
            heapq.heappush(pq, (dist[nx], nx))
if dist[D] == INF:
    print(-1)
else:
    print(dist[D])
    path = []
    curr = D
    while curr != -1:
        path.append(curr)
        curr = par[curr]
    path.reverse()
    print(*path)
