# Remember that the last number is not considered, therefore, we finish at 10
for rowNumber in range(1,11):
  print("First loop, row number: " + str(rowNumber))
  for columnNumber in range(1,6):
    print("Second loop, column number: " + str(columnNumber))

list_of_numbers = [1,2,3,4,5]

# How to go through elements inside a list
for i in range(len(list_of_numbers)):
  print("Loop ran " + str(i) + " time(s)")
  print(list_of_numbers[i])

list_of_numbers_twoD = [[1,2,3],["a","b","c"]]

# How to go through elements inside a two dimensional list
for i in range(len(list_of_numbers_twoD)):
  # Incrementing to show that we are looking at list 1 and 2, and not list 0 and 1
  print("list " + str(i + 1))
  for j in range(len(list_of_numbers_twoD[i])):
    print(list_of_numbers_twoD[i][j])


# You can try these AFTER the workshop
# For each challenge, make sure you're going through all the elements of each dimension
# Tip: See if you can print all the values before adding the if, elif statements

# Challenge 1
# When you find an even number, print "i found an even number"

list_of_numbers_twoD = [[1,7,3,8,2,6],[11,19,71,32,15,10]]

print("Challenge 1:")

# Challenge 2
# When you find an odd number, print "i found an odd number"

print("Challenge 2:")

# Challenge 3
# When you find the number 10, print a statement of your choice

print("Challenge 3:")