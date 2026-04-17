import sys
from collections import deque
input = sys.stdin.readline
R, H = map(int, input().split())
grid = [input().strip() for i in range(R)]
visited = [[False]*H for i in range(R)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dmd = 0
    while q:
        i, j = q.popleft()
        if grid[i][j] == 'D':
            dmd += 1
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0 <= ni < R and 0 <= nj < H:
                if not visited[ni][nj] and grid[ni][nj] != '#':
                    visited[ni][nj] = True
                    q.append((ni,nj))
    return dmd

ans = 0
for i in range(R):
    for j in range(H):
        if not visited[i][j] and grid[i][j] != '#':
            ans = max(ans,bfs(i,j))
print(ans)
