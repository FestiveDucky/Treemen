import pygame.image
from simulation import *
from menu1 import *
from menu2 import *
from sampling import *

BLUE = (10, 23, 57)


def finished_sim(sim_num, display):
    font = pygame.font.SysFont('Cambria', 75)
    current_simulation = \
    [["Base", (900, 400), (1050, 475)], ["Cutting", (810, 400), (1050, 475)], ["Planting", (770, 400), (1050, 475)]][
        sim_num - 1]
    completed_sim_text1 = font.render(f'{current_simulation[0]} Tree Simulation', True, BLUE)
    completed_sim_text2 = font.render('Completed', True, BLUE)
    display.blit(completed_sim_text1, current_simulation[1])
    display.blit(completed_sim_text2, current_simulation[2])


def create_key(display):
    image = pygame.image.load("images/key images.png")
    font = pygame.font.SysFont('Cambria', 60)
    acorn_text1 = font.render('- 1000 Acorns', True, BLUE)
    tree_text = font.render('- 1 Oak Tree ', True, BLUE)
    display.blit(image, (20, 200))
    display.blit(tree_text, (180, 435))
    display.blit(acorn_text1, (180, 245))


def side_screen(current_simulation, total_years, display, sim_num):
    font = pygame.font.SysFont('Cambria', 75)
    current_simulation_display1 = font.render(f'{["Base", "Cutting", "Planting"][sim_num - 1]} Tree', True, BLUE)
    current_simulation_display2 = font.render('Simulation', True, BLUE)
    year_display = font.render(f'Year| {current_simulation.year + 1}/{total_years}', True, BLUE)
    average_trees_display1 = font.render('Average Trees', True, BLUE)
    average = round(current_simulation.average_trees_alive / (current_simulation.year + 1), 2)
    if len(str(average)) > 5: average = round(average, 1)
    average_trees_display2 = font.render(f'Per Year| {average}', True, BLUE)
    tree_display = font.render(f'Trees Alive| {len(current_simulation.trees)}', True, BLUE)
    display.blit(current_simulation_display1, (20, 20))
    display.blit(current_simulation_display2, (20, 95))
    display.blit(average_trees_display1, (20, 575))
    display.blit(average_trees_display2, (20, 650))
    display.blit(tree_display, (20, 800))
    display.blit(year_display, (20, 950))
    create_key(display)


def redrawMap(points, SIZE, thickness, gamedisplay):
    for point in points:
        pygame.draw.circle(gamedisplay, (255, 255, 255), (point[1], point[0]), SIZE, thickness)


def create_sim(years_long, death_rate, sim_type, num_trees):
    simulation = Simulation(years_long, death_rate, sim_type)
    sampling = Sampling(700, 100, 1850, 1000, 20, 75, 85, 5, 1, simulation, num_trees)
    # We want the lists to be linked in the memory
    sampling.available_points = sampling.points
    return simulation, sampling


if __name__ == '__main__':
    pygame.init()

    satellite_image = pygame.image.load("images/map final modified.png")

    # Titles the game
    pygame.display.set_caption('Environmental Project')
    clock = pygame.time.Clock()

    WIDTH = 1920
    HEIGHT = 1080

    years = 1000

    gamedisplay = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

    num_starting_trees, natural_death_rate, num_trees_planted, percent_trees_cut = show_menu1(WIDTH, HEIGHT, gamedisplay)
    percent_trees_cut /= 100

    base_simulation, base_sampling = create_sim(years, natural_death_rate, 1, num_starting_trees)
    cut_simulation, cut_sampling = create_sim(years, natural_death_rate, 2, num_starting_trees)
    cut_simulation.trees_to_cut = percent_trees_cut
    plant_simulation, plant_sampling = create_sim(years, natural_death_rate, 3, num_starting_trees)
    plant_simulation.trees_to_plant = num_trees_planted
    plant_simulation.trees_to_plant_save = num_trees_planted

    simulations = [base_simulation, cut_simulation, plant_simulation]

    current_sim = 1

    average_trees = []
    final_tree_count = []

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

        # Side screen
        side_screen(simulations[current_sim - 1], years, gamedisplay, current_sim)

        previous_sim = current_sim

        # Running the planting simulation
        if current_sim == PLANTING:
            plant_simulation.get_trees_group().draw(gamedisplay)
            current_sim = plant_simulation.one_year(gamedisplay)

        # Running the cutting simulation
        if current_sim == CUTTING:
            cut_simulation.get_trees_group().draw(gamedisplay)
            current_sim = cut_simulation.one_year(gamedisplay)

        # Running the base simulation
        if current_sim == BASE:
            base_simulation.get_trees_group().draw(gamedisplay)
            current_sim = base_simulation.one_year(gamedisplay)

        if previous_sim != current_sim:
            final_tree_count.append(len(simulations[previous_sim - 1].trees))
            average_trees.append(round(simulations[previous_sim - 1].average_trees_alive / years, 2))
            finished_sim(previous_sim, gamedisplay)
            pygame.display.update()
            time.sleep(3)

        # Updating the display
        pygame.display.update()
        if current_sim > PLANTING:
            # Go to end screen
            gameRunning = False

    show_menu2(gamedisplay, average_trees, final_tree_count)
