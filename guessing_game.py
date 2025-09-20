import os

def clear_screen():
    os.system("cls" if os.name == "nt" else
"clear")

clear_screen()
secret_word = "skinet"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("\nenter the word : \n")
        guess_count += 1
    else:
        out_of_guesses = True
    if not guess == secret_word:
        print("\nwrong word, try again \n")
clear_screen()
if out_of_guesses:
    print("\nyou lose out of guesses \n")
else:
    print("\nyou win, congratulations \n")



