#Program to check if the input is a single character.

def IsSingle(mword):
    if len(mword) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        get_word = input('Enter the letter.')
        if IsSingle(get_word):
            print("The valid character is ", get_word)

        else:
            print('Invalid Characters!!')

