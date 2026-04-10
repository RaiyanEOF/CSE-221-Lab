import sys
input = sys.stdin.readline

N = int(input())
x, y = map(int, input().split())

moves = [
    (x-1,y),
    (x+1,y),
    (x,y-1),
    (x,y+1),
    (x-1,y-1),
    (x-1,y+1),
    (x+1,y-1),
    (x+1,y+1)
]

valid = []
for nx,ny in moves :
    if 1<=nx<=N and 1<=ny<=N :
        valid.append((nx,ny))

for i in range(len(valid)) :
    for j in range(i+1,len(valid)) :
        if valid[i][0] > valid [j][0] or (valid[i][0]==valid[j][0] and valid[i][1] > valid[j][1]) :
            temp = valid[i]
            valid[i] = valid[j]
            valid[j] = temp

print(len(valid))
for a,b in valid :
    print(a,b)
