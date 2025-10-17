def dead_state(width, height):
    board1 = []
    board2 = []

    # For width
    for _ in range(width):
        board1.append(0)


    for _ in range(height):
        board2.append(board1)

    return board2


    
print(dead_state(2,2))

    # [
    # [0,0,0,0,0], 
    # [0,0,0,0,0]
    # ]