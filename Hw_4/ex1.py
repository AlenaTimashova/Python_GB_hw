# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ round())

from math import pi
size = int(input("Enter how many symbols after '.' to shwo in PI: "))
p = str(pi)
result = p[:(size + 2)]

print(result)


