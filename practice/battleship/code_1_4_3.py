'''
    # функция выбора хода - добить двухпалубный корабль
'''
import numpy as np


def kill_boat(battle_state, last_move):
    '''
    :param battle_state: двухмерный массив numpy 4х4, который содержит результат наших выстрелов
          battle_state[i,j] < 0, то стреляли по полю (i,j) и ничего,
          battle_state[i,j] == 0, то не стреляли; если 1 или 2 - ранили и убили
    :param last_move: последний ваш ход (letter, number),который ранил 2-х палубный
    :return: move=(letter, number) - выбранный ход, чтобы добить корабль
    '''
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


def check_cell(battle_state, last_move, status):
    variants = [(last_move[0], last_move[1] - 1), (last_move[0], last_move[1] + 1),
                (last_move[0] - 1, last_move[1]), (last_move[0] + 1, last_move[1])]

    variants = list(filter(lambda variant: not (variant[0] < 0 or variant[0] >= battle_state.shape[0] or \
                                                variant[1] < 0 or variant[1] >= battle_state.shape[1]), variants))

    return list(filter(lambda variant: battle_state[variant] == status, variants))


if __name__ == '__main__':
    assert kill_boat(np.array([[-1, -1, 0, 0], [1, 0, 0, 10], [0, 0, 0, 0], [2, 0, 0, 0]]), ('a', 2)) == ('b', 2)
    assert kill_boat(np.array([[0,0,0,0], [0,0,0,0], [2,0,1,0], [0,0,0,2]]), ('c', 3)) == ('c', 2)

