import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

spf = list(range(N + 1))
for i in range(2, int(N**0.5) + 1):
    if spf[i] == i:
        for j in range(i*i, N + 1, i):
            if spf[j] == j:
                spf[j] = i

def primes(x):
    p = []
    while x > 1:
        d = spf[x]
        p.append(d)
        while x % d == 0:
            x //= d
    return list(set(p))

def count(m, p, X):
    res = 0
    n = len(p)
    for mask in range(1 << n):
        mul = 1
        bits = 0
        for i in range(n):
            if mask & (1 << i):
                mul *= p[i]
                bits += 1
        if mul > m:
            continue
        if bits % 2 == 0:
            res += m // mul
        else:
            res -= m // mul
    if X == 1:  
        res -= 1
    return res

def kth(X, K):
    p = primes(X)
    lo, hi = 1, N
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid, p, X) >= K:
            hi = mid
        else:
            lo = mid + 1
    return lo if count(lo, p, X) >= K else -1

for i in range(Q):
    X, K = map(int, input().split())
    print(kth(X, K))
