# Iterating lists
from random import randint


def getList(mylist: list):
    print(*[value for value in mylist if value[0] in ['a', 'b', 'c']])


def getNums():
    num = [a for a in range(1, randint(5, 1000)) if a % 10 == 0]
    print(num)


if __name__ == "__main__":
    fruits = list(map(str,input('Enter fruits here: ').split(',')))
    getList(fruits)
    # getNums()
