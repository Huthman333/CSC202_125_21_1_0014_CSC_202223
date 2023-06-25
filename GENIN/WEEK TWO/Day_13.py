      #Day 13 practics
          #Debugging
       #discribe the problem
def my_function():
     for i in range (1, 21):
          if i == 20:
           print("you got it")
my_function()
# from random import randint
# dice_imgs = ["o","o","o","o"]
# dice_num = randint(1,4)
# print(dice_imgs[dice_num])
         #play computer
year = int(input("what is your year of birth"))
if year > 1980 and year < 1994:
    print("you are a millenial.")
elif year > 1994:
    print("you are a zombie")
age = int(input("how old are you?"))
if age > 18:
    print(f"you can drive at age {age}.")

pages = 0
word_per_page = 0
pages = int(input("number of pages:"))
word_per_page == int(input("number of words per page:"))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_page = {word_per_page}")
print(total_words)
           #odd and even
number = int(input("which number do you want to check?"))
if number %2 == 0:
    print("this is an even number.")
else:
    print("this is an odd number.")
    #project
for number in range(1,101):
    if number %3 == 0 or number %5 == 0:
        print("walex")
    if number %3 == 0:
        print("wal")
    if number %5 == 0:
        print("lex")
    else:
        print(number)
