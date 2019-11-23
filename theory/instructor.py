mustang_year = 2016
mustang_colour = "red"
mustang_horsepower = 375




classrooms_in_hall_building = ["H435", "H831", "H545", "H450"]

hall_building = {
    "street_address": "1455 Boul de Maisonneuve Ouest",
    "floors": 12,
    "classrooms": classrooms_in_hall_building,
}

print(classrooms_in_hall_building)
print(hall_building)
x = 1 + 2 * 3
print(x)

x = 2*3/2*4+1
print(3*(4/2)+2*2)

x=1
y=2
z=3

print(x*2 - 3*y/z)
print(2 <= 2)

x = 2 < 3
print(x)

math_201 = [50, 90, 37, 57, 10, 76, 29]
math_202 = [90, 90, 82, 56, 17, 40, 75]
math_203 = [78, 80, 85, 47, 80, 100, 56]
math_204 = [34, 78, 76, 43, 73, 83, 72]
math_205 = [98, 65, 58, 49, 70, 89, 90]

math_201_total = 0
math_201_number_of_results_in_list = 0
math_201_average = 0
for result in math_201:
  math_201_number_of_results_in_list = math_201_number_of_results_in_list + 1
  math_201_total = math_201_total + result
  
  math_201_average = math_201_total/math_201_number_of_results_in_list


math_202_total = 0
math_202_number_of_results_in_list = 0
math_202_average = 0
for result in math_202:
  math_202_number_of_results_in_list = math_202_number_of_results_in_list + 1
  math_202_total = math_202_total + result
  
  math_202_average = math_202_total/math_202_number_of_results_in_list

def average(lis):
    return 1

def say_hello():
    print("Hello")

say_hello()

math_201_average = average(math_201)

if 2 > 3:
    print("I am inside the if-statement")

print("I am outside the if-statement")

x = 1
y = 2
z = False
result = x*2 >= y != z

print(result)