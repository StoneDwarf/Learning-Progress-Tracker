import re

print('Learning Progress Tracker')


def name_check(name, the_list):
    first_name_pattern = re.compile(r"^(?!.*[-']{2})[A-Za-z][A-Za-z' -]*[A-Za-z]$")
    last_name_pattern = re.compile(r"^(?!.*[-']{2})[A-Za-z][A-Za-z' -]*[A-Za-z]$")
    email_pattern = re.compile(r"^[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+$")
    test_input = name.split()
    if len(test_input) < 3:
        print('Incorrect credentials')
        return the_list
    first_name = test_input[0]
    last_name = ' '.join(test_input[1:-1])
    email = test_input[-1]
    if not first_name_pattern.match(first_name):
        print("Incorrect first name")
    elif not last_name_pattern.match(last_name):
        print("Incorrect last name")
    elif not email_pattern.match(email):
        print("Incorrect email")
    else:
        the_list.append(name)
        print("The student has been added.")
    return the_list


def student_add():
    print('Enter student credentials or "back" to return')
    new_list = []
    while True:
        user_input = input()
        if user_input == 'back':
            print(f'Total {len(new_list)} students have been added.')
            return
        else:
            new_list = name_check(user_input, new_list)


none_commands = ['\t', None]
while True:
    user_input = input()
    if user_input == 'exit':
        print('Bye!')
        break
    elif user_input in none_commands or user_input.strip() == '':
        print('No input.')
    elif user_input == 'add students':
        student_add()
    elif user_input == 'back':
        print("Enter 'exit' to exit the program")
    else:
        print('unknown command!')
