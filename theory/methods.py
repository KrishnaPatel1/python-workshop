def say_hello():
    print("Hello")
    print()

say_hello()

# Here is a method that calculates the double of a number
def double(number):
  result = number * 2
  return result

result = double(2)
print(result)
print()

# Here is a method that calculates the average of a list of numbers
def average(list_of_numbers):
  total = 0
  number_of_items_in_list = 0
  average = 0

  for number in list_of_numbers:
    number_of_items_in_list = number_of_items_in_list + 1
    total = total + number
  
  average = total/number_of_items_in_list

  return average

a_bunch_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = average(a_bunch_of_numbers)
print(result)
print()

# Challenge 1
# Create a function that takes a number
# it returns the negative of the number
# Note, use print(method) to print out the value
print("Challenge 1:")

# Challenge 2
# Imagine you are given some product that has some cost to it (e.g. $14.99)
# calculate the tax of the product and and it to the cost of the product
# return the total cost of the product
# assume the tax is 15%
# Note, use print() to print out the result of the method
print()
print("Challenge 2:")

# Challenge 3
# Create a method that
# takes in a student's test score and the total amount of points in the test
# returns the result of the student in percentage
print()
print("Challenge 3:")

# Challenge 4
# Create a method that:
# takes in one number
# if even, print the number and state that it is even
# if odd, print the number and state that it is odd
# if less than zero, print the number and state that it is negative
# if the number is a combination of the above conditions, then print both conditions (e.g. -2 is even and negative)
print()
print("Challenge 4:")