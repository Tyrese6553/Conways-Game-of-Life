import random

def random_state(width, height):
    board1 = []
    board2 = []
    dead_alive = [0,1]

    for _ in range(width):
        value = random.choice(dead_alive)
        board1.append(value)
        board2.append(board1)

    return board2



