import numpy as np

# CCW rotation matrix by 90 degrees
R_90 = np.array([
    [0, -1],
    [1, 0]
])

cardinal_start = np.array([1, 0])  # East
cardinal_directions = [np.linalg.matrix_power(R_90, i) @ cardinal_start for i in range(4)]

diagonal_start = np.array([1, 1])  # Northeast
diagonal_directions = [np.linalg.matrix_power(R_90, i) @ diagonal_start for i in range(4)]

w = "XMAS"
wl = len(w)
dirs = cardinal_directions + diagonal_directions
print(dirs)

with open("input") as f:
    lines = f.read().strip().splitlines()
nx = len(lines)
ny = len(lines[0].strip())
grid = lines  # [line.strip().split() for line in lines]

is_start_of_word = lambda x, y: grid[x][y] == w[0]
start_positions = [(x, y) for x in range(nx) for y in range(ny) if is_start_of_word(x, y)]


def is_within_bounds(x, y, dir):
    d = wl - 1
    return not any([
        (dir[0] == 1 and x + d >= nx)
        or (dir[0] == -1 and x - d < 0)
        or (dir[1] == 1 and y + d >= ny)
        or (dir[1] == -1 and y - d < 0)
    ])


is_word = lambda x, y, d: all(grid[x + i * d[0]][y + i * d[1]] == w[i] for i in range(1, wl))
count_words = sum(is_within_bounds(x, y, d) and is_word(x, y, d) for x, y in start_positions for d in dirs)
print(count_words)
