'''
    # определение результата выстрела move для известной диспозиции кораблей boats_position
    # и карты выстрелов shoots_map
    # ВЫХОД: 'miss' | 'injury' | 'killed' (промах, ранен, убит).
'''


def check(move, boats_position, shoots_map):
    res = ('miss', 'injury', 'killed')
    if move in shoots_map.keys():
        return res[0]
    for boat in boats_position:
        if move in boat:
            if len(boat) > 1:
                i = 0
                for cell in boat:
                    if cell in shoots_map.keys():
                        i += 1
                if i + 1 == len(boat):
                    return res[2]
                else:
                    return res[1]
            else:
                return res[2]
    return res[0]


if __name__ == '__main__':
    field = [[('a', 4)], [('d', 2)], [('b', 1), ('c', 1)]]
    shoots_map = {('a', 1): 1, ('a', 4): 1, ('d', 1): 1}
    assert check(('b', 3), field, shoots_map) == 'miss'
    assert check(('d', 2), field, shoots_map) == 'killed'
    assert check(('c', 1), field, shoots_map) == 'injury'
    shoots_map[('c', 1)] = 1
    assert check(('b', 1), field, shoots_map) == 'killed'

