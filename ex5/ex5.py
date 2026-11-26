from random import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_grid(rows: int, cols: int, alive: float = 0.25):
    return [[1 if random() < alive else 0 for c in range(cols)] for r in range(rows)]

def is_alieve(grid, r: int, c: int):
    rows = len(grid)
    cols = len(grid[0])
    alive = 0

    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if (dr == 0 and dc == 0):
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                alive += grid[nr][nc]

    if alive == 3: return 1
    elif grid[r][c] and 2<= alive <= 3: return 1
    else: return 0

def generate(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0] * cols for r in range(rows)]

    for r in range(rows):
        for c in range(cols):
            new_grid[r][c] = is_alieve(grid, r, c)

    return new_grid

def run_game(rows: int = 40, cols: int = 60):
    global grid
    grid = create_grid(rows, cols)
    fig, ax = plt.subplots(figsize=(8, 6))

    img = ax.imshow(grid, cmap="binary_r")
    ax.set_xticks([])
    ax.set_yticks([])
    title = ax.set_title("Такт: 0")

    def update(frame):
        global grid
        if frame > 0:
            grid = generate(grid)
        img.set_data(grid)
        title.set_text(f"Такт: {frame}")
        return [img, title]

    FuncAnimation(fig, update)

    plt.tight_layout()
    plt.show()

run_game()