# Conway's Game of Life in Python

This is the famous Game of Life program, where you can watch hundreds of generations. If you would like to read more about this game, you can click [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). It's quite an interesting read and if you also want to make this program, I would recommend reading up on it as well, it will give a good understanding on how it works. I would stick to the basics of the game as it can become complex.

If you want to create this program but need some guidance like myself, you can check out [Robert Heaton's blog](https://robertheaton.com/2018/07/20/project-2-game-of-life/), there are some good reads and advanced beginner guided projects.

## How it Works

* The user is asked for a width and a height. Together, these variables make up the board that is used. This is the only input that will be asked.
* A board is made up of random numbers, each cell is 1 or 0, alive or dead respectively. This is the initial board that starts the process of life. This is considered the first generation.
* The initial board is displayed.
* Initial board is then passed into the `next_board_state` function, next state is calculated, returned and displayed. The next state is considered the second generation.
* The next state from the above process is used to create the third generation, the third generation will then be used to create the forth, and so on.
* The program loops endlessly. The larger the board, the more eventful the future generations will typically be.

## Challenges

The most challenging part was the `next_board_state` function. The best way I found to understand it is by visualising the board, I mean literally, open any drawing application and make up a random board and label the x and y axes. Try to figure out the coordinates of the cells around your chosen cell, this helped me immensely.

The input is the initial board that is created randomly from the `random_state` and it is then passed to the `next_board_state` function as an argument. The width and height will be unknown as I prefer the user input these values, this allows you test different volumes to see how population density plays a part. We use the `dead_state` function to generate a template of dead cells, this serves as our next state and will be returned at the end of the function after going through all the rules.

The function iterates over each value within the list, that is the purpose of the first two `for` loops. The second set of `for` loops checks the cells around the current cell. This is done by using a `range` function and the current values of `x` and `y`, the board is treated similarly to a cartesian plane. Within the loop, if-statements are used to ensure we don't go out of the board and create an `IndexError` and to ensure we don't include the current cell that is being checked. If we find that the cell is alive, meaning it is equal to one, we add one to the `live_neighbours` variable which serves as a counter.

After the cells around the current cell is checked, it now goes to the rules, which is a few conditions. Below are the rules for the game of life:

* **Underpopulation**: Any live cell with fewer than two live neighbours dies.
* **Survival**: Any live cell with two or three live neighbours lives on to the next generation.
* **Overpopulation**: Any live cell with more than three live neighbours dies.
* **Reproduction**: Any dead cell with exactly three live neighbours becomes a live cell.

Once these rules are applied and the next state is adjusted. It then loops over to the next cell and the above process is done again until the end of the list.

## Modules

All modules used are found in the Python Standard Library and do not require separate installation:

* time
* sys
* os
* random



