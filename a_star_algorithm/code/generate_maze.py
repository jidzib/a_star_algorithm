import random
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import numpy as np
from utils import GRID_SIZE, DIRECTION, can_generate_here, find_unblocked_cell

def generateMaze():
    grid = [['unvisited' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    while any('unvisited' in row for row in grid): 
        unvisited_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 'unvisited']
        start_x, start_y = random.choice(unvisited_cells)
        grid[start_x][start_y] = 'unblocked'

        stack = [(start_x, start_y)]

        while stack:
            current_x, current_y = stack[-1]
            neighbors = [(current_x + dx, current_y + dy) for dx, dy in DIRECTION if can_generate_here(current_x + dx, current_y + dy, grid)]

            if neighbors:
                next_x, next_y = random.choice(neighbors)

                if random.random() < 0.7:
                    grid[next_x][next_y] = 'unblocked'
                else:
                    grid[next_x][next_y] = 'blocked'

                stack.append((next_x, next_y))
            else:
                stack.pop()

    return grid

def display_grid(grid, start=None, goal=None, cell_size=0.1):
    color_mapping = {
        'blocked': [0, 0, 0],        # black
        'unblocked': [255, 255, 255],      # white
        'start': [0, 255, 0],          # green
        'goal': [255, 0, 0]            # red
    }
    
    rgb_grid = np.array([[color_mapping['blocked'] if cell == 'blocked' else color_mapping['unblocked'] for cell in row] for row in grid])

    if start is not None:
        rgb_grid[start[0]][start[1]] = color_mapping['start']  # Mark the start cell with green
    if goal is not None:
        rgb_grid[goal[0]][goal[1]] = color_mapping['goal']  # Mark the goal cell with red

    plt.figure(figsize=(len(grid[0]) * cell_size, len(grid) * cell_size))
    plt.imshow(rgb_grid, origin='upper')

    plt.show()