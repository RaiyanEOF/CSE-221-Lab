N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i = 0
j = M - 1

best_diff = float('inf')
best_i = 0
best_j = 0

while i < N and j >= 0:
    current_sum = A[i] + B[j]
    diff = abs(current_sum - K)

    if diff < best_diff:
        best_diff = diff
        best_i = i
        best_j = j

    if current_sum > K:
        j -= 1
    else:
        i += 1

print(best_i + 1, best_j + 1)
