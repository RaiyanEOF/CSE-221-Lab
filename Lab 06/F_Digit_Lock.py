import sys
from collections import deque
input = sys.stdin.readline
S, C = input().split()
n = int(input())
invalid = set()
for i in range(n):
    invalid.add(input().strip())
visited = set()
q = deque()
q.append((S, 0))
visited.add(S)
while q:
    strt,st = q.popleft()   
    if strt == C:
        print(st)
        break
    for i in range(4):
        dig = int(strt[i])
        for move in (-1, 1):
            nd = (dig + move) % 10
            new_strt = strt[:i] + str(nd) + strt[i+1:]
            if new_strt not in visited and new_strt not in invalid:
                visited.add(new_strt)
                q.append((new_strt,st+1))
else:
    print(-1)
