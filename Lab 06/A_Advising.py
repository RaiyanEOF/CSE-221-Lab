import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for i in range(t) :
    n,e  = map(int,input().split())
    adj_list = [[] for i in range(n+1)]
    indegree = [0]*(n+1)
    for i in range(e) :
        u,v  = map(int,input().split())
        adj_list[u].append(v)
        indegree[v] += 1
    
    queue = deque()
    for i in range(1,n+1) :
        if indegree[i] == 0 :
            queue.append(i)
    
    topo = []
    while queue :
        node = queue.popleft()
        topo.append(node)
        for neighbor in adj_list[node] :
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0 :
                queue.append(neighbor)

    if len(topo) != n :
        print(-1)
    else :
        print(*topo)   
