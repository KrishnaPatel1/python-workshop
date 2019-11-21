number = input("Choose a number from 1-9")

# Dictionary example
# Access variables with their keys, and they will return their values
# key: value

numbers = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

if number == numbers["one"]:
  print(str(number) + " is lonely")

elif number == numbers["three"]:
  print(str(number) + " is a nice number")

elif number == numbers["five"]:
  print(str(number) + " is a party")

elif number == numbers["seven"]:
  print(str(number) + " makes you win at casinos")

elif number == numbers["nine"]:
  print(str(number) + " might be a little much...")

else:
  print("number is even: " + str(number))



# Alternatively, List Example 
# Remember, you start accessing values with "0" and not "1"

numbers = [1,2,3,4,5,6,7,8,9]

if number == numbers[0]:
  print(str(number) + " is lonely... again")

elif number == numbers[2]:
  print(str(number) + " i know is a nice number, but really?")

elif number == numbers[4]:
  print(str(number) + " is still a party")

elif number == numbers[6]:
  print(str(number) + " might not make you win twice")

elif number == numbers[8]:
  print(str(number) + " is still a lot")

else:
  print("Won't change the fact that the number is even: " + str(number))