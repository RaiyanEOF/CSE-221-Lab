import sys
input = sys.stdin.readline
N,E,Q = map(int,input().split())
parent = list(range(N+1))
rank = [0]*(N+1)

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b) :
    pa = find(a)
    pb = find(b)
    if pa == pb :
        return
    if rank[pa] < rank[pb] :
        parent[pa] = pb
    else :
        parent[pb] = pa
        if rank[pa] == rank[pb] :
            rank[pa] += 1

for i in range(E) :
    U,V  = map(int,input().split())
    union(U,V)

for i in range(Q) :
    X,Y = map(int,input().split())
    if find(X) == find(Y) :
        print("YES")
    else :
        print("NO") 
