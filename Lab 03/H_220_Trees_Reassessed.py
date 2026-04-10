import sys
input = sys.stdin.readline
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

def pre(inL, inR, postL, postR):
    if inL > inR:
        return   
    root = postorder[postR]
    print(root, end=' ')   
    i = inL
    while i<=inR and inorder[i] != root:
        i += 1    
    leftSize = i-inL    
    pre(inL, i-1, postL, postL+leftSize-1)
    pre(i+1, inR, postL+leftSize, postR-1)

pre(0, n-1, 0, n-1)
