import json


def task():
    filename = "input.json"
    with open(filename) as inp_:
        inp = json.load(inp_)

    #  считать содержимое JSON файла

    return max(inp, key=lambda dict_: dict_['score']) #dict_.get('score')   #  найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
