def task(words: list) -> list:
    return list(map(str.upper, words))
    #return [word.upper() for word in words]  #  перевести слова в верхний регистр c помощью map


if __name__ == "__main__":
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    print(task(list_words))
