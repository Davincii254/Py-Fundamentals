# # For loop to iterate over a range
for i in range(5):
    print(i)


# Nested for loop to create a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()  # Move to the next line after each row


# While loop to print numbers until a condition is met
count = 0
while count < 8:
    print(count)
    count += 1


# For loop with enumerate to iterate over both index and value
fruits = ['apple', 'banana', 'orange']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")


# For loop with zip to iterate over multiple lists simultaneously
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")


# Nested while loop to generate a pattern
row = 1
while row <= 5:
    col = 1
    while col <= row:
        print("*", end=" ")
        col += 1
    print()
    row += 1


# For loop with break and continue statements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        continue  # Skip even numbers
    if num == 7:
        break  # Exit the loop when 7 is encountered
    print(num)

# For loop with an else block that executes when the loop completes without a break
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 6:
        print("Found 6")
        break
else:
    print("6 not found")


# Using list comprehension to create a new list
squares = [x**2 for x in range(1, 6)]
print(squares)


# Nested list comprehension to create a matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)


# Looping through a dictionary using items()
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
for name, grade in student_grades.items():
    print(f"{name}: {grade}")
