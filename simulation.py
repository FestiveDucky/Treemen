import pygame.sprite
import random



class Plot:
    def __init__(self, vertices):
        self.vertices = vertices


class Simulation:
    def __init__(self):
        self.plots = []
        self.plots_group = pygame.sprite.Group()

    def get_plots(self):
        return self.plots