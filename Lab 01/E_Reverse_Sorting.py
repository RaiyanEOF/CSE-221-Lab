from collections import Counter
n = int(input())
a = list(map(int, input().split()))
b = sorted(a)

even_a = [a[i] for i in range(0,n,2)]
odd_a  = [a[i] for i in range(1,n,2)]
even_b = [b[i] for i in range(0,n,2)]
odd_b  = [b[i] for i in range(1,n,2)]

if Counter(even_a) != Counter(even_b) or Counter(odd_a) != Counter(odd_b):
    print("NO")
    exit()

ops = []

for i in range(n):
    if a[i] == b[i]:
        continue
    j = i + 1
    while j < n and not (a[j] == b[i] and (j % 2) == (i % 2)):
        j += 1
    while j > i:
        pos = j - 2
        a[pos], a[pos+1], a[pos+2] = a[pos+2], a[pos+1], a[pos]
        ops.append((pos+1,pos+3))
        j -= 2


if a == b:
    print("YES")
    print(len(ops))
    for l, r in ops:
        print(l, r)
else:
    print("NO")
