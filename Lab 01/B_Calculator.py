import sys
input = sys.stdin.readline
 
t = int(input())
 
for i in range(t):
    expr = input().split()
    a = float(expr[1])
    op = expr[2]
    b = float(expr[3])
 
    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a / b
    elif op == '%':
        res = a % b
    elif op == '&':
        res = int(a) & int(b)
    elif op == '|':
        res = int(a) | int(b)
    elif op == '^':
        res = int(a) ^ int(b)
    elif op == '<<':
        res = int(a) << int(b)
    elif op == '>>':
        res = int(a) >> int(b)
 
    print(f"{res:.6f}")
