import random

def dead_state(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]


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
    return board2, width, height


def render(board):
    print("-----------------------")
    for sub in board:
        # .join joins a list together with a separator = ""
        # It compacts the list elements together based on the separator
        new_board = "".join(["#" if num == 1 else " " for num in sub])
        print(f"|{new_board}|")
    print("-----------------------")
    

def next_board_state(init_board, width, height):
    '''
    **Used for testing**
    init_board = [
        [0,1,1],
        [1,1,0],
        [0,1,1]
    ]
    width = 3
    height = 3
    '''
    new_state = dead_state(width, height)
    

    for x in range(0, height):
        for y in range(0, width):
            # Initialises variable for each cell being checked
            live_neighbours = 0
            # Checks the cells around main cell
            for x1 in range((x-1), (x+2)):
                if x1 < 0 or x1 >= height:
                    continue
                for y1 in range((y-1), (y+2)):
                    if y1 < 0 or y1 >= width:
                        continue
                    if x1 == x and y1 == y:
                        continue
                    
                    if init_board[x1][y1] == 1:
                        live_neighbours += 1
            # Looks at the current cell and determines the results based on the rules
            if init_board[x][y] == 1:
                if live_neighbours <= 1 or live_neighbours > 3:
                    new_state[x][y] = 0
                else:
                    new_state[x][y] = 1
            elif new_state[x][y] == 0:
                if live_neighbours == 3:
                    new_state[x][y] = 1
                else:
                    new_state[x][y] = 0

    return new_state
                
