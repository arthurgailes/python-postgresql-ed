student_list = []

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
    student['marks'].append(mark)

#s=create_student()

#print(s)

def calculate_average_mark(student):
    # What happens if the student has no marks yet?
    if len(student["marks"]) == 0:
        return 0
    else:
        # Add together all of the student['marks']
        total = sum(student["marks"])
        # Divide them by the total number of marks
        average_mark = total/len(student["marks"])

        return average_mark

def print_student_details(student):
    #print out a string that tells the user important information about this student
    print("{}, average mark: {}".format(student["name"],calculate_average_mark(student)))

def print_student_list(list):
    for i, student in enumerate(list):
        print("ID: {}".format(i))
        print_student_details(list[i])


def menu():
    #Add a student (to student_list)
    #Add a mark to a student
    # Print a list of students
    # Exit the application
    selection = input("Enter 'p' to print the student list, "
                      "s to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            print_student_list(student_list)
        elif selection == 's':
            student_list.append(create_student())
        elif selection =='a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print the student list, "
                          "s to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


menu()

#add_mark(s, 70)
#print_student_details(s)