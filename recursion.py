# # 
# def countdown(n):
#     if n== 0:
#         print("done")
#         return
#     print(n)
#     countdown(n-1)
# countdown(10)

# # factorial
# def factorial(num):
#     if num < 0:
#         print("Factorial is not defined for negative numbers")
#     else:
#         factorial = 1
#         for i in range(1, num + 1):
#             factorial *= i
#         print(f" factorial of {num} is: {factorial}")

# using recursion:
def factorial(num):
    if num < 0:
        print("Factorial is not defined for negative numbers")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of", num, "is:", factorial(num))