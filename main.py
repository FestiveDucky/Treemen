from random import choice as ch

import pygame.image
from simulation import *

from sampling import *


def redrawMap(points, SIZE, thickness, gamedisplay):
    for point in points:
        pygame.draw.circle(gamedisplay, (255, 255, 255), (point[1], point[0]), SIZE, thickness)

# Variables - Death rate percentage, average household size (default = 3), number of acorns

# TODO add key
if __name__ == '__main__':
    pygame.init()

    satellite_image = pygame.image.load("images/Artboard 1.png")

    # Titles the game
    pygame.display.set_caption('Environmental Project')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    years = 200

    gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    simulation = Simulation(years)

    start = time.time()
    sampling = Sampling(700, 100, 1850, 1000, 20, 100, 110, 5,
                        1, simulation)

    # We want the lists to be linked in the memory
    sampling.available_points = sampling.points
    print(f"Time: {time.time() - start}")

    end_first_sim = False

    FPS = 20
    gameRunning = True
    a = []
    while gameRunning:
        clock.tick(FPS)
        # Checking events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                gameRunning = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                print(e.pos)
                a.append(e.pos)
                print(a)


        # Clearing the display
        gamedisplay.fill((0, 0, 0))
        gamedisplay.blit(satellite_image, satellite_image.get_rect())

        # Drawing to the screen
        simulation.get_trees_group().draw(gamedisplay)
        print(len(simulation.trees))

        # Running the simulation
        if not end_first_sim:
            end_first_sim = simulation.one_year(gamedisplay)

        # Updating the display
        pygame.display.update()
        # time.sleep(5)
