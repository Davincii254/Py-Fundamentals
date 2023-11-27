# A simple function that adds two numbers
def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

result = add_numbers(3, 7)
print(result)


# Function with a default parameter
def greet(name="Guest"):
    """
    Greets a person by name (default is "Guest").
    """
    print("Hello, " + name + "!")

greet()  # Uses the default parameter
greet("Alice")  # Uses the provided parameter



# Function with variable number of arguments using *args
def print_arguments(*args):
    """
    Prints all the arguments passed to the function.
    """
    for arg in args:
        print(arg)

print_arguments(1, 'hello', 3.14, [4, 5])


# Lambda function to square a number
square = lambda x: x ** 2
result = square(5)
print(result)


# Recursive function to calculate factorial
def factorial(n):
    """
    Calculates the factorial of a number using recursion.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
