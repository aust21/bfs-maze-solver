from maze import maze
from collections import deque
import matplotlib.pyplot as plt
import algorithm

def display_results(path, maze):
	if path:
		return f"shortest path is {path}"

	print("Here's the generated maze:\n")
	for row in maze:
		print(row)
	return "Sorry there is no path found."


# can change values 
start = (0, 0)
end = (2, 0)

path = algorithm.search_bfs(maze, start, end)
algorithm.visualize_path(maze, path)
print(display_results(path, maze))