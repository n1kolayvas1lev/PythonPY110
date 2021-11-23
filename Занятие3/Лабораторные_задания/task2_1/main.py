import json


def task() -> str:
    dict_numbers = {n: n ** 2 for n in range(1, 11)}  #  c помощью dict comprehension сформировать словарь
    return json.dumps(dict_numbers, indent=4)   #  сериализовать словарь в JSON строку


if __name__ == "__main__":
    print(task())
