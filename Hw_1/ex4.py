# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве


x1 = int(input("Введите координату х первой точки: "))
y1 = int(input("Введите координату y первой точки: "))
x2 = int(input("Введите координату х второй точки: "))
y2 = int(input("Введите координату y второй точки: "))

line_length  = round((((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)), 2)
print(f'Расстояние между точками равно {line_length}')