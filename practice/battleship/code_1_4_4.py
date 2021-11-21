'''
    # battle_state - это двухмерный массив numpy 4х4, который содержит результат наших выстрелов
    # last_move - последний сделанный вами ход в виде кортежа (letter, number),
    # letter - это одна из букв a,b,c,d, а number - это целое число от 1 до 4.
    (см. 3.15. Расстановка кораблей для морского боя);
    # result - результат последнего хода в виде строки
    'miss' | 'injury' | 'killed' (промах, ранен, убит) - см. 3.16. Определяем результат хода.
'''
import numpy as np


def kill_boat(battle_state, last_move):

    move = ("z", 0)  # пустой ход

    # ... ваш код по выбору хода ...
    last_move = (last_move[1] - 1, 'abcd'.index(last_move[0]))
    if battle_state[last_move] == 1:
        variants = check_cell(battle_state, last_move, 0)
        # [(1, 1), (2, 0)]
        for variant in variants:
            ships = check_cell(battle_state, variant, 2)
            if not ships:
                return 'abcd'[variant[1]], variant[0] + 1
    return move


def choose_act(battle_state, last_move, result):

    move = ("z", 0)

    if result == 'injury':
        return kill_boat(battle_state, last_move)

    last_move = (last_move[1] - 1, 'abcd'.index(last_move[0]))
    variants1 = []
    variants2 = []
    for ir, row in enumerate(battle_state):
        for ic, cell in enumerate(row):
            if cell == 0:
                if not check_cell(battle_state, (ir, ic), 2):
                    if not check_cell(battle_state, (ir, ic), -1):
                        variants2.append((ir, ic))
                    else:
                        variants1.append((ir, ic))
    if variants2:
        ix = np.random.choice(len(variants2))
        return 'abcd'[variants2[ix][1]], variants2[ix][0] + 1
    if variants1:
        ix = np.random.choice(len(variants1))
        return 'abcd'[variants1[ix][1]], variants1[ix][0] + 1
    return move


def check_cell(battle_state, last_move, status):
    variants = [(last_move[0], last_move[1] - 1), (last_move[0], last_move[1] + 1),
                (last_move[0] - 1, last_move[1]), (last_move[0] + 1, last_move[1])]

    variants = list(filter(lambda variant: not (variant[0] < 0 or variant[0] >= battle_state.shape[0] or \
                                                variant[1] < 0 or variant[1] >= battle_state.shape[1]), variants))

    return list(filter(lambda variant: battle_state[variant] == status, variants))


if __name__ == '__main__':
    # (d,2), (d,3), (d,4), (c,4)
    print(choose_act(np.array([[0,0,2,-1], [2,0,2,0], [0,-1,0,0], [-1,0,0,2]]), ('c', 2), 'kill'))
