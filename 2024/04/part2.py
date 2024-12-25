diag1 = [(1, 1), (-1, -1)]

diag2 = [(1, -1), (-1, 1)]

with open("input") as f:
    grid = f.read().strip().splitlines()

n = len(grid)

starts = [(x, y) for x in range(1, n - 1) for y in range(1, n - 1) if grid[x][y] == "A"]
crosses = sum(
    all(
        set(grid[x + dx][y + dy] for dx, dy in diag) == {"M", "S"}
        for diag in (diag1, diag2)
    )
    for x, y in starts
)
print(crosses)
