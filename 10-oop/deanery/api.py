from collections import defaultdict


class Request:
    def __init__(self, data: dict):
        self.__data = data

    def get_average(self):
        """
        Get the average grade of groups of students
        """
        # Get the existing numbers of groups of students
        groups = []
        for student_number in self.__data.keys():
            group_number = self.__data[student_number]["group_number"]
            groups.append(group_number)

        # Use defaultdict(list) to make such data_structure:
        # dict[key = group_number; value = dict[ keys = name_of_subject;
        # value = [grade1, grade2, ...] ]]
        groups_grades = {}
        for group_number in groups:
            groups_grades[group_number] = defaultdict(list)

        for student_number in self.__data.keys():
            group_number = self.__data[student_number]["group_number"]
            for subject, grade in self.__data[student_number]["grades"].items():
                groups_grades[group_number][subject].append(grade)

        average_grades = {}
        for group_number in groups:
            average_grades[group_number] = defaultdict(int)

        for group_number in groups_grades.keys():
            for subject, grade in groups_grades[group_number].items():
                average_grade = sum(grade) / len(grade)
                average_grades[group_number][subject] = average_grade

        return average_grades

    def get_list_of_students(self, course_number: int) -> list[str]:
        """
        Get the list of student for specific course
        """
        return [
            self.__data[key]["surname"].lower() + " " + self.__data[key]["name"].lower()
            for key in self.__data.keys()
            if self.__data[key]["course"] == course_number
        ]

    def get_best(self) -> dict:
        """
        Return the surname of students for each group
        with best average grade
        """
        # Get the dict of all students in groups with its average grade
        groups = defaultdict(dict)
        for student_number in self.__data.keys():
            group_number = self.__data[student_number]['group_number']
            number_of_subjects = len(self.__data[student_number]['grades'])
            grades_average = sum(self.__data[student_number]['grades'].values()) / number_of_subjects
            student_surname = self.__data[student_number]['surname']
            groups[group_number][student_surname] = grades_average

        # Create a dictionary with the best average grade students in groups
        best_students = dict()
        for group_number in groups.keys():
            # Return the surname of student with max average grade
            # NOTE: use itemgetter() and key argument to specify that
            # find max among the VALUES.
            best_student_surname = max(groups[group_number].keys(), key=lambda key: groups[group_number][key])
            best_student_average_grade = groups[group_number][best_student_surname]
            best_students[group_number] = {best_student_surname: best_student_average_grade}

        return best_students

    def get_worst(self) -> dict:
        """
        Return the surname of students for each group
        with the worst average grade
        """
        # Get the dict of all students in groups with its average grade
        groups = defaultdict(dict)
        for student_number in self.__data.keys():
            group_number = self.__data[student_number]['group_number']
            number_of_subjects = len(self.__data[student_number]['grades'])
            grades_average = sum(self.__data[student_number]['grades'].values()) / number_of_subjects
            student_surname = self.__data[student_number]['surname']
            groups[group_number][student_surname] = grades_average

        # Create a dictionary with the worst average grade in groups
        worst_students = dict()
        for group_number in groups.keys():
            # Return the surname of student with min average grade
            worst_student_surname = min(groups[group_number].keys(), key=lambda key: groups[group_number][key])
            worst_student_average_grade = groups[group_number][worst_student_surname]
            worst_students[group_number] = {worst_student_surname: worst_student_average_grade}

        return worst_students
