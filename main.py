import time
from random import choice as ch

import pygame.image
from simulation import *

from sampling import *


def redrawMap(points, SIZE, thickness, gamedisplay):
    for point in points:
        pygame.draw.circle(gamedisplay, (255, 255, 255), (point[1], point[0]), SIZE, thickness)


def create_sim(years_long, death_rate, sim_type, num_trees):
    simulation = Simulation(years_long, death_rate, sim_type)
    sampling = Sampling(700, 100, 1850, 1000, 20, 75, 85, 5,
                             1, simulation, num_trees)
    # We want the lists to be linked in the memory
    sampling.available_points = sampling.points
    return simulation, sampling


# TODO add key, current year, shows titles to them before they run, redo border points for more accuracy
if __name__ == '__main__':
    pygame.init()

    satellite_image = pygame.image.load("images/map final modified.png")

    # Titles the game
    pygame.display.set_caption('Environmental Project')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    # TODO maybe add offspring var
    num_trees_planted = 30
    percent_trees_cut = 0.5
    num_starting_trees = 20
    natural_death_rate = 5

    years = 100

    gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    base_simulation, base_sampling = create_sim(years, natural_death_rate, 1, num_starting_trees)
    cut_simulation, cut_sampling = create_sim(years, natural_death_rate, 2, num_starting_trees)
    cut_simulation.trees_to_cut = percent_trees_cut
    plant_simulation, plant_sampling = create_sim(years, natural_death_rate, 3, num_starting_trees)
    plant_simulation.trees_to_plant = num_trees_planted
    plant_simulation.trees_to_plant_save = num_trees_planted

    end_plant_sim = False
    end_cut_sim = False
    end_base_sim = False

    FPS = 20
    gameRunning = True
    a = []
    start = time.time()
    while gameRunning:
        clock.tick(FPS)
        # Checking events
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                gameRunning = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                # TODO remove for final
                print(e.pos)
                a.append(e.pos)
                print(a)

        # Clearing the display
        gamedisplay.fill((0, 0, 0))
        gamedisplay.blit(satellite_image, satellite_image.get_rect())

        # Running the plating simulation
        if end_cut_sim and not end_plant_sim:
            plant_simulation.get_trees_group().draw(gamedisplay)
            end_plant_sim = plant_simulation.one_year(gamedisplay)
            if end_plant_sim:
                time.sleep(3)
                print("------------------------------")
                print(f"Planting simulation ran for {time.time() - start} seconds!")

        # Running the cutting simulation
        if end_base_sim and not end_cut_sim:
            cut_simulation.get_trees_group().draw(gamedisplay)
            end_cut_sim = cut_simulation.one_year(gamedisplay)
            if end_cut_sim:
                time.sleep(3)
                print("------------------------------")
                print(f"Cutting simulation ran for {time.time() - start} seconds!")
                start = time.time()

        # Running the base simulation
        if not end_base_sim:
            base_simulation.get_trees_group().draw(gamedisplay)
            end_base_sim = base_simulation.one_year(gamedisplay)
            if end_base_sim:
                time.sleep(3)
                print("------------------------------")
                print(f"Base simulation ran for {time.time() - start} seconds!")
                start = time.time()

        # Updating the display
        pygame.display.update()
        if end_plant_sim:
            # Go to end screen
            gameRunning = False
