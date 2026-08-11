def add(a, b):
    return (a + b)

def subtract(a, b):
    return (a - b)

def multiply(a, b):
    return (a * b)

def divide(a, b):
    try:
        return (a / b)
    except:
        return "Something went wrong"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add/subtract/multiply/divide): ")

if operation == "add":
    print(add(num1, num2))
elif operation == "subtract":
    print(subtract(num1, num2))
elif operation == "multiply":
    print(multiply(num1, num2))
elif operation == "divide":
    print(divide(num1, num2))
else:
    print("Invalid operation")

