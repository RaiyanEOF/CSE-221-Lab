import sys
input = sys.stdin.readline

N,E = map(int, input().split())

u = list(map(int, input().split()))
v = list(map(int, input().split()))

indegree = [0]*(N + 1)
outdegree = [0]*(N + 1)

for i in range(E):
    outdegree[u[i]] += 1
    indegree[v[i]] += 1

result = []
for i in range(1, N + 1):
    result.append(str(indegree[i] - outdegree[i]))

print(" ".join(result))
