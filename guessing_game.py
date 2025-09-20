import os

def clear_screen():
              # Cond for eny operating system 
    os.system("cls" if os.name == "nt" else
"clear")

# Clear screen to start with n clean place
clear_screen()

# The challenge word
secret_word = "hello"

# Player guessing word in this variable 
guess = ""

# Number of used hints
guess_count = 0

# Number of available hints
guess_limit = 3

# Variable alarm you that player is finished hints
out_of_guesses = False

# game loop end if win and not win
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("\n enter the word : \n")
        guess_count += 1
    else:
        out_of_guesses = True
    if not guess == secret_word:
        print("\n wrong word, try again \n")
clear_screen()

# game over notification 
if out_of_guesses:
    print("\n you lose out of guesses \n")
else:
    print("\n you win, congratulations \n")




