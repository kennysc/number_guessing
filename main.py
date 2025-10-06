import os
from random import randint

def isnumber(message):
    valid  = False
    while not valid:
        try:
            number = int(input(message))
            valid = True
        except KeyboardInterrupt:
            print("")
            print("Exiting...")
            quit()
        except:
            print("Not a valid number, try again")
    return number

def small_big(guesses, target):
    smaller_list = []
    bigger_list = []
    for guess in guesses:
        if guess < target:
            smaller_list.append(guess)
        else:
            bigger_list.append(guess)
    return smaller_list, bigger_list

def main():
    lower_number = isnumber("Enter the low number: ")
    higher_number = isnumber("Enter the high number: ")

    while higher_number <= lower_number:
        print("The high number must be higher than the low number...")
        higher_number = isnumber("Enter the high number: ")

    random_number = randint(lower_number, higher_number)
    number_of_guesses = 7
    guess_count = 0
    guesses = []

    while guess_count < number_of_guesses:
        os.system('cls' if os.name == 'nt' else 'clear')
        smaller, bigger = small_big(guesses, random_number)

        print(f"You have {number_of_guesses - guess_count} guesses left!")
        print(f"Smaller: {', '.join(map(str, sorted(smaller)))}")
        print(f"Bigger: {', '.join(map(str, sorted(bigger)))}")
        guess = isnumber(f"Guess un number between {lower_number} and {higher_number}: ")
        guesses.append(guess)
        if guess == random_number:
            print("Success! You found the random number!")
            break
        if guess < random_number:
            print("Too Low")
        if guess > random_number:
            print("Too high")
        guess_count += 1

if __name__ == "__main__":
    main()
