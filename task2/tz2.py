import sys

#чтение данных из файла
def ellipse_data(filename):
    with open(filename) as f:
        lines = f.readlines()
        # Координаты центра
        center = list(map(float, lines[0].strip().split()))
        # Радиусы
        radii = list(map(float, lines[1].strip().split()))
    return center[0], center[1], radii[0], radii[1]

#Чтение координат точек из файла
def read_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                coords = list(map(float, line.split()))
                points.append((coords[0], coords[1]))
    return points

#Определение положение точки относительно эллипса
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
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]

    x0, y0, a, b = ellipse_data(ellipse_file)
    points = read_points(points_file)

    for x, y in points:
        print(point_position(x, y, x0, y0, a, b))


if __name__ == "__main__":
    main()
