# Initialize the factorial result to 1
factorial = 1

# Initialize the input number to 6
number = 5

# Loop from 1 to number (inclusive) and multiply factorial by each number
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}")
