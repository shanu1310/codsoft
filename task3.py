def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (1, 2, 3, or 4): ")

# Perform calculation based on user input
if operation == '1':
    result = add(num1, num2)
elif operation == '2':
    result = subtract(num1, num2)
elif operation == '3':
    result = multiply(num1, num2)
elif operation == '4':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

# Display the result
print("Result: ", result)
