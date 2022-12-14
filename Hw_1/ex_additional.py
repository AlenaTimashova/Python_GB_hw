# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def check_deMorgan_law(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    
    return left == right

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x}, {y}, {z}) is {check_deMorgan_law(x, y, z)}')