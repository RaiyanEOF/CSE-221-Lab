n = int(input())
a = list(map(int, input().split()))

while True:
    swapped = False
    
    for i in range(n - 1):
        if (a[i] % 2 == a[i + 1] % 2) and (a[i] > a[i + 1]):
            a[i], a[i + 1] = a[i + 1], a[i]
            swapped = True
    
    if not swapped:
        break

for x in a:
    print(x, end=' ')
