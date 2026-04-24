import sys
import heapq
input = sys.stdin.readline
n = int(input())
words = [input().strip() for i in range(n)]
graph = [[] for i in range(26)]
indeg = [0]*26
used = [0]*26
for w in words:
    for c in w:
        used[ord(c)-97] = 1

for i in range(n-1):
    a = words[i]
    b = words[i+1]
    m = min(len(a),len(b))
    if len(a) > len(b) and a[:m] == b[:m]:
        print(-1)
        sys.exit()
    for j in range(m):
        if a[j] != b[j]:
            u = ord(a[j])-97
            v = ord(b[j])-97
            graph[u].append(v)
            indeg[v] += 1
            break

heap = []
for i in range(26):
    if used[i] and indeg[i] == 0:
        heapq.heappush(heap, i)
ans = []
while heap:
    u = heapq.heappop(heap)
    ans.append(chr(u+97))
    for v in graph[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            heapq.heappush(heap, v)
if len(ans) != sum(used):
    print(-1)
else:
    print("".join(ans))
