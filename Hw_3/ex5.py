# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def find_fib(number):
    fib_list = [0]
    x, y = 0, 1

    for i in range(number):
        x, y  = y, x + y
        fib_list.append(x)
        fib_list.insert(0, -x if i%2 else x)
    
    return fib_list

k = int(input("Input a number for fibonacchi list: "))
print(find_fib(k))
