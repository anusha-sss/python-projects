def division(a, b):
    return a / b


def multiplication(a, b):
    return a * b


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


print("Basic operations performed:")
print("1.Division")
print("2.Multiplication")
print("3.Addition")
print("4.Subtraction")

choice = int(input("Choose the operation from 1,2,3,4:"))

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if choice == 1:
    print(num1, "/", num2, "=", division(num1, num2))
elif choice == 2:
    print(num1, "*", num2, "=", multiplication(num1, num2))
elif choice == 3:
    print(num1, "+", "=", addition(num1, num2))
elif choice == 4:
    print(num1, "-", num2, "=", subtraction(num1, num2))
else:
    print("Invalid choice")

