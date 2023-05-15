#Printing a multiplication Table
from random import randint


def GetTable(num):
    for a in range(1,num):
        for b in range(1,num):
            print(a*b, end= "\t")

        print()

    return



if __name__ == "__main__":
    mx = randint(5,30)
    GetTable(mx)
