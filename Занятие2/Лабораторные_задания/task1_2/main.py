A = int(input('введите число'))
B = int(input('введите число'))
cond_1 = A % 2 == 1
cond_2 = B % 2 == 1
if cond_1 and cond_2:
    print('каждое из чисел нечетное')