'''
    # функция начальной расстановки кораблей 1-палубных и 2-х палубных
    how_many_boats - tuple n1 n2
    n1 - Однопалубные, n2 - двухпалубные
    для поля 4*4: 1 <= n1 <= 3; 0 <= n2 <= 1
    разрешим кораблям касаться углами друг друга. Но не стоять впритык сторонами.
    return - [([a,b,c,d], [1-4]), (...)] Описания кораблей могут идти в любом порядке.
'''
import random


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
                if row * c == 0:
                    if 0 <= cell[0] + row < len(board) and 0 <= cell[1] + c < len(board[0]):
                        board[cell[0] + row][cell[1] + c] = 1
    return board


def select_random_cell(board, part_cell=None):
    if part_cell is None:
        row = random.randrange(len(board))
        cell = random.randrange(len(board[0]))
        print(board)
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


if __name__ == '__main__':
    print(start_boats_position((3, 1)))
    #print(start_boats_position((3, 0)))

