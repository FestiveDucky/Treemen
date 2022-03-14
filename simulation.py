import pygame.sprite

from random import choice as ch, randint as ri


# TODO add images to trees and acorns, make some trees mature vs. other being "unmature"

class Tree(pygame.sprite.Sprite):
    def __init__(self, master, group, coords, cell):
        super().__init__(group)
        self.master = master
        self.coords = coords
        self.cell = cell
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(centerx=self.coords[1], centery=self.coords[0])

    def delete(self):
        self.master.available_cells[self.cell] = self.master.cells[self.cell]
        self.master.cells[self.cell].remove_point()
        self.master.points.remove(self.coords)


class Simulation:
    def __init__(self, total_years):
        self.trees = {}
        self.trees_group = pygame.sprite.Group()
        self.year = 0
        self.sampling = None
        self.average_trees_alive = 0
        self.total_years = total_years

    def one_year(self, gamedisplay):
        self.year += 1
        print(self.year)
        self.average_trees_alive += len(self.trees)
        print(f"Average Trees: {self.average_trees_alive // self.year}")
        # TODO every 20 years kill 75% of trees
        remove = []
        for tree in self.trees:
            num = ri(1, 100)
            # 27
            if num <= 30:
                self.trees[tree].delete()
                self.trees[tree].kill()
                remove.append(tree)

        for coords in remove:
            self.trees.pop(coords)

        if self.year % 2 == 0:
            trees_to_add = []
            for tree in self.trees:
                # TODO make more biased to higher values
                self.sampling.outer_circle_radius = ri(60, 120)
                self.sampling.inner_circle_radius = self.sampling.outer_circle_radius - ri(30, 50)
                trees_to_add.append(self.sampling.sampling(20, tree, gamedisplay))

            for tree in trees_to_add:
                if tree is not None:
                    self.trees[tree.coords] = tree

        if self.year == self.total_years:
            return True
        else:
            return False

    def get_trees_group(self):
        return self.trees_group
