# Напишите программу, которая будет преобразовывать десятичное число в двоичное

number = int(input("Input number:"))

new_num = ''
while number > 0:
    new_num = str(number % 2) + new_num 
    number = number // 2
print(new_num)
