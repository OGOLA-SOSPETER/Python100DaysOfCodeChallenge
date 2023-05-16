#list elements
from random import randint


def printList():
    my_list = list(map(int, input().split(",")))
    print(*my_list)


def printFizbuz():
    for num in range(1,100):
        temp = ""
        if num % 3 == 0:
            temp += "Fizz"
        if num % 5 == 0:
            temp += "Buzz"
        else:
            print(temp or num)


if __name__ == "__main__":
    # printList()
    printFizbuz()

