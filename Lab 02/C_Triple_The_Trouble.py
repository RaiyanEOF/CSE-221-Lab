import sys
input = sys.stdin.readline
n, x = map(int, input().split())
arr = list(map(int, input().split()))

nums = [(arr[i], i+1) for i in range(n)]
nums.sort()

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        total = nums[i][0] + nums[left][0] + nums[right][0]

        if total == x:
            print(nums[i][1], nums[left][1], nums[right][1])
            sys.exit(0)
        elif total < x:
            left += 1
        else:
            right -= 1

print(-1)
