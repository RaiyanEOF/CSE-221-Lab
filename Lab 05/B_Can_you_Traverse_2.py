import sys
input = sys.stdin.readline

N, M = map(int,input().split())

u_list = list(map(int, input().split()))
v_list = list(map(int, input().split()))

adj = [[] for i in range(N+1)]
for i in range(M):
    u = u_list[i]
    v = v_list[i]
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N+1)
dfs_order = []

stack = [1]

while stack:
    u = stack.pop()
    if not visited[u]:
        visited[u] = True
        dfs_order.append(u)
        for v in reversed(adj[u]):
            if not visited[v]:
                stack.append(v)

print(*dfs_order)
