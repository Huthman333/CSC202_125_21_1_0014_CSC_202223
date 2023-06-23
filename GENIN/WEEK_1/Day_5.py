#python loop
import random

fruits = ["apple", "peach", "pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "pie")
    print(fruits)
student_scores = input("input a list of student scores")
for n in range(0, len(student_scores)):
    print(student_scores)
student_scores = [78, 65, 89, 55, 91, 64, 89]
heigest_score = 0
for score in student_scores:
    if score > heigest_score:
        heigest_score = score
print(f"the highest score in the class is: {heigest_score}")
#password generator
letters = ['a','d','f','u','p']
numbers = ['0','1','2','3','4','5']
symbols = ['!','@','#','%']
print("welcome to the pypassword generator! ")
nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"how many numbers would you like?\n"))
for char in range(1, nr_letters + 1):
    password_list = []
    password_list += random.choice(letters)
for char in range (1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range (1, nr_numbers + 1):
    password_list += random.choice(numbers)
    print(password_list)


