import random
def generate_maze(maze_size):
	maze = []
	for row in range(maze_size):
		blocks = []
		for col in range(maze_size):
			blocks.append(random.choice([0, 1]))
		maze.append(blocks)
	return maze


def get_maze_size():
	while True:
		size = input("Enter maze size: ")
		try:
			return int(size)
		except ValueError:
			print("Invalid size provided.")
			continue

maze_size = get_maze_size()
maze = generate_maze(maze_size)
