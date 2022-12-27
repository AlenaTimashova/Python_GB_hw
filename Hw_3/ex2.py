# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def find_mult_list(lst):
    new_list = []
    
    if len(lst) % 2 == 0:
        limit = len(lst) // 2
    else:
        limit = len(lst) // 2 + 1

    for i in range(limit):
        new_list.append(lst[i] * lst[-(i+1)])
    print(new_list) 

my_list = [2, 3, 5, 6]

find_mult_list(my_list)

