import sys
input = sys.stdin.readline

def power_and_sum(a, n, m):
    if n == 1:
        return a % m, a % m 
    if n%2==0:
        p_even, s_even = power_and_sum(a,n//2,m)  
        p = (p_even * p_even) % m    
        s = (s_even + p_even * s_even) % m   
        return  p,s
    else:
        p_odd, s_odd = power_and_sum(a,n-1,m)    
        p = (p_odd*a) % m   
        s = (s_odd+p) % m    
        return  p,s


T = int(input())
for i in range(T):
    a, n, m = map(int, input().split())
    if a==1:
        print(n % m)
    else:
        p,result = power_and_sum(a, n, m)
        print(result)
