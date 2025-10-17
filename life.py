def dead_state(width, height=0):
    board1 = []
    board2 = []

    # For width
    for _ in range(width):
        board1.append(0)
        board2.append(board1)

    return board2


    
print(dead_state(5))

    # [
    # [0,0,0,0,0], 
    # [0,0,0,0,0]
    # ]