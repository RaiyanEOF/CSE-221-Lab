import sys
input = sys.stdin.readline

n = int(input())
mat = [[0]*n for i in range(n)]

for i in range(n) :
    nodes = list(map(int,input().split()))
    for j in range(1,len(nodes)) :
        edge = nodes[j]
        mat[i][edge] = 1

for row in mat :
    for val in row :
        print(val,end =" ")
    print()
