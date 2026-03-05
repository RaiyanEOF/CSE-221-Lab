import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    left = 0
    right = len(arr) 
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left = 0
    right = len(arr)   
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    x, y = map(int, input().split())   
    left_index = lower_bound(arr, x)
    right_index = upper_bound(arr, y)   
    print(right_index - left_index)
