import sys
import json

#загрузка json из файла
def load_json(filepath):
    try:
        with open(filepath) as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: файл не найден")
        sys.exit(1)
    except OSError:
        print("Error: не удалось открыть файл")
        sys.exit(1)

#сохранение данных в json
def save_json(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    except OSError:
        print("Ошибка: не удалось записать файл")
        sys.exit(1)

#Поиск по Id
def create_values_dict(values_data):
    values_dict = {}

    if "values" in values_data:
        for item in values_data["values"]:
            test_id = item["id"]
            test_value = item["value"]

            if test_value == test_id:
                print(f"Error: в values.json значение value совпадает с id ({test_id})")
                print("Ожидается что 'value' хранит результат теста а не номер")
                sys.exit(1)

            values_dict[test_id] = test_value
    return values_dict

# Заполнение value
def fill_tests(tests_list, values_dict):
    for test in tests_list:
        # value по id
        if "id" in test:
            test_id = test["id"]
            if test_id in values_dict:
                test["value"] = values_dict[test_id]

        if "values" in test:
            fill_tests(test["values"], values_dict)

def main():
    if len(sys.argv) != 4:
        print("Error: неверное количество аргументов")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    if "values" not in values_data:
        print("Error: первый файл должен быть values.json")
        sys.exit(1)

    if "tests" not in tests_data:
        print("Error: второй файл должен быть tests.json")
        sys.exit(1)

    #Словарь
    values_dict = create_values_dict(values_data)

    # Заполнение tests
    if "tests" in tests_data:
        fill_tests(tests_data["tests"], values_dict)

    save_json(report_file, tests_data)

if __name__ == "__main__":
    main()
