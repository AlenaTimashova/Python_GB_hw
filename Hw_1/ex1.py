# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def Is_Weekend(number_of_the_week):
    if(number_of_the_week == 6) or (number_of_the_week == 7):
        print("Это выходной")
    else:
        print("Это не выходной")

week_day = int(input('Введите день недели цифрой: '))

Is_Weekend(week_day)
