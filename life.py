import random

def random_state(width, height):
    board2 = []

    for _ in range(height):
        # Initialises board1 again so it resets the values in the list
        # This allows each sublist to be random and not the same set each time
        board1 = []
        for _ in range(width):
            value = random.choice([0,1])
            board1.append(value)
        board2.append(board1)

    return board2

