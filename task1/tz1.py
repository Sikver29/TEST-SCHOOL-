n1, m1, n2, m2 = map(int, input().split())

def circular_path(n, m):
    msv = [i + 1 for i in range(n)]
    path = []
    start = 0
    while True:
        temp = [msv[(start + k) % n] for k in range(m)]
        path.append(temp[0])
        start = (start + m - 1) % n
        if start == 0:
            break
    return ''.join(str(x) for x in path)

path1 = circular_path(n1, m1)
path2 = circular_path(n2, m2)

print(path1 + path2)
