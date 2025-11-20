import sys

# Чтение чисел
def read_numbers_from_file(filepath):
    numbers = []
    try:
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        print("Error: Файл должен содержать целые числа")
                        sys.exit(1)

    except FileNotFoundError:
        print("Error: файл не найден")
        sys.exit(1)
    except OSError:
        print("Error: не удалось открыть файл")
        sys.exit(1)

    return numbers

# Минимальное количество ходов
def calculate_min_moves(nums):
    if not nums:
        return 0

    # Сортировка
    sorted_nums = sorted(nums)
    n = len(sorted_nums)

    # Медиана
    if n % 2 == 1:
        median = sorted_nums[n // 2]
    else:
        median = sorted_nums[n // 2 - 1]

    # Сумма Растояния до медианы
    moves = 0
    for num in nums:
        moves += abs(num - median)

    return moves


def main():
    if len(sys.argv) != 2:
        print("Error: неверное количество аргументов")
        sys.exit(1)

    input_file = sys.argv[1]
    max_moves = 20

    nums = read_numbers_from_file(input_file)
    min_moves = calculate_min_moves(nums)

    if min_moves <= max_moves:
        print(min_moves)
    else:
        print(f"{max_moves} ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()
