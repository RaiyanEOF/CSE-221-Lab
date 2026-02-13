def get_sorted_students(ids, marks):
    students = []
    for i in range(len(ids)):
        students.append((ids[i], marks[i]))
    n = len(students)
    for i in range(n):
        for j in range(0, n - i - 1):
            id1, mark1 = students[j]
            id2, mark2 = students[j + 1]
            if (mark1 < mark2) or (mark1 == mark2 and id1 > id2):
                students[j], students[j + 1] = students[j + 1], students[j]
    return students


def minimum_swaps(original, sorted_list):
    visited = [False] * len(original)
    swaps = 0
    for i in range(len(original)):
        if visited[i] or original[i] == sorted_list[i]:
            continue
        cycle = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = sorted_list.index(original[j])
            cycle += 1
        swaps += cycle - 1
    return swaps



t = int(input())

for i in range(t):
    n = int(input())
    ids = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    org = []
    for i in range(n):
        org.append((ids[i], marks[i]))
    sorted = get_sorted_students(ids,marks)
    swaps = minimum_swaps(org,sorted)
    print(f"Minimum swaps: {swaps}")
    for sid, mark in sorted:
        print(f"ID: {sid} Mark: {mark}")
