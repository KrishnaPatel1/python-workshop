# Scenario: print all numbers between 1 and 100

# Declare initial variables to 0
average = 0
total = 0
amountOfNumbersInRange = 0

# Iterate through the loop, 1 to 99
print("First for loop")
for number in range(1, 10):
  # Add one everytime we run the loop
  amountOfNumbersInRange = amountOfNumbersInRange + 1
  # Add number to total every time the for loop runs
  total = total + number

# Compute the average
average = total/amountOfNumbersInRange

# Print values
print("There are " + str(amountOfNumbersInRange) + " numbers in the range")
print("The sum of all numbers is:  " + str(total))
print("The average is: " + str(average))

# Reset values
average = 0
total = 0
amountOfNumbersInRange = 0

# Second loop, ranging to 101 in order to include 100 (so 1 - 100)
print("Second for loop")
for number in range(1, 11):
  # Add one everytime we run the loop
  amountOfNumbersInRange = amountOfNumbersInRange + 1
  # Add number to total every time the for loop runs
  total = total + number

# Compute the average
average = total/amountOfNumbersInRange

# Print values
print("There are " + str(amountOfNumbersInRange) + " numbers in the range")
print("The sum of all numbers is:  " + str(total))
print("The average is: " + str(average))

# Challenge 1
# Compute the total amount of times 4 appears
list_of_numbers = [3, 4, 7, 23, 12, 4, 4, 2, 10, 4]

print("Challenge 1:")

# Challenge 2
# Find its respective percentage

print("Challenge 2:")

