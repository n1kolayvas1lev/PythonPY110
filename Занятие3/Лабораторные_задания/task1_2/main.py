OUTPUT_FILE = "output.txt"


def task():
    #  записать лесенку в файл
    with open(OUTPUT_FILE, 'w') as f:
        for i in range(1, 11):
            f.write(' ' * (10 - i) + '*' * i + '\n')  #  f"{'*' * i:>10}"

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
