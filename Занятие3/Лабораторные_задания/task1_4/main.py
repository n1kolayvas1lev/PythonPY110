INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'rt') as in_:
        inp_ = list(map(str.upper, in_))
    with open(OUTPUT_FILE, 'w') as out_:
        for _ in inp_:
            out_.write(_)
    #  перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
