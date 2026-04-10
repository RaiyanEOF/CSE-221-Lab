import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
knights = set()

for i in range(K) :
    x,y = map(int,input().split())
    knights.add((x,y))

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

for x,y in knights :
    for i in range(8) :
        nx = x + dx[i]
        ny = y + dy[i]
        if 1<=nx<=N and 1<=ny<=M :
            if(nx,ny) in knights :
                print("YES")
                sys.exit()
print("NO")
