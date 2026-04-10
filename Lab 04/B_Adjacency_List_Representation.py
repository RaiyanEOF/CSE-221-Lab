import sys
input = sys.stdin.readline
 
N,E = map(int,input().split())
U = list(map(int,input().split()))
V = list(map(int,input().split()))
W = list(map(int,input().split()))
 
adj = [[] for i in range(N + 1)]
for i in range(E) :
    adj[U[i]].append((V[i],W[i]))
 
for i in range(1,N+1):
    print(i, end=": ")
    for node,weight in adj[i]:
        print(f"({node},{weight})",end =" ")
    print()
