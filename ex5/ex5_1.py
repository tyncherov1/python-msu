import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def evolve_grid(rows, cols, alive = 0.25):
    grid = (np.random.rand(rows, cols) < alive).astype(np.int8)
    while True:
        yield grid
        frame_grid = np.pad(grid, 1)
        child = np.zeros((rows, cols), np.int8)
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                child += np.roll(frame_grid, (i, j), (0, 1))[1:-1, 1:-1]
        grid = ((child == 3) | ((grid == 1) & (child == 2))).astype(np.int8)
                

def run_game(rows: int = 40, cols: int = 60):
    grid = evolve_grid(rows, cols)
    fig, ax = plt.subplots(figsize=(8, 6))

    img = ax.imshow(next(grid), cmap=plt.cm.binary_r)
    ax.set_xticks([])
    ax.set_yticks([])
    title = ax.set_title("Такт: 0")

    def update(frame):
        nonlocal grid
        img.set_data(next(grid))
        title.set_text(f"Такт: {frame}")
        return [img, title]

    FuncAnimation(fig, update)

    plt.tight_layout()
    plt.show()

run_game()
