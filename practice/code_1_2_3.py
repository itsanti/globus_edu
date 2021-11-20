'''
    Для заданного значения переменной N необходимо:
    - вывести сумму всех целых числа от 0 до N-1, если N<10
    - вывести текст "used numbers= 0, 1, 2, 3, ..., N-1", если 10<=N<20
    - вывести текст "very big number", если N>=20
'''


def numbers_work(string):
    n = int(string)
    if n < 10:
        return sum(range(n))
    elif 10 <= n < 20:
        return 'used numbers= ' + ', '.join(map(str, range(n)))
    else:
        return 'very big number'


if __name__ == '__main__':
    #print(numbers_work(input()))
    assert numbers_work("4") == 6
    assert numbers_work("12") == 'used numbers= 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'
    assert numbers_work("22") == 'very big number'
