import sys

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

def main():
    if len(sys.argv) != 5:
        print("Error: Передайте 4 аргумента")
        sys.exit(1)

    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:])

    except ValueError:
        print("Error: Аргументы должны быть целыми числами")
        sys.exit(1)

    if n1 <= 0 or m1 <= 0:
        print("Error: n и m для массива 1 должны быть положительными числами")
        sys.exit(1)

    if m1 > n1:
        print("Error: m не может быть больше n (массив 1)")
        sys.exit(1)

    if n2 <= 0 or m2 <= 0:
        print("Error: n и m для массива 2 должны быть положительными числами")
        sys.exit(1)

    if m2 > n2:
        print("Error: m не может быть больше n (массив 2)")
        sys.exit(1)

    path1 = circular_path(n1, m1)
    path2 = circular_path(n2, m2)
    print(path1 + path2)

if __name__ == "__main__":
    main()
