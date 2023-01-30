from os.path import exists, join
from pathlib import Path

from database_commands import *
from search import search_discipline, search_student



def add_student(discipline, student_name, grade):
    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'),
               f'{student_name} {grade}',
               'a')


def add_grade(discipline, student_name, grade):
    stud_dict = get_students_dict(discipline)

    stud_dict[student_name].append(grade)

    write_data(join(DISCIPLINES_DIR, f'{discipline}.txt'), stud_dict)


def user_interface():
    print('Выберите роль:\n1. Преподаватель\n2. Ученик\n')

    decision = input('Ваша роль: ')

    if decision == '1':
        print('\nСписок предметов:')
        print('\n'.join(get_disciplines_dict().keys()) + '\n')

        discipline = input('Введите название предмета: ')

        search_res = search_discipline(discipline)

        if search_res[0]:
            student = input('Введите фамилию ученика: ').capitalize()

            if not search_student(search_res[1], student):
                grade = input('Введите оценку: ')

                add_student(search_res[1], student, grade)

            else:
                grade = input('Введите оценку: ')

                add_grade(search_res[1], student, grade)

        else:
            print('Такого предмета нет в списке!')

    elif decision == '2':
        surname = input('Введите вашу фамилию: ')

        for name, filename in get_disciplines_dict().items():
            if search_student(filename, surname):
                print(f'{name}: {", ".join(get_students_dict(filename)[surname])}')


if __name__ == "__main__":
    user_interface()