while True:
    print('Введите число от 3 до 20 включительно: ')
    n = int(input())
    if n == 0:
        print('End')
        break
    factor_list = []  # factor_list - список делителей введенного числа
    term_list = []  # term_list - список слагаемых чисел из factor_list
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factor_list.append(i)
    factor_list.append(n)
    for i in factor_list:
        for j in range(1, i):
            if j < i / 2:
                term_list.append(j)
                term_list.append(i - j)
    for i in range(len(term_list)):
        print(term_list[i], end='')
    print()
