'''
    Обьединить два неупорядоченых списка чисел в один упорядоченый.
'''


def merge(left, right):
    left = sorted(eval(left))
    right = sorted(eval(right))
    result = []
    while len(left) and len(right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if len(left):
        result.extend(left)
    else:
        result.extend(right)
    return result


if __name__ == '__main__':
    #print(merge(input()))
    assert merge('[2, 1, 5]', '[4, 7, 2]') == [1, 2, 2, 4, 5, 7]
    assert merge('[]', '[3, 2, 1]') == [1, 2, 3]

