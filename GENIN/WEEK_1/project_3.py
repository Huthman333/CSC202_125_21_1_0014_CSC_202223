print("Welcome to python deliveries!")
size = input("what size pizza do you want? S, M, or L")
add_pepperoni = input("do you want pepperoni? y or n")
extra_cheese = input("do you want extra cheese? y or n")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
if add_pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "y":
    bill += 1
print(f"your final bill is ${bill}")


love calculator
print('Welcome to love calculator!')
name1 = input("what is yoy name?\n")
name2 = input("what is their name?\n")
combined_string = name1 + name2
lower_case_string = combined_string.lower()
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
     print(f"your love score is {love_score}, love is not for you ")
 elif (love_score >= 40) and (love_score <= 50):
     print(f"your score is {love_score},love is for you.")
 else:
     print(f"you score is {love_score}")


    #final project
print("welcome to treasure island.")
print("your mission is to find the treasure.")
choice1 = input('you\'re at a crossroad, where do you want to go? type"left" or "right".').lower()

if choice1 == "left":
    choice2 = input('you\'ve come to a lake.there is an island in the middle of the lake. type "wait" to wait for a boat. '
    'type "swim" to swim across.').lower()
  if choice2 == "wait":
     choice3 = input("you arrive at the island unharmed. there is a house with 3 doors. one red, one yellow and one blue."
    "which colour do you chose.?\n").lower()
  if choice3 == "red":
      print("its a room full of fire. game over.")
     if choice3 == "yellow":
      print("you found the treasure! you win!")
    else:
      print("you chose a door that does not exits. game over.")
  else:
     print("you got attacked by an angry trouts. game over.")
else:
   print("you hell into a hole. game over")
