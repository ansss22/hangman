#Step 1 
import random
from hangman_art import stages
from hangman_art import logo
from  hangman_words import word_list
from replit import clear

lives = 6 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

print(f'Pssst, the solution is {chosen_word}.')
display = []
for _ in range(len(chosen_word)):
    display += "_"

print(display)

end_of_game = False
while not end_of_game:
    guess = input("Please enter a letter :   ").lower()
    clear()
    if guess in display:
        print(f"You've already guessed a {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter


    if guess not in chosen_word:  
        print(f"You guessed {guess}, That's not in the word . You lose a life!")  
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])
 

