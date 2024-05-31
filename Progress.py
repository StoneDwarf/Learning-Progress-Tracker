import re

print('Learning Progress Tracker')


def name_check(name, the_list, students_list, students_data):
    first_name_pattern = re.compile(r"^(?!.*[-']{2})[A-Za-z][A-Za-z' -]*[A-Za-z]$")
    last_name_pattern = re.compile(r"^(?!.*[-']{2})[A-Za-z][A-Za-z' -]*[A-Za-z]$")
    email_pattern = re.compile(r"^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+$")
    test_input = name.split()
    if len(test_input) < 3:
        print('Incorrect credentials')
        return the_list, students_list, students_data
    first_name = test_input[0]
    last_name = ' '.join(test_input[1:-1])
    email = test_input[-1]
    if not first_name_pattern.match(first_name):
        print("Incorrect first name")
    elif not last_name_pattern.match(last_name):
        print("Incorrect last name")
    elif not email_pattern.match(email):
        print("Incorrect email")
    for id_number, student in students_data.items()
        if email in student[0]:
            print('This email is already taken.')
            break
    else:
        the_list.append(name)
        new_id = students_list[-1] + 1
        students_list.append(new_id)
        students_data[new_id] = [[first_name + last_name, email], [0,0,0,0]]
        print("The student has been added.")        
    return the_list, students_list, students_data


def student_add(students_list, students_data):
    print('Enter student credentials or "back" to return')
    new_list = []
    while True:
        user_input = input()
        if user_input == 'back':
            print(f'Total {len(new_list)} students have been added.')
            return
        else:
            name_check(user_input, new_list, students_list, students_data)   


def add_points():   # <<< finish this function
    print("Enter an id and points or 'back' to return")
    print(f'No student is found for id={}')
    print('Incorrect points format')
    id_input = name.split()
    for index, point in enumerate.students_data[student_id][1]
    print('Points updated')


def find_student():    # <<< finish this function
    print("Enter an id or 'back' to return")
    print(f'id points: Python={}; DSA={}; Databases={}; Flask={}')


def list_print(students):
    if len(students) > 1:
        print('No students found')
    else:
        for item in students[1:]:
            print(item)


students_data = {}
students_list = [0001]
none_commands = ['\t', None]
while True:
    user_input = input()
    if user_input == 'exit':
        print('Bye!')
        break
    elif user_input in none_commands or user_input.strip() == '':
        print('No input.')
    elif user_input == 'add students':
        student_add(students_list, students_data)
    elif user_input == 'back':
        print("Enter 'exit' to exit the program")
    elif user_input == 'list':
        list_print(students_list)
    else:
        print('unknown command!')
