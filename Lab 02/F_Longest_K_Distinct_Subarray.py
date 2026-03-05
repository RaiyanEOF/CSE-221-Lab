import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
max_len = 0
freq = {}
distinct = 0
for right in range(N):
    if arr[right] not in freq or freq[arr[right]] == 0:
        distinct += 1
        freq[arr[right]] = 0
    freq[arr[right]] += 1
    while distinct > K:
        freq[arr[left]] -= 1
        if freq[arr[left]] == 0:
            distinct -= 1
        left += 1
    max_len = max(max_len, right - left + 1)

print(max_len)
