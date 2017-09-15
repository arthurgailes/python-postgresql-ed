#creating lists
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)

print(len(numbers))

print(numbers[1])

print(numbers[0])

print(numbers[len(numbers)-1])

for number in numbers:
    print(number)

for number in numbers:
    print(number**2)

greater_than_three = 5 > 3
print(greater_than_three)

equal_to_five = 5 == 5
print(equal_to_five)

for number in numbers:
    print(number == 5)

for number in numbers:
    if number > 5:
        print(number)

#learning in and not
print(10 not in numbers)


import random


rando1 = 100
for i in numbers:
    rando2 = random.randint(0,9)
    if rando2 < rando1:
        rando1 = rando2

print(rando1)

magic_numbers = [random.randint(0,9), random.randint(0,9)]

def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))

    if (user_number) not in magic_numbers:
        return "This is not the number you are looking for"

    if (user_number) in magic_numbers:
        return "You got it right!"


def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is attempt {i}.".format(i = attempt+1))
        message = ask_user_and_check_number()
        print(message)

x = int(input("How many times would you like to run it? "))
run_program_x_times(x)