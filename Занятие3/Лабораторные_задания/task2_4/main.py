import json


def task():
    filename = "input.json"
    with open(filename) as inp_:
        inp = json.load(inp_)
    #  считать содержимое JSON файла

    gen_exr = (dict_.get("contains_improvement_appeals") for dict_ in inp) #  записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
