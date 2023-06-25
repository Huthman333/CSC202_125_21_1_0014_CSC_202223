#Data types
#String
print("Hello"[0])
print("hello" + "world")

# Integer
print(123 + 345)

# float
# 3.14156
#
# Boolean
#
# True
# False
num_char = len(input("what is your name"))
print(type(num_char))
new_num_char = str(num_char)
print("your name has" + new_num_char + "characters")
two_digit_number = input("type a two didt number")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
two_digit_number = second_digit + first_digit
print(two_digit_number)
print(3 * 3 + 3 / 3 - 3)
# PEMDASLR
height = input("enter your height in m:")
weight = input("enter your weight in kg:")
bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)
print(round(8 / 3,  2))
print(type(8 // 3))
score = 0
height = 1.8
isWinning = True
# f-string
print(f"your score is {score}, your heoght is {height},you are winning is {isWinning}")
print("your score is" + str(score))
age = input("what is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remainig = years_remaining * 52
months_remining = years_remaining * 12
message = f"you have {days_remaining} days, {weeks_remainig} weeks, and {months_remining} month, left."
#print(message)
print("welcome to the tip calculator!")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like tp give? 10, 12, or 15?"))
people = int(input("how many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")