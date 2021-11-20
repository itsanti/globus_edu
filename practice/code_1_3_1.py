'''
    список номеров людей, в порядке их выбывания из круга
'''


# ===========Область программирования слушателя ==================

def form_list(N, K):
    res = []
    count = 1
    i = 0
    while len(res) != N:
        el = (i % N) + 1
        if el not in res:
            if count % K == 0:
                res.append(el)
                count = 1
            else:
                count += 1
        i += 1
    return res


# ==============================================================

# ---------- !!! эту часть не меняем !!! ---------
if __name__ == '__main__':
    #N = int(input())
    #K = int(input())
    assert form_list(7, 2) == [2, 4, 6, 1, 5, 3, 7]
    assert form_list(12, 3) == [3, 6, 9, 12, 4, 8, 1, 7, 2, 11, 5, 10]

