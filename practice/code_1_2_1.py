# ввод строки, содержащей три положительных числа через запятую, например "5, 2.0, 13"

def count_bits(string):
    numbers = list(map(lambda n: int(round(float(n), 0)), string.split(', ')))
    bits = [bin(number).count('1') for number in numbers]
    bits.sort()
    return ', '.join(map(str, bits))


print(count_bits(input()))

# if __name__ == '__main__':
#     print(count_bits("2, 3, 5"))
#     print(count_bits("6.7, 15, 17.4"))
#     print(count_bits("5, 2.0, 13"))
