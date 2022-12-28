# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и вывести многочлен степени k.

from random import randint
 
k = int(input('Введите натуральную степень k:'))

numbers = {x: randint(0, 100) for x in range(k, -1, -1)}

polynomial = []
for key, value in numbers.items():
    polynomial.append(f'{value}x^{key}')
poly = ' + '.join(polynomial)
poly = poly.replace('x^1 ', 'x ').replace('x^0', '') 

print(poly)