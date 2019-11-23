number = int(input("Choose a number from 1-9: "))

if number == 1:
  print(str(number) + " is lonely")

elif number == 3:
  print(str(number) + " is a nice number")

elif number == 5:
  print(str(number) + " is a party")

elif number == 7:
  print(str(number) + " makes you win at casinos")

elif number == 9:
  print(str(number) + " might be a little much...")

else:
  print("You didn't a choose a number between 1-9: " + str(number))
  

# Challenge 1
# Determine the grade of a student given the result of a student using following grading scheme
# Below 25 --> F
# 25 to 44 --> E
# 45 to 59 --> D
# 60 to 74 --> C
# 75 to 89 --> B
# Above 90 --> A
# if the result isn't between 0 - 100, tell the user that he/she is a fool
print()
print("Challenge 1")
result = int(input())
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
input_ = int(input())
while (input_ != 1) and (input_ != 0):
  print("Please insert a value of 1 or 0")
  input_ = int(input())

pursuing_a_minor = bool(input_)

