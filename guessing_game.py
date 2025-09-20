import os
# secret_word
# challenge word variable 

# guess_limit = 3
# Number of available hints

def GuessingSecretWord(secret_word, guess_limit):

    def clear_screen():
                  # Cond for any operating system 
        os.system("cls" if os.name == "nt" else "clear")

    # Clear screen to start with n clean place
    clear_screen()

    # Player guessing word in this variable 
    guess = ""

    # Number of used hints
    guess_count = 0

    # Variable to alert that player is out of hints
    out_of_guesses = False

    # game loop end if win and not win
    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("\n enter the word : \n").lower()
            guess_count += 1
        else:
            out_of_guesses = True
        if not guess == secret_word:
            print(f"\n wrong word, you have {guess_limit - guess_count} attempts left.\n")
    clear_screen()

    # Game over notification 
    if out_of_guesses:
        print("\n you lose out of guesses \n")
    else:
        print("\n you win, congratulations \n")




