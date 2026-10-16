import sys
input = sys.stdin.readline
 
t = int(input())
 
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    ok = True
 
    for j in range(1,n):
        if a[j] < a[j - 1]:
            ok = False
            break
 
    if ok :
        print("YES")
    else :
        print("NO")
