print("Hello, this is a simple calculator.")

firstNumber = input("Please enter you first number here ")

secondNumber = input("Please enter you second number here ")

operator = input("Please choose an operator and enter here ")

if operator == "+":
    print(int(firstNumber) + int(secondNumber))
elif operator == "-":
    print(int(firstNumber) - int(secondNumber))
elif operator == "*":
    print(int(firstNumber) * int(secondNumber))
elif operator == "/":
    print(int(firstNumber) / int(secondNumber))
else:
    print("This is not an option. Please choose +, -, *, or /.")

print("Happy calculating!")