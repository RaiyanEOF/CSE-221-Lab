import sys
import heapq
input = sys.stdin.readline
INF = float('inf')
n,e,s,d = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
first_dist = [INF]*(n+1)
second_dist = [INF]*(n+1)
first_dist[s] = 0
pq = [(0,s)]

while pq:
    curr_dist, u = heapq.heappop(pq)
    for v, w in graph[u]:
        new_dist = curr_dist + w
        if new_dist < first_dist[v]:
            second_dist[v] = first_dist[v]
            first_dist[v] = new_dist
            heapq.heappush(pq, (new_dist,v))
        elif first_dist[v] < new_dist < second_dist[v]:
            second_dist[v] = new_dist
            heapq.heappush(pq,(new_dist,v))

if second_dist[d] == INF:
    print(-1)
else:
    print(second_dist[d])
