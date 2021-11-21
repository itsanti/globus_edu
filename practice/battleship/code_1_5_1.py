''' --------- модуль слушателя курса -------- '''
import numpy as np
import random
# ==================================================================

def check_cell(battle_state, last_move, status):
    variants = [(last_move[0], last_move[1] - 1), (last_move[0], last_move[1] + 1),
                (last_move[0] - 1, last_move[1]), (last_move[0] + 1, last_move[1])]

    variants = list(filter(lambda variant: not (variant[0] < 0 or variant[0] >= battle_state.shape[0] or \
                                                variant[1] < 0 or variant[1] >= battle_state.shape[1]), variants))

    return list(filter(lambda variant: battle_state[variant] == status, variants))


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


def format_positions(boats_position):
    result = []
    for boat in boats_position:
        if type(boat) is list:
            for ix, cell in enumerate(boat):
                boat[ix] = ('abcd'[cell[1]], cell[0] + 1)
        else:
            boat = ('abcd'[boat[1]], boat[0] + 1)
        result.append(boat)
    return result


def fill_board(board, cells):
    for cell in cells:
        for row in (-1, 0, 1):
            for c in (-1, 0, 1):
                if 0 <= cell[0] + row < len(board) and 0 <= cell[1] + c < len(board[0]):
                    board[cell[0] + row][cell[1] + c] = 1
    return board


def select_random_cell(board, part_cell=None):
    if part_cell is None:
        row = random.randrange(len(board))
        cell = random.randrange(len(board[0]))
        while board[row][cell] is not None:
            row = random.randrange(len(board))
            cell = random.randrange(len(board[0]))
        return row, cell
    else:
        rows = [part_cell[0], part_cell[0] + 1, part_cell[0] - 1]
        rows = [row for row in rows if 0 <= row < len(board)]
        cells = []
        for row in rows:
            if part_cell[0] == row:
                if part_cell[1] - 1 >= 0 and board[row][part_cell[1] - 1] is None:
                    cells.append((row, part_cell[1] - 1))
                elif part_cell[1] + 1 < len(board[row]) and board[row][part_cell[1] + 1] is None:
                    cells.append((row, part_cell[1] + 1))
            else:
                if board[row][part_cell[1]] is None:
                    cells.append((row, part_cell[1]))
        return random.choice(cells)


# ================ эти функции обязательно должны быть =================


# --- функция начальной расстановки кораблей 1-палубных и 2-х палубных---
def start_boats_position(how_many_boats):
    n1 = how_many_boats[0]  # кол-во однопалубных
    n2 = how_many_boats[1]  # кол-во двухпалубных

    board = [[None] * 4 for i in range(4)]
    boats_position = []

    n2_cells = []
    for i in range(2 * n2):
        if i % 2 == 0:
            n2_cells.append(select_random_cell(board, None))
            board[n2_cells[0][0]][n2_cells[0][1]] = 1
        else:
            n2_cells.append(select_random_cell(board, n2_cells[0]))
            boats_position.append(n2_cells)
            board = fill_board(board, n2_cells)
            n2_cells = []

    for i in range(n1):
        cell = select_random_cell(board, None)
        board = fill_board(board, [cell])
        boats_position.append([cell])

    return format_positions(boats_position)


# ---------- функция выбора нового хода ----------
def choose_act(battle_state, last_move, result):

    move = ("z", 0)

    if result == 'injury':
        return kill_boat(battle_state, last_move)
    elif result == 'miss':
        for ir, row in enumerate(battle_state):
            for ic, cell in enumerate(row):
                if cell == 1:
                    return kill_boat(battle_state, ('abcd'[ic], ir + 1))

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
