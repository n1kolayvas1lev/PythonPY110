import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_data = json.load(f)

    return    #  отсортировать список словарей


if __name__ == "__main__":
    data = task()
    print(json.dumps(data, indent=4))

    #  дополнительно записать отсортированный список в JSON файл
