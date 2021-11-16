def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]
    # for i in list_words:
    #     print(len(i))
    return max(len(i) for i in list_words)
    #  записать выражение-генератор


if __name__ == "__main__":
    print(task())
