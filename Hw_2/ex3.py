# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

list1 = [2, 2, 3, 1, 8]
n = abs(int(input('Input number n = ')))
numbers = list(range(-n, n+1))
print(numbers)
mult = 1
for i in list1:
    mult *= numbers[i]

print(mult)