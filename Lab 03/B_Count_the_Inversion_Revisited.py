import sys
input = sys.stdin.readline

def count_less(arr,x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

def merge_count(a,l,r):
    if l >= r:
        return 0    
    m = (l + r) // 2
    cnt = 0  
    cnt += merge_count(a,l,m)
    cnt += merge_count(a,m+1,r)
    right_sq = []
    i = m + 1
    while i <= r:
        right_sq.append(a[i]*a[i])
        i += 1
    right_sq.sort()
    i = l
    while i <= m:
        cnt += count_less(right_sq,a[i])
        i += 1   
    temp = []
    i = l
    j = m + 1   
    while i <= m and j <= r:
        if a[i] <= a[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(a[j])
            j += 1   
    while i <= m:
        temp.append(a[i])
        i += 1   
    while j <= r:
        temp.append(a[j])
        j += 1   
    k = 0
    while k < len(temp):
        a[l + k] = temp[k]
        k += 1    
    return cnt


n = int(input())
arr = list(map(int, input().split()))
print(merge_count(arr, 0, n-1))
