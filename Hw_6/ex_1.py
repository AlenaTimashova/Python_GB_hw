# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# from random import randint

my_list = [i for i in range(1, 10)]  # list comprehension

def find_sum(lst):
    sum_list = [value for i, value in enumerate(lst) if i % 2] # enumerate
    return sum(sum_list)

print(find_sum(my_list))
