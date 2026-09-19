def addition(a, b):
    return a + b
def subtraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b

while True:
    print("--- Calculator Menu ---")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("exit : Exit")

    choice = input("Enter your choice from the menu: ")

    if choice == "exit":
        break

    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    if choice == "+":
        print("Addition: ", addition(num1, num2))
    elif choice == "-":
        print("Subtraction: ", subtraction(num1, num2))
    elif choice == "*":
        print("Multiplication: ", multiplication(num1, num2))
    elif choice == "/":
        print("Division: ", division(num1, num2))
    else:
        print("Invalid Choice")