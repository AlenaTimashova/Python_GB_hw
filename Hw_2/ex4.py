# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

n = int(input('Input number n = '))
sum = 0
for i in range (1, n+1, 2):
    sum += i

print(sum)