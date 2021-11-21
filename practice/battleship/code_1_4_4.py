'''
    # battle_state - это двухмерный массив numpy 4х4, который содержит результат наших выстрелов
    # last_move - последний сделанный вами ход в виде кортежа (letter, number),
    # letter - это одна из букв a,b,c,d, а number - это целое число от 1 до 4.
    (см. 3.15. Расстановка кораблей для морского боя);
    # result - результат последнего хода в виде строки
    'miss' | 'injury' | 'killed' (промах, ранен, убит) - см. 3.16. Определяем результат хода.
'''
import numpy as np


def choose_act(battle_state, last_move, result):

    move = ("z", 0)

    # ... здесь должен быть ваш код по выбору нового хода move

    return move


def check_cell(battle_state, last_move, status):
    variants = [(last_move[0], last_move[1] - 1), (last_move[0], last_move[1] + 1),
                (last_move[0] - 1, last_move[1]), (last_move[0] + 1, last_move[1])]

    variants = list(filter(lambda variant: not (variant[0] < 0 or variant[0] >= battle_state.shape[0] or \
                                                variant[1] < 0 or variant[1] >= battle_state.shape[1]), variants))

    return list(filter(lambda variant: battle_state[variant] == status, variants))


if __name__ == '__main__':
    # (d,2), (d,3), (d,4), (c,4)
    print(choose_act(np.array([[-1, -1, 2, 0], [0, 0, 0, 0], [0, 2, 0, 0], [2, 0, 0, 0]]), ('b', 1), 'miss'))
