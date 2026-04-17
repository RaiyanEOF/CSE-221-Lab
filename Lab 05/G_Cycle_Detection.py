import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for i in range(N+1)]
indegree = [0]*(N+1)

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    indegree[v] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

count = 0
while q :
    node = q.popleft()
    count += 1
    for neighbor in adj[node] :
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0 :
            q.append(neighbor)

if count == N:
    print("NO")   
else:
    print("YES")  
