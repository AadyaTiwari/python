import random 
from words import words
from hangman_visual import lives_visual_dict
import string

def generate_word():
    w = random.choice(words)

    while "-" in w or ' ' in w:
        w = random.choice(words)

    return w.upper()

def hangman():
    word = generate_word()
    w_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used = set()

    lives = 7

    while len(w_letters) > 0 and lives > 0:

        print("You have used these letters: ", ' '.join(used), "and", end = " ")
        print("You have", lives, "lives.")

        word_list = [letter if letter in used else "_" for letter in word]

        print("Current Word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used:
            used.add(user_letter)
            if user_letter in w_letters:
                w_letters.remove(user_letter)

            else:
                lives -= 1
                print(lives_visual_dict[lives])
                print(f"{user_letter} is not in the word!")
            
            

        elif user_letter in used:
            print(f"You have already guessed {user_letter}. Please try again.")

        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died! The correct word is:", word)
        
    else: print("you guessed the correct word!!", word)


hangman()