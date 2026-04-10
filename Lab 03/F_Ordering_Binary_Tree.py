import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = []

def build(l,r):
    if l>r:
        return   
    mid = (l + r)//2
    result.append(arr[mid])  
    build(l,mid-1)
    build(mid+1,r)

build(0,n-1)
print(*result)
