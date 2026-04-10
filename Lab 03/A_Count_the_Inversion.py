def merge(left,right) :
    i = 0
    j = 0 
    merged =[]
    inv_count = 0
    while i<len(left) and j<len(right) :
        if left[i]<=right[j] :
            merged.append(left[i])
            i+= 1
        else :
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    while i<len(left) :
        merged.append(left[i])
        i += 1
    while j<len(right) :
        merged.append(right[j])
        j += 1

    return merged, inv_count

def mergeSort(arr):
    if len(arr)<=1:
        return arr, 0   
    mid = len(arr) // 2
    left, inv_left = mergeSort(arr[:mid])
    right, inv_right = mergeSort(arr[mid:])
    merged, inv_merge = merge(left, right)
    
    return merged, inv_left + inv_right + inv_merge

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

sorted_arr, inversion_count = mergeSort(arr)

print(inversion_count)
print(*sorted_arr)
