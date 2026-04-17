import sys
input = sys.stdin.readline
N, R = map(int, input().split())
adj_list = [[] for i in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

subtree = [0]*(N+1)
parent = [-1]*(N+1)

stack = [R]
order = []

while stack :
    node = stack.pop()
    order.append(node)
    for neighbor in adj_list[node] :
        if neighbor != parent[node] :
            parent[neighbor] = node
            stack.append(neighbor)

for node in reversed(order) :
    subtree[node] = 1
    for neighbor in adj_list[node] :
        if neighbor != parent[node] :
            parent[neighbor] = node
            subtree[node] += subtree[neighbor]

Q = int(input())
for i in range(Q) :
    x = int(input())
    print(subtree[x])

