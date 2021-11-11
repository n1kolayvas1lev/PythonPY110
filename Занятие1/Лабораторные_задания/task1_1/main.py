def task() -> list:
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,  # шестнадцатеричное представление
        0b1010101010  # бинарное представление представление
    ]

    #[int(value) for value in num_list]
    return list(map(int, num_list))


#def map_(func, iterable):
#    for value in iterable:
#        func(value)


if __name__ == "__main__":
    print(task())
