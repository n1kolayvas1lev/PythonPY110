if __name__ == "__main__":
    str_ = "1q2w3e4r5t6y"
    chars = filter(str.isalpha, str_)
    #chars = [char for char in str_ if char.isalpha()]  #  переписать с помощью filter

    print("".join(chars))
