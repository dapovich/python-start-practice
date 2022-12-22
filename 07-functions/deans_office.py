# 3. Деканат.
#
# Дано: список студентов: каждый элемент списка содержит фамилию, имя, отчество, год рождения, курс, номер группы, оценки по пяти предметам.
#
# Задание: реализуйте сл. функции:
#
# 1) возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке;
# 2) находит средний балл каждой группы по каждому предмету;
# 3) определяет самого старшего студента и самого младшего студентов.
# 4) возвращает словарь, где для каждой группы определен лучший с точки зрения успеваемости студент.

from collections import defaultdict


# List of students realized through dictionary
students_dict = {
    1 : {
        'name' : 'Ivan',
        'surname' : 'Beliy',
        'patronymic' : 'Aleksandrovich',
        'course' : 1,
        'birth_year' : 2000,
        'group_number' : '321-1',
        'grades' : {
            'math' : 3,
            'electrical_circuit' : 4,
            'digital_signal_processing' : 4,
            'fpga_programming' : 5,
            'physics' : 4
        }
    },

    2 : {
        'name' : 'Andrey',
        'surname' : 'Chernuy',
        'patronymic' : 'Vladimirovich',
        'course' : 2,
        'birth_year' : 1997,
        'group_number' : '201',
        'grades' : {
            'math' : 3,
            'electrical_circuit' : 4,
            'digital_signal_processing' : 2,
            'fpga_programming' : 4,
            'physics' : 3
        }
    },

    3 : {
        'name' : 'Vasiliy',
        'surname' : 'Terkin',
        'patronymic' : 'Timofeevich',
        'course' : 3,
        'birth_year' : 2002,
        'group_number' : '521',
        'grades' : {
            'math' : 5,
            'electrical_circuit' : 5,
            'digital_signal_processing' : 5,
            'fpga_programming' : 4,
            'physics' : 3
        }
    },

    4 : {
        'name' : 'Evgeniy',
        'surname' : 'Akimov',
        'patronymic' : 'Petrovich',
        'course' : 1,
        'birth_year' : 1998,
        'group_number' : '321-1',
        'grades' : {
            'math' : 5,
            'electrical_circuit' : 4,
            'digital_signal_processing' : 4,
            'fpga_programming' : 5,
            'physics' : 5
        }
    },

    5 : {
        'name' : 'Alina',
        'surname' : 'Koshkina',
        'patronymic' : 'Aleksandrova',
        'course' : 2,
        'birth_year' : 2001,
        'group_number' : '521',
        'grades' : {
            'math' : 5,
            'electrical_circuit' : 5,
            'digital_signal_processing' : 5,
            'fpga_programming' : 5,
            'physics' : 5
        }
    },

    6 : {
        'name' : 'Timofey',
        'surname' : 'Kishenev',
        'patronymic' : 'Olegovich',
        "course" : 3,
        'birth_year' : 1997,
        'group_number' : '201',
        'grades' : {
            'math' : 3,
            'electrical_circuit' : 5,
            'digital_signal_processing' : 3,
            'fpga_programming' : 4,
            'physics' : 3
        }
    },
}


def get_the_list_of_students(students_dict: dict, course_number: int) -> list[str]:
    return sorted([
        students_dict[key]['surname'].lower() + ' ' + students_dict[key]['name'].lower()
        for key in students_dict.keys()
        if students_dict[key]['course'] == course_number
    ])


def get_the_average_grade(students_dict: dict) -> dict:
    # Get the existing numbers of groups of students
    groups = []
    for student_number in students_dict.keys():
        group_number = students_dict[student_number]["group_number"]
        groups.append(group_number)

    # Use defaultdict(list) to make such data_structure:
    # dict[key = group_number; value = dict[ keys = name_of_subject; value = [grade1, grade2, ...] ]]
    groups_grades = {}
    for group_number in groups:
        groups_grades[group_number] = defaultdict(list)

    for student_number in students_dict.keys():
        group_number = students_dict[student_number]["group_number"]
        for subject, grade in students_dict[student_number]["grades"].items():
            groups_grades[group_number][subject].append(grade)

    # print("Все оценки по предметат для каждой группы:")
    # print(groups_grades, end='\n\n')

    average_grades = {}
    for group_number in groups:
        average_grades[group_number] = defaultdict(int)

    for group_number in groups_grades.keys():
        for subject, grade in groups_grades[group_number].items():
            average_grade = sum(grade) / len(grade)
            average_grades[group_number][subject] = average_grade

    return average_grades
    

def get_the_youngest_and_the_oldest_students(students_dict: dict) -> list[tuple]:
    """
    Find the max and min birth year in the list of students.
    NOTE: if there are several students with the max value of birth_year, it
    will return all of these students.
    """
    birth_years = {}
    for student_number in students_dict.keys():
        student_surname = students_dict[student_number]['surname']
        student_birth_year = students_dict[student_number]['birth_year']
        birth_years[student_surname] = student_birth_year

    max_birth_year = max(birth_years.values())
    min_birth_year = min(birth_years.values())

    # Use lambda function to sort list of tuples by the 2-th element in tuple (birth_year value)
    return sorted([
        (surname, birth_year)
        for surname, birth_year in birth_years.items()
        if birth_year == max_birth_year or birth_year == min_birth_year
    ], key=lambda item: item[1])


def get_the_best_student_in_groups(students_dict: dict) -> dict:
    # Get the dict of all students in groups with its average grade
    groups = defaultdict(dict)
    for student_number in students_dict.keys():
        group_number = students_dict[student_number]['group_number']
        number_of_subjects = len(students_dict[student_number]['grades'])
        grades_average = sum(students_dict[student_number]['grades'].values()) / number_of_subjects
        student_surname = students_dict[student_number]['surname']
        groups[group_number][student_surname] = grades_average

    # Dictionary with the best students in groups
    best_students = dict()
    for group_number in groups.keys():
        # Return the surname of student with max average grade
        # NOTE: use itemgetter() and key argument to specify that
        # find max among the VALUES.
        best_student_surname = max(groups[group_number].keys(), key=lambda key: groups[group_number][key])
        best_student_average_grade = groups[group_number][best_student_surname]
        best_students[group_number] = {best_student_surname : best_student_average_grade}

    return best_students




if __name__ == '__main__':

    print("1. Функция, которая возвращает список студентов по курсу, причем студенты одного курса располагались в алфавитном порядке:")
    course_number = 2
    print(f"List of students with {course_number=}:")
    print(get_the_list_of_students(students_dict, 2), end='\n\n')

    print("2. Функция, которая находит средний балл каждой группы по каждому предмету:")
    print(get_the_average_grade(students_dict), end='\n\n')

    print("3. Функция, которая определяет самого старшего студента и самого младшего студентов.")
    print(get_the_youngest_and_the_oldest_students(students_dict), end='\n\n')

    print("4. Функция, которая возвращает словарь, где для каждой группы определен лучший с точки зрения успеваемости студент.")
    print(get_the_best_student_in_groups(students_dict), end='\n\n')

