# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Ask for operation
print("\nChoose operation: +, -, *, /")
op = input("Enter operation: ")

# Perform calculation
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operation"

# Show result
print("\nResult:", result)