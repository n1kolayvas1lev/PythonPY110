def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    # a = []
    # for i in list_words:
    #     x = len(i)
    #     a.append(x)
    return max(list(map(len, list_words)))   #  найти длину самого длинного слова


if __name__ == "__main__":
    print(task())
