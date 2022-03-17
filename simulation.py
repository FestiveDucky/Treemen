import pygame.sprite
from random import choice as ch, randint as ri


BASE = 1
CUTTING = 2
PLANTING = 3

tree_image = pygame.image.load("images/trees2-02.png")


class Tree(pygame.sprite.Sprite):
    def __init__(self, master, group, coords, cell):
        super().__init__(group)
        self.master = master
        self.coords = coords
        self.cell = cell
        # self.image = pygame.Surface((15, 15))
        # self.image.fill((255, 0, 0))
        self.image = tree_image
        self.rect = self.image.get_rect(centerx=self.coords[1], centery=self.coords[0])

    def delete(self):
        self.master.available_cells[self.cell] = self.master.cells[self.cell]
        self.master.cells[self.cell].remove_point()
        self.master.points.remove(self.coords)


class Simulation:
    def __init__(self, total_years, natural_death_rate, sim_type):
        self.trees = {}
        self.trees_group = pygame.sprite.Group()
        self.year = 0
        self.sampling = None
        self.average_trees_alive = 0
        self.total_years = total_years
        self.natural_death_rate = natural_death_rate
        # 1 = base, 2 = cutting, 3 = planting
        self.sim_type = sim_type
        self.trees_to_plant = 0
        self.trees_to_plant_save = 0
        self.trees_to_cut = 0

    def one_year(self, gamedisplay):
        self.year += 1
        self.average_trees_alive += len(self.trees)

        remove = []
        for tree in self.trees:
            num = ri(1, 100)
            if num <= self.natural_death_rate:
                if self.trees_to_plant == 0:
                    self.trees[tree].delete()
                    self.trees[tree].kill()
                    remove.append(tree)
                else:
                    self.trees_to_plant -= 1

        for coords in remove:
            self.trees.pop(coords)

        if self.year % 4 == 0:
            trees_to_add = []
            for tree in self.trees:
                self.sampling.outer_circle_radius = ri(60, 120)
                self.sampling.inner_circle_radius = self.sampling.outer_circle_radius - ri(30, 50)
                trees_to_add.append(self.sampling.sampling(10, tree, gamedisplay))

            for tree in trees_to_add:
                if tree is not None:
                    self.trees[tree.coords] = tree

        if self.year % 10 == 0:
            if self.sim_type == CUTTING:
                for i in range(int(self.trees_to_cut * len(self.trees))):
                    self.remove_random_tree()
            elif self.sim_type == PLANTING:
                self.trees_to_plant += self.trees_to_plant_save

        if self.year == self.total_years:
            return self.sim_type + 1
        else:
            return self.sim_type

    def remove_random_tree(self):
        tree = ch(list(self.trees))
        self.trees[tree].delete()
        self.trees[tree].kill()
        self.trees.pop(tree)

    def get_trees_group(self):
        return self.trees_group
