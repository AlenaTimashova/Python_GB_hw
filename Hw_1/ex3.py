# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input('Введите номер четверти: '))

if quarter == 1:
        print('х: (0, +inf)\ny: (0, +inf)')
elif quarter == 2:
        print('х: (-inf, 0)\ny: (0, +inf)')
elif quarter == 3:
        print('х: (-inf, 0)\ny: (-inf, 0)')
elif quarter == 4:
        print('х: (0, +inf)\ny: (-inf, 0)')
else:
    print('Неверный номер четверти')
