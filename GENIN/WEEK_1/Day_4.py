#Day 4
#randomisation aand python list
test_seed = int(input("create a seed number:"))
import random
random_side = random.randint(0, 1)
if random_side == 1:
 print("heads")
else:
 print("tails")

#python list
user_choice = input("what do you choose? type 0 for rock, 1 for paper or 2 for scissors\n")
computer_choice = random.randint(0 , 2)
print(f"computer chose {computer_choice}")
if user_choice == 0 and computer_choice == 2:
    print("user wins!")
elif user_choice == computer_choice:
    print("you win!")
elif computer_choice == user_choice:
    print("it is a draw !")
else:
    print("you have typed invalid no, you lose!")


