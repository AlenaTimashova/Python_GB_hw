# Получить список уникальных элементов заданной последовательности.

from random import randint

numbers_list = [randint(1, 8) for i in range(10)] # list comprehension
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list)) # filter, lambda
print(f'Для последовательности {numbers_list}, список уникальных элементов: {result_list}')
