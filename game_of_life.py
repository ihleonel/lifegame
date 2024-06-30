# -*- coding:utf-8 -*-
""" Game of Life """
import time
import pygame
import numpy as np

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25

screen.fill(bg)

NXC, NYC = 50, 50

DIM_CW = width / NXC
DIM_CH = height / NYC

gameState = np.zeros((NXC, NYC))

PAUSE_GAME = False
RESTAR_GAME = False
VELOCITY_GAME = 0.2

while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    time.sleep(VELOCITY_GAME)

    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_p:
                PAUSE_GAME = not PAUSE_GAME
            elif event.key == pygame.K_r:
                RESTAR_GAME = True

        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX = int(np.floor(posX / DIM_CW))
            celY = int(np.floor(posY / DIM_CH))
            newGameState[celX, celY] = not mouseClick[2]
    for y in range(0, NXC):
        for x in range(0, NYC):
            if PAUSE_GAME:
                n_neigh = (
                    gameState[(x - 1) % NXC, (y - 1) % NYC] +
                    gameState[x % NXC, (y - 1) % NYC] +
                    gameState[(x + 1) % NXC, (y-1) % NYC] +
                    gameState[(x - 1) % NXC, y % NYC] +
                    gameState[(x + 1) % NXC, y % NYC] +
                    gameState[(x - 1) % NXC, (y+1) % NYC] +
                    gameState[x % NXC, (y + 1) % NYC] +
                    gameState[(x + 1) % NXC, (y + 1) % NYC]
                )
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
            if RESTAR_GAME:
                newGameState = np.zeros((NXC, NYC))
                RESTAR_GAME = not RESTAR_GAME
                PAUSE_GAME = False

            poly = [
                (x * DIM_CW, y * DIM_CH),
                ((x + 1) * DIM_CW, y * DIM_CH),
                ((x + 1) * DIM_CW, (y + 1) * DIM_CH),
                (x * DIM_CW, (y + 1) * DIM_CH)
            ]
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()
