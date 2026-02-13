n = int(input())

def convert_name(name):
    result = []
    for c in name:
        if 'a' <= c <= 'z':
            result.append(chr(ord(c) - ord('a') + ord('A')))
        else:
            result.append(chr(ord(c) - ord('A') + ord('a') + 26))
    return "".join(result)

trains = []

for i in range(n):
    line = input()
    parts = line.split()
    name = parts[0]
    time = parts[-1]
    h, m = time.split(":")
    minutes = int(h)*60+int(m)
    trains.append((convert_name(name), -minutes, i, line))

trains.sort()

for train in trains:
    print(train[3])
