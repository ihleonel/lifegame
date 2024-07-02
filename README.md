# Lifegame
## Description

Initially, there is a grid with some cells which may be alive or dead. Our task is to generate the next generation of cells based on the following rules:

1. Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
