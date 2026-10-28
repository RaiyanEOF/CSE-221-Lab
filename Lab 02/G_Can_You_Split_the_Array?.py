import sys
input = sys.stdin.readline
 
n, k = map(int, input().split())
arr = list(map(int, input().split()))
 
low = max(arr)
high = sum(arr)
ans = high
 
while low <= high:
    mid = (low + high) // 2
    parts = 1
    total = 0
    for x in arr:
        if total + x > mid:
            parts += 1
            total = x
        else:
            total += x
    if parts <= k:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
print(ans)
