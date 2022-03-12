import pygame.sprite
import random
plot_vertices = {1: [(723, 261), (863, 163), (873, 133), (794, 126), (705, 161)], 2: [], 3: [], 4: [], 5: [], 6: [],
                 7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [],
                 15: [], 16: [], 17: [], 18: [], 19: [], 20: []}


class Plot:
    def __init__(self, vertices):
        self.vertices = vertices
        aidaowijdawoidj


class Simulation:
    def __init__(self):
        self.plots = []
        self.plots_group = pygame.sprite.Group()

    def get_plots(self):
        return self.plots