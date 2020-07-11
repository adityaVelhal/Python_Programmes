import random


def play_hungman():
    name = input("Your name: ")
    attempts = 5
    
    print("Hello " + name + ", Get ready to play hungman.\nIn this game a word is randomaly selected " + 
    "and you were asked to guess single character of it." + "\nYou have 5 attempts to guess it right.")

    word = ['game', 'rocket', 'machine', 'dirt', 'python', 'tiger']
    i = random.randint(0, len(word))
    selected_word = word[i]

    while attempts > 0:
        attempts -= 1

        char = input("Enter one character : ")
        char = char.lower()

        if char in selected_word:
            print(char)
            print("You won!!... The Actual word is "+ selected_word)
            
            response = int(input("Press 1 to play again or 0 to end : "))
            if response == 1:
                play_hungman()
            
            break
        else:
            print("_")
            print("You have " + str(attempts) + " attempts left")
    else:
        response = int(input("Press 1 to play again or 0 to end : "))
        if response == 1:
            play_hungman()    
    

if __name__ == "__main__":
    play_hungman()