t = int(input())

for i in range(t):
    expression = input().strip()  
    split = expression.split()  
    n1 = float(split[1])
    op = split[2]
    n2 = float(split[3])
    
    if op == '+':
        res = n1+n2
    elif op == '-':
        res = n1-n2
    elif op == '*':
        res = n1*n2
    elif op == '/':
        res = n1/n2
    
    print(f"{res:.6f}")
