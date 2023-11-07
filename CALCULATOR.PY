print("Welcome to my codsoft internship project task-2 by LAKSHYA AGARWAL")
print("CALCULATOR")
print("Operations to perform:")

print("1. ADDITION")
def add(num1, num2): 
    return num1 + num2

print("2. Subtraction")
def subtract(num1, num2): 
    return num1 - num2

print("3. Multiplication") 
def multiply(num1, num2): 
    return num1 * num2

print("4. Division")
def divide(num1, num2): 
    if num2 == 0:
        return "Division by zero is not allowed."
    return num1 / num2
print("5. Raising a power to number Like 2 sqr 5")
def raisePower(x, y):
    return x ** y

choice = input("Enter choice: ")

if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        result = divide(num1, num2)
        print(num1, "/", num2, "=", result)

    elif choice == '5':
        print (num1, "**", num2, "=", raisePower(num1, num2))

else:
    print("Please select a valid input (1 to 5) for the operation.")
