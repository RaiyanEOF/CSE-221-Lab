import sys
from math import gcd

input = sys.stdin.readline
n, q = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and gcd(i, j) == 1:
            graph[i].append(j)

for j in range(q):
    x, k = map(int, input().split())

    if k <= len(graph[x]):
        print(graph[x][k - 1])
    else:
        print(-1)
