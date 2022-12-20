# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input('Input number n: '))
i = 2

while i <= n:
    if n % i == 0:
        print(i)
        break
    i += 1
