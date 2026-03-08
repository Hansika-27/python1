#Python program to create calculator

#step1: create functions
# #function to add two number 
def add(num1, num2):
    return num1 + num2

#function to subtract two number
def  sub(num1, num2):
    return num1 - num2

#function to multiply two number
def mul(num1, num2):
    return num1 * num2

#function to divide two number
def div(num1, num2):
    return num1 / num2

#function to avg two number
def avg(num1, num2):
    return (num1 + num2) / 2


#step2: take user input
print("please select a operation :\n " \
      "1. Addition\n" \
      "2. Subtraction\n"\
      "3. Multiplication\n"\
      "4. Division\n" \
      "5. Average\n")

select = int(input("Select a operation from 1, 2, 3, 4, 5 : "))
number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))


#step3:  print the result
if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif select == 2:
    print(number1, "-", number2, "=", sub(number1, number2))

elif select == 3:
    print(number1, "*", number2, "=", mul(number1, number2))

elif select == 4:
    print(number1, "/", number2, "=", div(number1, number2))

elif select == 5:
    print("Average of", number1, "and", number2, "is", avg(number1, number2))

else:
    print("Invalid operation! pls select again!")







