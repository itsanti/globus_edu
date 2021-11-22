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
            n2_cells.append((len(board) - 1, 0))
            board[n2_cells[0][0]][n2_cells[0][1]] = 1
        else:
            n2_cells.append((len(board) - 1, 1))
            boats_position.append(n2_cells)
            n2_cells = []

    boats_position.append([(0, 0)])
    if n1 >= 2:
        boats_position.append([(0, len(board[0]) - 1)])
        if n1 == 3:
            boats_position.append([(len(board) - 1, len(board[0]) - 1)])

    return format_positions(boats_position)


def format_positions(boats_position):
    result = []
    for boat in boats_position:
        if len(boat) > 1:
            for ix, cell in enumerate(boat):
                boat[ix] = ('abcd'[cell[1]], cell[0] + 1)
        else:
            boat = [('abcd'[boat[0][1]], boat[0][0] + 1)]
        result.append(boat)
    return result


if __name__ == '__main__':
    print(start_boats_position((3, 1)))
    #print(start_boats_position((3, 0)))

