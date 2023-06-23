#Day 10
#funtions with inputs
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
   return "you did not provide valid inputs."
   formated_f_name =  f_name.title()
  formated_l_name = l_name.title()
  return  f"Result:{formated_f_name} {formated_l_name}"
print(format_name(input("what is your first name?"),input("what is your last name")))
#formated_string = format_name("AdEWALE","YU")
#print(formated_string)
#Days in Month
def is_leap(year):
    if year %4 == 0:
        if year % 100 == 0:
            if year %400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        print("Not leap year")
def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid"
    month_days = [31, 28,31,30.31,31,30]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]
year = int(input("enter a year:"))
month = int(input("enter a month:"))
days = days_in_month(year, month)
print(days)
#Calculator
def add(n1, n2):
    return n1 + n2
#Subtration
def subtract(n1, n2):
    return n1 - n2
#Multiplication
def multiply(n1, n2):
    return n1 * n2
#Divition
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

}
num1 = int(input("what is the first number?:"))

for symbol in operations:
    print(symbol)
    operation_symbol = input("pick an operation from the line above:")
num2 = int(input("what is the second number?:"))
calculation_function = operations[operation_symbol]
answer = calculation_function[num1, num2]
print(f"{num1} {operation_symbol} {num2} = {answer}")


