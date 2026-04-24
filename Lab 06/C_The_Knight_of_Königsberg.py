from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),(1, 2), (1, -2), (-1, 2), (-1, -2)]
visited = [[-1]*N for i in range(N)]

q = deque()
q.append((x1, y1))
visited[x1][y1] = 0

while q:
    x, y = q.popleft()   
    if x == x2 and y == y2:
        print(visited[x][y])
        exit()
    for cx,cy in moves:
        nx = x + cx
        ny = y + cy      
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))
print(-1)
