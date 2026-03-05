N, S = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = N - 1

while left < right:
    total = arr[left] + arr[right]

    if total == S:
        print(left + 1, right + 1)   
        break
    elif total < S:
        left = left + 1
    else:
        right = right - 1
else:
    print(-1)
