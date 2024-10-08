from generate_maze import generateMaze, display_grid
from a_star import a_star_search
from utils import find_unblocked_cell, create_goal, print_path
from a_star_adaptive import adaptive_a_star_search
import time

NUMGRIDS = 50
gridList = [generateMaze() for _ in range(NUMGRIDS)]

# region Display_grids Demo

# start = find_unblocked_cell(gridList[0])
# goal = create_goal(start, gridList[0])
# print("start: ",start)
# display_grid(gridList[0]) #Display without start and goal
# display_grid(gridList[0], start=start) #Display with only start
# display_grid(gridList[0], goal=goal) #Display with only goal
# display_grid(gridList[0], start=start, goal=goal) #Display with both start and goal

#endregion

#region Simple Visualization and Path output

# demoGrid = [
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ['unblocked','unblocked','blocked','unblocked','unblocked'],
#              ['unblocked','unblocked','blocked','blocked','unblocked'],
#              ['unblocked','unblocked','blocked','blocked','unblocked'],
#              ['unblocked','unblocked','unblocked','blocked','unblocked']
#              ]
# demoStart = (4,2)
# demoGoal = (4,4)
# display_grid(demoGrid, start=demoStart, goal=demoGoal)
# demoPath = a_star_search(demoGrid, demoStart, demoGoal)
# print_path(demoPath, demoGoal)

#endregion

#region favorSmallG vs favorLargeG

# startTime = time.time()
# for grid in gridList:
#     start = find_unblocked_cell(grid)
#     goal = create_goal(start, grid)
#     a_star_search(grid, start, goal, favorSmallG = True)
# endTime = time.time()
# print("Average time for favor small G: ", (endTime-startTime)/NUMGRIDS)

# startTime = time.time()
# for grid in gridList:
#     start = find_unblocked_cell(grid)
#     goal = create_goal(start, grid)
#     a_star_search(grid, start, goal, favorSmallG = False)
# endTime = time.time()
# print("Average time for favor large G: ", (endTime-startTime)/NUMGRIDS)

#endregion

#region Effect of Ties Demo

# tieBreakerDemoGrid = [
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ['unblocked','unblocked','unblocked','unblocked','unblocked'],
#              ]
# tieBreakerDemoStart = (0,0)
# tieBreakerDemoGoal = (4,4)
# display_grid(tieBreakerDemoGrid, start=tieBreakerDemoStart, goal=tieBreakerDemoGoal)

# startTime = time.time()
# path1 = a_star_search(tieBreakerDemoGrid, tieBreakerDemoStart, tieBreakerDemoGoal, favorSmallG = True)
# endTime = time.time()
# print("Favor Small G Time: ", endTime- startTime)
# print("Favor Small G Final Path: ")
# print_path(path1, tieBreakerDemoGoal)
# startTime = time.time()
# path2 = a_star_search(tieBreakerDemoGrid, tieBreakerDemoStart, tieBreakerDemoGoal, favorSmallG = False)
# endtime = time.time()
# print("Favor Large G Time: ", endtime - startTime)
# print("Favor Large G Final Path: ")
# print_path(path2, tieBreakerDemoGoal)

#endregion

#region forward vs backward A*

# startTime = time.time()
# for grid in gridList:
#     start = find_unblocked_cell(grid)
#     goal = create_goal(start, grid)
#     a_star_search(grid, start, goal) #Forward A*
# endTime = time.time()
# print("Average time for forward A*: ", (endTime-startTime)/NUMGRIDS)

# startTime = time.time()
# for grid in gridList:
#     start = find_unblocked_cell(grid)
#     goal = create_goal(start, grid)
#     a_star_search(grid, goal, start) #Backward A*
# endTime = time.time()
# print("Average time for backward A*: ", (endTime-startTime)/NUMGRIDS)

#endregion

#region Adaptive A*

# cnt = 0
# improvment = 0
# for grid in gridList:
#     print("Grid ", cnt)
#     AdaptiveGoal = find_unblocked_cell(grid)
#     times = adaptive_a_star_search(grid, AdaptiveGoal, 50, printOnlyFirstLast=True) #Runs Adaptive A* 500 times on first grid in gridList
#     improvment += times[0] - times[1]
#     cnt += 1
# averageImprovement = improvment / NUMGRIDS
# print("Average Improvment: ", averageImprovement)

#endregion