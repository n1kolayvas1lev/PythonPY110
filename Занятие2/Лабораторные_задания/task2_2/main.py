def count(start_number: float = 1, step: float = 1):
    yield start_number
    while True:
        start_number += step
        yield start_number

#    #  написать функцию-генератор возвращающую целые числа


if __name__ == "__main__":
    my_count = count(10, 0.5)
    for _ in range(10):
        print(next(my_count))
