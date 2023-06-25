#Day 3
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("what is your age?"))
    if age<= 18:
        bill = 12
        print("youth tickets are $7")
    elif age <= 12:
        bill = 7
        print("child tickets are $12")
    else:
        print("adult tickets are $23")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is {bill}")

else:
    print("sorry, you have to grow taller before you van ride.")
    #comparison operators
#>,<,>=,<=,==,!=
# day 3.1 odd and even exercise

number = int(input("which number do you want to choose? "))
if number %2 == 0:
    print("this is a even number")
else:
    print("this is an odd number.")

height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"your bmi is {bmi}, you have underweight.")
elif bmi < 25:
    print(f'your bmi is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f"your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"your bmi is {bmi},you are obese.")
else:
    print(f"your bmi is {bmi}, you are clinically obese.")
 #day 3.3
year = int(input("which year do you want to check?"))
if year %4 == 0:
    if year %100 == 0:
        if year %400 == 0:
            print("leap year")
        else:
            print("not leap year.")
    else:
        print("leap year.")
else:
    print("not leap year")

#love_calculator
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
elif(love_score >= 40) and (love_score <= 50):
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