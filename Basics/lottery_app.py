#Sets vs Lists:
##Lists use []. Similar to a string; stores whatever you put in it literally.
##Sets remove duplicates from list. Syntax is set() or {}. Will print out in different orders every time
##  non-intersecting sets have no numbers in common. Adding 2 non-intersecting sets of 2 will have 4 values
##  intersecting sets have at least one value in common

lottery_values = {3,5,17,6}
user_values = {3,5,11,2}

#shows intersection between lists
lottery_values.intersection(user_values)

#Begin lottery program
#User can pick 6 numbers
import random

def menu():
    # Ask player for numbers
    user_numbers = get_player_numbers()
    #Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()
    #Print out winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print("You matched at {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))

def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    #Now, create a set of integers from this number_csv
    number_list = number_csv.split(",") #['1','2','3']
    integer_set = {int(number) for number in number_list}
    return integer_set



#Lottery calculates 6 random numbers (between 1 and 20)

def create_lottery_numbers():
    values = set() #Cannot initialize empty set like so: {}
    while len(values) <6 : #range = [0,1,2,3,4,5]
        number = random.randint(1,20)
        values.add(number)
    return values
print(create_lottery_numbers())

