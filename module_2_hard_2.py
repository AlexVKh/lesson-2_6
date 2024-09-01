# def factor_search - функция для поиска делителей числа
def factor_search(n):
    factor_list = [] # factor_list - список делителей числа
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            factor_list.append(i)
    factor_list.append(n)
    return factor_list

# def term_search - функция для разложения числа на пары слагаемых
def term_search(factor_list):
    term_list = [] # term_list - список слагаемых чисел из factor_list
    for i in factor_list:
        for j in range(1, i):
            if j < i / 2:
                term_list.append([j, i - j])
    return term_list

#def sort - сортировка списка списков по 1-ому элементу
def sort(term_list):
    term_list.sort(key=lambda x: x[0])
    return

while True:
    n = int(input("Введите числа от 3 до 20: "))
    if n == 0:
        print('End')
        break
    factor_list = factor_search(n)
    result = term_search(factor_list)
    sort(result)
    for i in range(len(result)):
        for j in range(2):
            print (result[i][j], end='')
    print()



