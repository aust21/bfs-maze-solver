from maze import maze
from collections import deque
import matplotlib.pyplot as plt


def search_bfs(maze, start, end):
	columns, rows = len(maze), len(maze[0])
	queue = deque([(start, [start])])
	visited_nodes = set()

	# immediately return if starting position is on an obstacle
	if maze[start[0]][start[1]] == 1:
		return None

	while queue:
		current_node, path = queue.popleft()

		if current_node == end:
			return path

		if current_node in visited_nodes:
			continue

		visited_nodes.add(current_node)
		row, col = current_node  # row, col
		neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

		for neighbor in neighbors:
			neighbor_row, neighbor_col = neighbor
			# neighbor_xcor in range(0, rows + 1) and neighbor_ycor in range(0, columns + 1)
			if neighbor_row in range(0, rows) and neighbor_col in range(0, columns) and \
						maze[neighbor_row][neighbor_col] != 1 and neighbor not in visited_nodes:
				queue.append((neighbor, path + [neighbor]))
	return None


def visualize_path(maze, path):
	if not path:
		return 
	plt.imshow(maze, cmap='viridis', origin='upper', interpolation='nearest')
	for coordinate in path:
		plt.text(coordinate[1], coordinate[0], 'X', ha='center', va='center', color='red', fontsize=8)
	plt.show()


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

# maze = [
# [0, 0, 1, 0, 1],
# [1, 0, 0, 0, 1],
# [0, 0, 1, 1, 0],
# [0, 0, 1, 1, 0],
# [1, 1, 0, 1, 1],
# ]

path = search_bfs(maze, start, end)
visualize_path(maze, path)
print(display_results(path, maze))