import random

def random_state(width, height):
    board1 = []
    board2 = []

    for _ in range(width):
        value = random.choice([0,1])
        board1.append(value)
        board2.append(board1)

    return board2


print(random_state(5,5))
