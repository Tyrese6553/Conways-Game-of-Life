import random

def random_state(width, height):
    board1 = []
    board2 = []

    for _ in range(width):
        value = random.choice([0,1])
        board1.append(value)
   
    for _ in range(height):
        board2.append(board1)

    return board2



'''
def render(board):
    new_board1 = []
    new_board2 = []

    for num in board:
        for nest in num:
            if nest == 0:
                new_board1.append(" ")
            if nest == 1:
                new_board1.append("#")

    return new_board1

board = [[1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0]]

print(render(board))
'''

    # use \n to print new line after each element from list