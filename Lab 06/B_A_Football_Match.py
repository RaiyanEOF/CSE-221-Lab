import sys
from collections import deque
input = sys.stdin.readline

n,e = map(int,input().split())
adj_list = [[] for i in range(n+1)]
visited = [-1]*(n+1)
for i in range(e) :
    u,v = map(int,input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

ans = 0
for i in range(1,n+1) :
    if visited[i] == -1 :
        q = deque()
        q.append(i)
        visited[i] = 0
        count= [1,0] 
        while q :
            node = q.popleft()
            for neighbor in adj_list[node] :
                if visited[neighbor] == -1 :
                    visited[neighbor] = 1 - visited[node]
                    count[visited[neighbor]] += 1
                    q.append(neighbor)
        ans += max(count)
print(ans)
