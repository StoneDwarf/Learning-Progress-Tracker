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
        return
    elif not last_name_pattern.match(last_name):
        print("Incorrect last name")
        return
    elif not email_pattern.match(email):
        print("Incorrect email")
        return
    for id_number, student in students_data.items():
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


def add_points(students_list, students_data):
    print("Enter an id and points or 'back' to return")
    while True:
        student_id = input()
        if student_id == 'back':
            return students_list, students_data
        else:
            id_input = student_id.split()
            if len(id_input) != 5:
                print('Incorrect points format')
                continue
            try:
                new_id = int(id_input[0])
                if new_id not in students_list:
                    print(f'No student is found for id={new_id}')
                    continue
  #  students_data = {new_id: [[first_name + last_name, email], [0,0,0,0]]}
            except:
                print(f'No student is found for id={id_input[0]}')
            try:
                new_id = int(id_input[0])
                points = list(map(int, id_input[1:]))
                int_pattern = re.compile(r'^-?\d+$')
                if any(point < 0 for point in points):
                    print('Incorrect points format')
                    continue
                elif not all(int_pattern.match(item) for item in id_input[1:]):
                    print('Incorrect points format')
                    continue
                else:
                    for index in range(len(points)):
                        students_data[new_id][1][index] += points[index]
                    print('Points updated')
                    continue
  #  students_data = {new_id: [[first_name + last_name, email], [0,0,0,0]]}
            except:
                print('Incorrect points format')

def find_student(students_data):   #  students_data = {new_id: [[first_name + last_name, email], [0,0,0,0]]}
    print("Enter an id or 'back' to return")
    while True:
        student_id = input()
        if student_id == 'back':
            return
        try:
            id = int(student_id)
            print(f'{id} points: Python={students_data[id][1][0]}; DSA={students_data[id][1][1]}; Databases={students_data[id][1][2]}; Flask={students_data[id][1][3]}')
        except:
            print(f'No student is found for id={student_id}')


def list_print(students):
    if len(students) == 1:
        print('No students found')
    else:
        print('Students:')
        for item in students[1:]:
            print(item)


def course_check(students_data):
    max_points = {'python': 600, 'DSA': 400, 'databases': 480, 'flask': 550}
    course_list = ['python', 'DSA', 'databases', 'flask']

    print('Type the name of a course to see details or \'back\' to quit')
    general_stat(students_data)

    while True:
        user_input = input()
        if user_input == "back":
            return
        elif user_input not in course_list:
            print('Unknown course')
        else:
            course_name = user_input.capitalize()
            print(f"{course_name}")
            print("ID    Points    Completion")
            student_stats = []
            for student_id, data in students_data.items():
                points = data[1]
                if user_input == 'python':
                    course_index = 0
                elif user_input == 'DSA':
                    course_index = 1
                elif user_input == 'databases':
                    course_index = 2
                elif user_input == 'flask':
                    course_index = 3

                course_points = points[course_index]
                if course_points > 0:                    
                    completion = (course_points / max_points[user_input]) * 100
                    student_stats.append((student_id, course_points, completion))
            student_stats.sort(key=lambda x: x[1], reverse=True)
            for student_id, course_points, completion in student_stats:
                print(f"{student_id}    {course_points}    {completion:.1f}%")


def general_stat(students_data):
    course_names = ['Python', 'DSA', 'Databases', 'Flask']
    course_sums = {name: 0 for name in course_names}
    course_submissions = {name: 0 for name in course_names}
    course_counts = {name: 0 for name in course_names}

    for student_id, data in students_data.items():
        points = data[1]
        for course_index, point in enumerate(points):
            course_name = course_names[course_index]
            course_sums[course_name] += point
            if point > 0:
                course_submissions[course_name] += 1
                course_counts[course_name] += 1

    most_popular = max(course_submissions, key=course_submissions.get)
    least_popular = min(course_submissions, key=course_submissions.get)
    highest_activity = max(course_sums, key=course_sums.get)
    lowest_activity = min(course_sums, key=course_sums.get)
    easiest_course = max(course_counts, key=lambda x: course_sums[x] / course_counts[x] if course_counts[x] > 0 else float('-inf'))
    hardest_course = min(course_counts, key=lambda x: course_sums[x] / course_counts[x] if course_counts[x] > 0 else float('inf'))

    max_sum = max(course_sums.values())
    min_sum = min(course_sums.values())
    most_popular = [course for course, total in course_sums.items() if total == max_sum]
    least_popular = [course for course, total in course_sums.items() if total == min_sum]
    
    max_activity = max(course_submissions.values())
    min_activity = min(course_submissions.values())
    highest_activity = [course for course, activity in course_submissions.items() if activity == max_activity]
    lowest_activity = [course for course, activity in course_submissions.items() if activity == min_activity]

    max_average = max(course_sums[course] / course_counts[course] if course_counts[course] > 0 else float('-inf') for course in course_counts)
    min_average = min(course_sums[course] / course_counts[course] if course_counts[course] > 0 else float('inf') for course in course_counts)
    easiest_course = [course for course in course_counts if course_counts[course] > 0 and course_sums[course] / course_counts[course] == max_average]
    hardest_course = [course for course in course_counts if course_counts[course] > 0 and course_sums[course] / course_counts[course] == min_average]
    
    print(f"Most popular: {', '.join(most_popular) if most_popular and max_sum > 0 else 'n/a'}")
    print(f"Least popular: {', '.join(least_popular) if least_popular and min_sum < max_sum else 'n/a'}")
    print(f"Highest activity: {', '.join(highest_activity) if highest_activity and max_activity > 0 else 'n/a'}")
    print(f"Lowest activity: {', '.join(lowest_activity) if lowest_activity and min_activity < max_activity else 'n/a'}")
    print(f"Easiest course: {', '.join(easiest_course) if easiest_course and max_average > float('-inf') else 'n/a'}")
    print(f"Hardest course: {', '.join(hardest_course) if hardest_course and min_average < float('inf') else 'n/a'}")


students_data = {}
students_list = [0]
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
    elif user_input == 'add points':
        add_points(students_list, students_data)
    elif user_input == 'find':
        find_student(students_data)
    elif user_input == 'statistics':
        course_check(students_data)
    else:
        print('Unknown command!')
