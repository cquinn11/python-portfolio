#simple calculator
#function
#adds num1 + num 2 and prints results
def add (num1, num2):
    result = num1 + num2
    print("The result is: " + str(result))
def subtract (num1, num2):
    result = num1 - num2
    print("The result is: " + str(result))
def multiply (num1, num2):
    result = num1 * num2
    print("The result is: " + str(result))
def divide (num1, num2):
    result = num1 / num2
    print("The result is: " + str(result))
def simplecalc():
    print("Welcome Preschoolers to Simple Calculator")
    while True:
        print("Please choose an operation: ")
        print("""1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Quit""")
        operation = int(input("(1-5) :"))

        if operation == 1:
            add1 = int(input("Enter the first number you would like to add: "))
            add2 = int(input("Enter the second number you would like to add: "))
            add(add1,add2)
        if operation == 2:
            subtract1 = int(input("Enter the first number you would like to subtract: "))
            subtract2 = int(input("Enter the second number you would like to subtract: "))
            subtract(subtract1,subtract2)
        if operation == 3:
            multiply1 = int(input("Enter the first number you would like to multiply: "))
            multiply2 = int(input("Enter the second number you would like to multiply: "))
            multiply(multiply1,multiply2)
        if operation == 4:
            divide1 = int(input("Enter the first number you would like to divide: "))
            divide2 = int(input("Enter the second number you would like to divide: "))
            divide(divide1,divide2)
        if operation == 5:
            print("Thank you for using the simple calculator!")
            break
#main
simplecalc()
