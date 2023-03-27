from api import Request
from database import data


def main():
    request = Request(data)
    print(request.get_list_of_students(course_number=3))
    print(request.get_average())
    print(request.get_best())
    print(request.get_worst())


if __name__ == "__main__":
    main()
