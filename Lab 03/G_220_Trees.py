import sys
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))

def post(l,r,p):
    if l > r:
        return p   
    root = preorder[p]
    p += 1   
    i = l
    while i< r and inorder[i] != root:
        i += 1   
    p = post(l,i-1,p)
    p = post(i+1,r,p)   
    print(root, end=' ')
    return p

post(0,n-1,0)
