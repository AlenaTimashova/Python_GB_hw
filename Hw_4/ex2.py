# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def factorize(number):
    fact_list = []
    i = 2
    while i <= number**0.5:
        if number % i == 0:
            fact_list.append(i)
            number //= i
        else:
            i += 1
    
    if number > 1:
        fact_list.append(number)

    return fact_list


num = int(input("Input a number: "))

print(factorize(num))
