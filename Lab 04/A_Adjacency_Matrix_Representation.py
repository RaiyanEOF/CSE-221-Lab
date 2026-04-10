import sys 
input = sys.stdin.readline
N,E = map(int,input().split())
 
adj = [[0]*N for i in range(N)]
for i in range(E) :
    U,V,W = map(int,input().split())
    adj[U-1][V-1] = W
 
for i in range(N) :
    for j in range(N) :
        print(adj[i][j], end=" ")
    print()
