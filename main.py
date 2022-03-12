
from random import choice as ch

import pygame.image

from poissicDisc import *


def redrawMap(points, SIZE, thickness, gamedisplay):
    for point in points:
        pygame.draw.circle(gamedisplay, (255, 255, 255), (point[1], point[0]), SIZE, thickness)


if __name__ == '__main__':
    satellite_image = pygame.image.load("images/Artboard 1.png")

    # Titles the game
    pygame.display.set_caption('Environmental Project')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    pointRadius = 1
    thickness = 5
    innerCircleRadius = 15
    outerCircleRadius = 20
    candidateSamples = 10

    gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    start = time.time()
    sampling = Sampling(50, 50, 500, 500, candidateSamples, innerCircleRadius, outerCircleRadius, gamedisplay, thickness, pointRadius)
    points = sampling.getPoints()
    print(f"Time: {time.time() - start}")

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
        gamedisplay.blit(satellite_image, satellite_image.get_rect())
        pygame.draw.polygon(gamedisplay, (0, 0, 0), [(723, 261), (863, 163), (873, 133), (794, 126), (705, 161)])

        # Drawing to the screen
        redrawMap(points, pointRadius, thickness, gamedisplay)
        sampling.draw(None, True)

        # Updating the display
        pygame.display.update()
