import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k, x = map(int, input().split())
    print(k+(k - 1)//(x - 1))
