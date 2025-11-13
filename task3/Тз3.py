import sys
import json

#загрузка json из файла
def load_json(filepath):
    with open(filepath) as f:
        return json.load(f)

#сохранение данных в json
def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

#Поиск по Id
def create_values_dict(values_data):
    values_dict = {}

    if "values" in values_data:
        for item in values_data["values"]:
            test_id = item["id"]
            test_value = item["value"]
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
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)

    #Словарь
    values_dict = create_values_dict(values_data)

    # Заполнение tests
    if "tests" in tests_data:
        fill_tests(tests_data["tests"], values_dict)

    save_json(report_file, tests_data)


if __name__ == "__main__":
    main()
