# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input('Input number n: '))
count = 1
for i in range(1, n + 1):
    count = count * i
    print(count, end=' ')
