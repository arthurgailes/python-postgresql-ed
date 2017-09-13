student = {"name": "Jose",
           "marks":[70,50,80,44,99],
           "exams": {
               "final": 70,
               "midterm": 50
           }}


def create_student():
    # Ask the user for the student's name
    name = input("What is your name? ")
    #Create the dictionary in the format {'name', '<student_name>', 'marks': []}
    student_data = {
        "name": name,
        "marks": []
    }
    #Return that dictionary
    return student_data

def add_mark(student, mark):
    #Append a mark to the student dictionary
    mark = input("Enter mark: ")
    student['marks'].append(mark)

s=create_student()
(add_mark(s,70))  #Pasing by reference (to the dictionary)

def add_number

print(s)