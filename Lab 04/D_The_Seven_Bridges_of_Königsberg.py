import sys
input = sys.stdin.readline

N,E = list(map(int,input().split()))
u = list(map(int,input().split()))
v = list(map(int,input().split()))

degree = [0]*(N+1)

for i in range(E):
    degree[u[i]] += 1
    degree[v[i]] += 1

odd = 0
for i in range(1,N+1) :
    if degree[i] % 2 != 0 :
        odd += 1

if odd==0 or odd==2 :
    print("YES")
else :
    print("NO")
