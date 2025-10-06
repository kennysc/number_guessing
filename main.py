import os
from random import randint

def isnumber(message):
    while True:
        try:
            number = int(input(message))
            return number
        except KeyboardInterrupt:
            print("\nExiting...")
            quit()
        except:
            print("Not a valid number, try again")

def guesswithinlimits(higher_number, lower_number):
    while True:
        number = isnumber(f"Guess a number between {lower_number} and {higher_number}: ")
        if lower_number <= number <= higher_number:
            return number
        else:
            print(f"{number} is not between {lower_number} and {higher_number}")

def main():
    lower_number = isnumber("Enter the low number: ")
    higher_number = isnumber("Enter the high number: ")

    while higher_number <= lower_number:
        print("The high number must be higher than the low number...")
        higher_number = isnumber("Enter the high number: ")

    random_number = randint(lower_number, higher_number)
    number_of_guesses = 10
    guess_count = 0
    too_low = False
    current_guess = None


    while guess_count < number_of_guesses:
        os.system('cls' if os.name == 'nt' else 'clear')
        if too_low:
            print(f"{current_guess} was too low")
        elif not too_low and guess_count != 0:
            print(f"{current_guess} was too high")

        print(f"You have {number_of_guesses - guess_count} guesses left!")
        #guess = isnumber(f"Guess un number between {lower_number} and {higher_number}: ")
        guess = guesswithinlimits(higher_number, lower_number)

        if guess == random_number:
            print("Success! You found the random number!")
            quit()
        if guess < random_number:
            print("too low")
            too_low = True
            current_guess = guess
            lower_number = guess + 1
        if guess > random_number:
            too_low = False
            current_guess = guess
            higher_number = guess - 1
        guess_count += 1

    print("Game over, better luck next time!")

if __name__ == "__main__":
    main()
