number = input("Choose a number from 1-9")

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
  print(str(number) + " is party")

elif number == numbers["seven"]:
  print(str(number) + " makes you win at casinos")

elif number == numbers["nine"]:
  print(str(number) + " might be a little much...")

else:
  print("number is even: " + str(number))