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

print(add(5, 3))
print(divide(10, 0))