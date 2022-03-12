import pygame, os, sys, time
from random import choice as ch
from poissicDisc import *


def redrawMap(points, SIZE, thickness, gamedisplay):
    for point in points:
        pygame.draw.circle(gamedisplay, (255, 255, 255), (point[1], point[0]), SIZE, thickness)


if __name__ == '__main__':

    fullscreen = False
    move = False

    # Titles the game
    pygame.display.set_caption('Sampling')
    clock = pygame.time.Clock()

    if fullscreen:
        WIDTH = 1920
        HEIGHT = 1080
    else:
        WIDTH = 1001
        HEIGHT = 560

    pointRadius = 1
    thickness = 5
    innerCircleRadius = 10
    outerCircleRadius = 15
    candidateSamples = 20

    if move:
        x = 1920
        y = 30
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

    if fullscreen:
        gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    else:
        gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT))

    start = time.time()
    sampling = Sampling(50, 50, 500, 500, candidateSamples, innerCircleRadius, outerCircleRadius, gamedisplay, thickness, pointRadius)
    points = sampling.getPoints()
    print(points)
    print(f"Time: {time.time() - start}")
    # 222.17 (10)
    # 108.41 (5)

    FPS = 20
    gameRunning = True

    while gameRunning:
        clock.tick(FPS)
        # Checking events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                gameRunning = False

        # Clearing the display
        gamedisplay.fill((0, 0, 0))

        # Drawing to the screen
        redrawMap(points, pointRadius, thickness, gamedisplay)
        sampling.draw(None, True)

        # Updating the display
        pygame.display.update()
