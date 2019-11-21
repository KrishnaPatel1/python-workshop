# Scenario: print all numbers between 1 and 100

# Declare initial variables to 0
average = 0
total = 0
amountOfNumbersInRange = 0

# Iterate through the loop, 1 to 99
print("First for loop")
for number in range(1, 100):
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
for number in range(1, 101):
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
