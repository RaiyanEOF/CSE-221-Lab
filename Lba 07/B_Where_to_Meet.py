import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
def reachable(start, adj_list, n) :
    dist = [INF]*(n+1)
    dist[start] = 0
    pq = [(0,start)]
    while pq :
        d,u = heapq.heappop(pq)
        if d > dist[u] :
            continue
        for v,w in adj_list[u] :
            if dist[v] > d + w :
                dist[v] = d + w
                heapq.heappush(pq,(dist[v],v))
    return dist
n,e,s,t  = map(int,input().split())
adj_list = [[] for i in range(n+1)]
for i in range(e) :
    u,v,w = map(int,input().split())
    adj_list[u].append((v,w))

distS = reachable(s,adj_list,n)
distT = reachable(t,adj_list,n)
best_time = INF
best_node = -1

for i in range(1,n+1) :
    if distS[i] < INF and distT[i] < INF :
        t = max(distS[i],distT[i])
        if t < best_time or (t==best_time and i < best_node) :
            best_time = t
            best_node = i

if best_node == -1 :
    print(-1)
else :
    print(best_time, best_node)
