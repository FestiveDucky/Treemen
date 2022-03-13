import pygame.sprite
from sampling import *
from random import choice as ch


# TODO add images to trees and acorns, make some trees mature vs. other being "unmature"

class Tree(pygame.sprite.Sprite):
    def __init__(self, master, group, coords):
        super().__init__(group)
        self.master = master
        self.life_span = 0
        self.coords = coords
        self.acorns_sample = None
        self.acorns = []
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(centerx=self.coords[1], centery=self.coords[0])

    def make_tree(self):
        if len(self.acorns) >= 20:
            new_tree = ch(self.acorns)
        else:
            create_tree = ch([True] * len(self.acorns) + [False] * (100 - len(self.acorns)))
            if create_tree:
                new_tree = ch(self.acorns)
            else:
                return

        tree = Tree(self.master, self.master.trees_group, new_tree)
        return tree

    def acorn_cycle(self, gamedisplay, reached_tree_cap):
        # Each acorn sprite represents 1000 real acorns
        self.acorns_sample = Sampling(self.coords[1] - 30, self.coords[0] - 30, self.coords[1] + 30, self.coords[0] + 30, 20, 20, 25, 5, 1)
        self.acorns = self.acorns_sample.getPoints()
        self.acorns_sample.draw(None, gamedisplay, (0, 255, 0), True)
        if not reached_tree_cap:
            return self.make_tree()


class Simulation:
    def __init__(self, tree_coords, max, tree_cap):
        self.trees = {}
        self.trees_group = pygame.sprite.Group()
        self.year = 0
        self.tree_cap = tree_cap
        self.last_year = max
        for coords in tree_coords:
            self.trees[coords] = Tree(self, self.trees_group, coords)
        print(len(tree_coords))

    def one_year(self, gamedisplay):
        self.year += 1
        print(self.year)
        if self.year % 2 == 0:
            new_trees = []
            for tree in self.trees:
                new_trees.append(self.trees[tree].acorn_cycle(gamedisplay, self.tree_cap <= len(self.trees)))

            for tree in new_trees:
                if tree is not None:
                    self.trees[tree.coords] = tree
        if self.year == self.last_year:
            return True
        else:
            return False

    def get_trees_group(self):
        return self.trees_group
