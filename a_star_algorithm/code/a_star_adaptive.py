import numpy as np
import heapq
import time
from generate_maze import generateMaze, find_unblocked_cell, display_grid
from utils import *



def adaptive_a_star_search(grid, goal, n, favorSmallG = True, printOnlyFirstLast = False ):

    cell_details = [[Cell() for _ in range(len(grid[0]))] for _ in range(len(grid))] # list of all cells with information
    firstStart = find_unblocked_cell(grid)
    times = [0, 0]
    for runNum in range(n):
        start_time = time.time()
        closed_list = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))] # popped cells
        
        if runNum == 0 or runNum == n-1:
            start = firstStart
        else:
            start = create_goal(goal, grid)

        i, j = start[0], start[1]
        h_start = heuristic(i, j, goal) if cell_details[i][j].h_star is None else cell_details[i][j].h_star
        cell_details[i][j].h = h_start
        cell_details[i][j].f = h_start
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
                end_time = time.time()
                totalTime = end_time - start_time
                if (runNum == 0):
                    times[0] = totalTime
                elif (runNum == n-1):
                    times[1] =  totalTime
                if not printOnlyFirstLast or (runNum == 0 or runNum == n - 1):
                    print("Agent has arrived at the goal")
                    print("Runtime ", runNum , " : ", totalTime)
                found_destination = True
                break
            
            for dir in DIRECTION:
                new_i = i + dir[0]
                new_j = j + dir[1]
                if is_valid(grid, new_i, new_j) and is_unblocked(grid, new_i, new_j) and not closed_list[new_i][new_j]:
                    g_new = cell_details[i][j].g + 1.0
                    h_new = heuristic(new_i, new_j, goal) if cell_details[new_i][new_j].h_star is None else cell_details[new_i][new_j].h_star
                    f_new = g_new + h_new 
                        
                    if cell_details[new_i][new_j].f == float('inf') or cell_details[new_i][new_j].f > f_new:
                        cell_details[new_i][new_j].f = f_new
                        cell_details[new_i][new_j].g = g_new
                        cell_details[new_i][new_j].h = h_new
                        cell_details[new_i][new_j].parent_i = i
                        cell_details[new_i][new_j].parent_j = j
                        # Add the cell to the open list
                        if favorSmallG:
                            heapq.heappush(open_list, (f_new, g_new, new_i, new_j))
                        else:
                            heapq.heappush(open_list, (f_new, -g_new, new_i, new_j))

        # Goal is not found after visiting all cells
        cell_details = update_adaptive_heuristics(cell_details, goal, closed_list)
        if not found_destination:
            end_time = time.time()
            totalTime = end_time - start_time
            if (runNum == 0):
                times[0] = totalTime
            elif (runNum == n-1):
                times[1] =  totalTime

            if not printOnlyFirstLast or (runNum == 0 or runNum == n - 1):
                print("Failed to find the destination cell") 
                print("Runtime ", runNum , " : ", totalTime)
    return times 
            
def update_adaptive_heuristics(cell_details, goal, closed_list):
    """ Update the adaptive heuristic h* after finding the goal. """
    goal_i, goal_j = goal[0], goal[1]
    g_goal = cell_details[goal_i][goal_j].g
    if (g_goal != float('inf')):
        for i in range(len(cell_details)):
            for j in range(len(cell_details[0])):
                cell_details[i][j].f = float('inf')
                if cell_details[i][j].g != float('inf') and closed_list[i][j] == True:
                    cell_details[i][j].h_star = g_goal - cell_details[i][j].g
    return cell_details

