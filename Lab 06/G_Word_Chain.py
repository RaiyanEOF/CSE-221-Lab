import sys
from collections import deque
input = sys.stdin.readline
n, A, B = input().split()
n = int(n)
words = [input().strip() for i in range(n)]
group = [[] for i in range(26)]
for i in range(n):
    group[ord(words[i][0])-65].append(i)

start = words.index(A)
target = words.index(B)
visited = [False]*n
visited[start] = True
q = deque([start])
while q:
    i = q.popleft()
    if i == target:
        print("YES")
        break
    last = ord(words[i][-1]) - 65
    for j in group[last]:
        if not visited[j]:
            visited[j] = True
            q.append(j)
    group[last] = []   
else:
    print("NO")
