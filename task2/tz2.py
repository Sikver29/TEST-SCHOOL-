import sys

# Чтение данных из файла
def ellipse_data(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()

    except FileNotFoundError:
        print("Error: файл не найден")
        sys.exit(1)
    except OSError:
        print("Error: Не удалось открыть файл")
        sys.exit(1)

    try:
        # Координаты центра
        center = list(map(float, lines[0].strip().split()))
        # Радиусы
        radii = list(map(float, lines[1].strip().split()))

    except ValueError:
        print("Error: файл эллипса должен содержать только числа")
        sys.exit(1)
    if radii[0] <= 0 or radii[1] <= 0:
        print("Error: радиусы должны быть положительными")
        sys.exit(1)

    return center[0], center[1], radii[0], radii[1]

# Чтение координат точек из файла
def read_points(filename):
    points = []
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        coords = list(map(float, line.split()))

                    except ValueError:
                        print("Error: Файл должен содержать только числа")
                        sys.exit(1)

                    points.append((coords[0], coords[1]))
    except OSError:
        print("Error: не удалось открыть файл")
        sys.exit(1)

    return points

# Определение положение точки относительно эллипса
def point_position(x, y, x0, y0, a, b):
    # Формула эллипса:
    result = ((x - x0) ** 2 / a ** 2) + ((y - y0) ** 2 / b ** 2)

    if abs(result - 1.0) < 1e-9:
        return 0  # На эллипсе
    if result < 1.0:
        return 1  # Внутри
    else:
        return 2  # Снаружи

def main():
    if len(sys.argv) != 3:
        print("Error: Укажите 2 файла: <ellipse.txt> <points.txt>")
        sys.exit(1)

    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    x0, y0, a, b = ellipse_data(ellipse_file)
    points = read_points(points_file)

    for x, y in points:
        print(point_position(x, y, x0, y0, a, b))

if __name__ == "__main__":
    main()
