from itertools import count
def pow_gen(base: int):
    pow_ = 0
    yield pow(base, pow_)
    #base = (base ** i for i in count(1, 1))

    for i in count(1, 1):
        yield base ** i
    # yield (base ** i for i in count(1, 1))  #  записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
