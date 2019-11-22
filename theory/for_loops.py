# Scenario: print all numbers in the following list
numbers = [55, 33, 12, 678, 93, 11, 4]
for number in numbers:
  print(number)

# Scenario: double the value of all the numbers in the following list
numbers = [55, 33, 12, 678, 93, 11, 4]
for number in numbers:
  number = number * 2
  print(number)

# Challenge 1
# Compute the total amount of times the number 4 appears
print()
print("Challenge 1:")
list_of_numbers = [3, 4, 7, 23, 12, 4, 4, 2, 10, 4]

# Challenge 2
# Compute the average of the list from challenge 1
print()
print("Challenge 2:")



#######################################################################################
######WE SHALL COME BACK TO THIS AFTER COVERING THE METHODS SECTION OF THE THEORY######
#######################################################################################

for number in numbers:
  print("Current number is:", number)
  number = number * 2
  print("Current number times two is:", number)

print()

# Scenario: print all numbers between 1 and 9
for number in range(1, 10):
  print(number)
  
print()

# Declare initial variables to 0
average = 0
total = 0
amount_of_numbers_in_range = 0

# Iterate through the loop, 1 to 9
print("First for-loop")
for number in range(1, 10):
  # Add one everytime we run the loop
  amount_of_numbers_in_range = amount_of_numbers_in_range + 1
  # Add number to total every time the for loop runs
  total = total + number

# Compute the average
average = total/amount_of_numbers_in_range

# Print values
print("There are " + str(amount_of_numbers_in_range) + " numbers in the range")
print("The sum of all numbers is:  " + str(total))
print("The average is: " + str(average))
print()

# Reset values
average = 0
total = 0
amount_of_numbers_in_range = 0

# Second loop, ranging to 11 in order to include 10 (so 1 - 10)
print("Second for-loop")
for number in range(1, 11):
  # Add one everytime we run the loop
  amount_of_numbers_in_range = amount_of_numbers_in_range + 1
  # Add number to total every time the for loop runs
  total = total + number

# Compute the average
average = total/amount_of_numbers_in_range

# Print values
print("There are " + str(amount_of_numbers_in_range) + " numbers in the range")
print("The sum of all numbers is:  " + str(total))
print("The average is: " + str(average))
