import sys
from collections import deque
input = sys.stdin.readline
N, E, S, D = map(int, input().split())
adj = [[] for i in range(N + 1)]

for i in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

sou = list(map(int,input().split()))
des = list(map(int,input().split()))

dist = [-1]*(N+1)
q = deque()

for s in sou:
    dist[s] = 0
    q.append(s)
while q:
    node = q.popleft()
    for nx in adj[node]:
        if dist[nx] == -1:
            dist[nx] = dist[node] + 1
            q.append(nx)
result = []
for d in des:
    result.append(str(dist[d]))
print(" ".join(result))
