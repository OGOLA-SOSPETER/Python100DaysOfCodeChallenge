 #A reminder on the random module
import random
#creating a class to handle the random functioning

class Guesses:
    @staticmethod
    def get_random():
        attempts = eval(input('Enter the number of times you want to attempt the game: '))
        counter = attempts
        for a in range(0,attempts):
            print('\n','-'*30)
            number = eval(input("Enter your Guess.\n"))
            counter = counter - 1
            guess = random.randint(1, 1000)
            if number == guess:
                print("Your Guess is right!"
                      "\nYou won!")
                break

            else:
                print("Wrong Guess!\n"
                      "System won!")
                print('The correct answer is ', guess)
                print('-' * 30)

        new_count = counter
        print('-' * 30,end="\n")
        if new_count > 1:
            print("You guessed right at the count of {:2d} / {:2d}".format(new_count,attempts))
        else:
            print("Failed!")
        print('Your percentage pass = {:.4f}'.format(new_count / attempts * 100), '%')
        print('-' * 30)
        print('-' * 30)

Ges1 = Guesses
Ges1.get_random()
