from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
adj = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


visited = [False]*(N+1)
queue = deque()
bfs_order = []


queue.append(1)
visited[1] = True

while queue:
    u = queue.popleft()
    bfs_order.append(u)
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)

print(*bfs_order)
