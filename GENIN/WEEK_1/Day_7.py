#hangman
word_list = ["ardvark","baboon","camel"]
import random
chosen_word = random.choice(word_list)
guess = input("guess a letter:").lower()
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
print(f'pssst, the solution is {chosen_word}.')
display = []
word_lenght = len(chosen_word)
for _ in range(word_lenght):
    display += "_"

guess = input("guess a letter:")
for position in range (word_lenght):
    letter = chosen_word[position]
    print(f"curren position: {position}\n current letter: {letter}\n guessed letter: {guess}")
    if letter == guess:
        display[position] = letter
        print(display)
import random




