#Day 12 practice
#scope and guessing game
enemies = 1
def increase_enemies():
    enemies = 2
    print(f"enemies inside function:{enemies}")
    increase_enemies()
    print(f"enemies outside function:{enemies}")
    #local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)
#global scope
player_health = 10
def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)

#there is no block scope
game_level = 3
def create_enemy():
   enemies = ["zombie","alien","skeleton"]
   if game_level < 5:
       new_enemy = enemies[0]

   print(new_enemy)
#modifying global scope
enemies = 1
def increase_enemies():
   # global enemies
    #enemies += 1
   return enemies
print(f"enemies inside function:{enemies}")
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#project
from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! the answer was {answer}.")
def set_difficulty():
    level = input("Choose a difficulty. type 'easy' or 'hard':")
    if level == "easy":
       returns = EASY_LEVEL_TURNS
    else:
       returns = HARD_LEVEL_TURNS
def game():
 print("Welcome to the number guessing game!")
 print("Im thinking of a number between 1 and 100.")
answer  = randint(1,100)
print(f"psst, the correct answer is {answer}")
turns = set_difficulty()
print(f"you have {5} attempts remaining to guess the number")
guess = 0
while guess != answer:
 guess = int(input("Make a guess"))
check_answer(guess, answer)
game()
