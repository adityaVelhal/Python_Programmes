import random


def play():
    guess_used = 0
    name = input("Your Name : ")
    number = random.randint(1, 5)
    print(number)
    print('\nHello ' + name + ', Welcome to number guessing game...😁😁')
    print('\nI am guessing no. between 1 to 5...')
    print('\nYou have 5 attempts to guess it right!')

    while guess_used < 5:
        guess_used += 1
        guess_no = int(input("\nWhat's your guess: "))
        if number == guess_no:
            print('\nGreat! You guessed it right.')
            print("Better luck next time.\n")
            response = int(input("Press 1 to play again or 0 to end : "))
            if response == 1:
                play()
            else:
                break
        else:
            print("\nWrong! You have "+ str(5 - guess_used) + " attempts remaining.")
    else:
        print("Better luck next time.\n")
        response = int(input("Press 1 to play again or 0 to end."))
        if response == 1:
            play()

if __name__ == "__main__":
    play()