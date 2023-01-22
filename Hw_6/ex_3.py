# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import factorial

n = int(input('Введите число: '))

list_mult = list(map(lambda x: x * factorial(x - 1), range(1,n+1))) # map, lambda
print(list_mult)