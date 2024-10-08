import numpy as np
import heapq
import time
from generate_maze import generateMaze
from utils import *

def a_star_search(grid, start, goal, favorSmallG = True, print = False):

    closed_list = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))] # popped cells
    cell_details = [[Cell() for _ in range(len(grid[0]))] for _ in range(len(grid))] # list of all cells with information

    i, j = start[0], start[1]
    cell_details[i][j].h = heuristic(i,j,goal)
    cell_details[i][j].f = cell_details[i][j].h
    cell_details[i][j].g = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    open_list = []
    heapq.heappush(open_list, (cell_details[i][j].f, 0.0, i, j)) # cells to be visited (f value, g value, row ,column)

    found_destination = False

    while open_list:
        p = heapq.heappop(open_list) # pops smallest f value cell then by g value

        i = p[2] 
        j = p[3]
        closed_list[i][j] = True
        if (is_goal(i, j, goal)):
            if print:
                print("Agent has arrived at the goal")
            return cell_details

        for dir in DIRECTION:
            new_i = i + dir[0]
            new_j = j + dir[1]
            g_new = cell_details[i][j].g + 1.0
            h_new = heuristic(new_i, new_j, goal)
            f_new = g_new + h_new  
            if is_valid(grid, new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:

                if is_goal(new_i, new_j, goal):
                    found_destination = True                      
                if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                    cell_details[new_i][new_j].parent_i = i
                    cell_details[new_i][new_j].parent_j = j 
                    cell_details[new_i][new_j].f = f_new
                    cell_details[new_i][new_j].g = g_new
                    cell_details[new_i][new_j].h = h_new
                    # Add the cell to the open list
                    if favorSmallG:
                        heapq.heappush(open_list, (f_new, g_new, new_i, new_j))
                    else:
                        heapq.heappush(open_list, (f_new, -g_new, new_i, new_j))

    # Goal is not found after visiting all cells
    if not found_destination:
        if print:
            print("Failed to find the destination cell") 
        return None
