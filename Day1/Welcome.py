#Welcome to the #100DaysOfPythonLoopsChallenge
from random import randint
import sys


def Welcome():
    name = sys.stdout
    
    for a in range(1, randint(1,100)):
        print(a, name)


if __name__ == "__main__":
    Welcome()
