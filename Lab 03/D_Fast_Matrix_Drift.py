m = 1000000007

def mult(A, B):
    a11 = (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % m
    a12 = (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % m
    a21 = (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % m
    a22 = (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % m   
    return [[a11, a12], [a21, a22]]

def matrix(A,X):
    res = [[1,0], [0,1]] 
    while X > 0:
        if X % 2 == 1:
            res = mult(res, A)   
        A = mult(A, A)
        X = X//2   
    return res

T = int(input())
for i in range(T):
    a11, a12, a21, a22 = map(int, input().split())
    X = int(input())   
    A = [[a11, a12], [a21, a22]]    
    R = matrix(A,X)
    
    print(R[0][0], R[0][1])
    print(R[1][0], R[1][1])
