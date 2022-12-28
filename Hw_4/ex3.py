# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
num_list = [5, 7, 5, 9, 15, 2, 7]

num_dict = {}
for i in num_list: 
    num_dict[i] = num_dict.get(i, 0) + 1
    new_list = [key for key, value in num_dict.items() if value == 1]

print(f'Список неповторяющихся элементов: {new_list}')

