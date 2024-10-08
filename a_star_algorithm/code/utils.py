import random

DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1), ]  # North, East, South, West
GRID_SIZE = 101

class Cell:
    def __init__(self):
        self.parent_i = 0  # parent cell row index
        self.parent_j = 0  # parent cell column index
        self.f = float('inf')  # total cost of the cell (g + h)
        self.g = float('inf')  # cost from start to this cell
        self.h = 0  # heuristic cost from this cell to destination
        self.h_star = None

def heuristic(row, column, goal):
    return abs(row - goal[0]) + abs(column - goal[1]) # manhattan distance to calculate heuristic value

def is_valid(grid, row, column):
    return (row >= 0) and (row < len(grid)) and (column >= 0) and (column < len(grid[0])) # used to make sure the agent's move is within the bounds of the grid

def is_unblocked(grid, row, column): # check if the agent is running into a blocked cell, return True if not
    return grid[row][column] == 'unblocked'

def is_goal(row, column, goal): # check if the agent is on the goal cell
    return row == goal[0] and column == goal[1]

def print_path(cell_details, goal):
    if cell_details is None:
        return
    print("Path: ")
    path = []
    row, column = goal[0], goal[1]

    while not (cell_details[row][column].parent_i == row and cell_details[row][column].parent_j == column):
        path.append((row, column))
        temp_row = cell_details[row][column].parent_i
        temp_col = cell_details[row][column].parent_j
        row = temp_row
        column = temp_col

    path.append((row, column))
    path.reverse()

    for i in path:
        print("->", i, end=" ")
    print()
    return path

def find_unblocked_cell(grid):
    """Find a random unblocked cell in the grid."""
    while True:
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == 'unblocked':
            return (x, y)
        
def can_generate_here(x, y, grid):
    """Check if the cell (x, y) is within bounds and unvisited."""
    return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and grid[x][y] == 'unvisited'

def create_goal(start, grid):
    while True:
        goal = find_unblocked_cell(grid)
        if goal != start:
            return goal
