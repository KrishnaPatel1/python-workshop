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



# Challenge 1
# Determine the grade of a student given the following grading scheme
# Below 25 --> F
# 25 to 44 --> E
# 45 to 59 --> D
# 60 to 74 --> C
# 75 to 89 --> B
# Above 90 --> A
print()
print("Challenge 1")

result = input()
grade = ""





# Challenge 2
# If a student has an A or B, he/she is an honour student
print()
print("Challenge 2")

is_honour_student = None

# Challenge 3
# If a student has an A or B 
# AND
# if he/she is also pursuing a minor
# then he/she is an excellent student
print()
print("Challenge 3")
print("Press 1 if the student is pursuing a minor, press 0 is the student is not")

pursuing_minor = input()


