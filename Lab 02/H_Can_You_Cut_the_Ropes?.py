import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
ropes = list(map(int, input().split()))
 
low = 1
high = max(ropes)
ans = -1
 
while low <= high:
    mid = (low + high) // 2
    pieces = 0
    for length in ropes:
        pieces += length // mid
    if pieces >= k:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1
print(ans)
