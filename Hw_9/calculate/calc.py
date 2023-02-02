def compl(numbers, op):
    numbers = numbers.split()

    real_1 = float(numbers[0])
    imag_1 = float(numbers[1])
    compl_1 = complex(real_1, imag_1)

    real_2 = float(numbers[2])
    imag_2 = float(numbers[3])
    compl_2 = complex(real_2, imag_2)
    
    if op == "+":
        return compl_1 + compl_2
    elif op == "-":
        return compl_1 - compl_2
    elif op == "*":
        return compl_1 * compl_2
    elif op == "/" and compl_2 != 0:
        return compl_1 / compl_2
    elif op == "**":
        return pow(compl_1, compl_2)