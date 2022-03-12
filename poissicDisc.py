import pygame, time, math
from random import randint as ri
from random import choice as ch


class Cell(pygame.sprite.Sprite):
    def __init__(self, side_length, coords):
        super().__init__()
        self.side_length = side_length
        self.coords = coords
        self.point = None
        self.image = pygame.Surface((self.side_length - 1, self.side_length - 1))
        self.image.fill((30, 30, 30))
        self.rect = self.image.get_rect(x=self.coords[1] * self.side_length, y=self.coords[0] * self.side_length)

    def add_point(self, point):
        self.point = point


class Sampling:
    def __init__(self, x1, y1, x2, y2, candidate_samples, inner_circle_radius, outer_circle_radius, gamedisplay,
                 thickness, circle_size):
        # x1, y1, x2, y2 are the dimensions on where to run the algorithm
        self.gamedisplay = gamedisplay
        self.inner_circle_radius = inner_circle_radius
        self.outer_circle_radius = outer_circle_radius
        self.thickness = thickness
        self.circle_size = circle_size
        self.points = []
        self.available_points = []

        self.x1 = x1
        self.y1 = y1

        self.cell_side_length = int(self.inner_circle_radius / math.sqrt(2))
        # Making the dimensions evenly divisble by the cell side length
        self.x2 = x2 // self.cell_side_length * self.cell_side_length
        self.y2 = y2 // self.cell_side_length * self.cell_side_length
        self.x1 = x1 // self.cell_side_length * self.cell_side_length
        self.y1 = y1 // self.cell_side_length * self.cell_side_length

        self.cells = {}
        self.available_cells = {}
        for y in range(self.y1 // self.cell_side_length, self.y2 // self.cell_side_length):
            for x in range(self.x1 // self.cell_side_length, self.x2 // self.cell_side_length):
                new_cell = Cell(self.cell_side_length, (y, x))
                self.cells[(y, x)] = new_cell
                self.available_cells[(y, x)] = new_cell

        self.createPoints(candidate_samples)

    def draw(self, specific_point, all=False):
        if all:
            # Draws the cells underneath the points for debugging
            # for cell in self.cells:
            #     self.gamedisplay.blit(self.cells[cell].image, self.cells[cell].rect)

            for point in self.points:
                if point in self.available_points:
                    color = (255, 255, 255)
                else:
                    color = (255, 0, 0)

                pygame.draw.circle(self.gamedisplay, color, (point[1], point[0]), self.circle_size,
                                   self.thickness)

        else:
            if specific_point in self.available_points:
                color = (255, 255, 255)
            else:
                color = (255, 0, 0)
            pygame.draw.circle(self.gamedisplay, color, (specific_point[1], specific_point[0]),
                               self.circle_size, self.thickness)
        pygame.display.update()

    def checkEvents(self):
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()

    def getPoints(self):
        return self.points

    def distance(self, other_point, current_point):
        vector = (current_point[0] - other_point[0], current_point[1] - other_point[1])
        dis = math.sqrt(vector[0] ** 2 + vector[1] ** 2)
        return dis

    def new_point(self, angle, distance, current_point):
        angle = math.radians(angle)
        return current_point[0] + (distance * math.sin(angle)), current_point[1] + (distance * math.cos(angle))

    def createPoints(self, candidate_samples):
        # Starting point
        current_point = (ri(self.y1, self.y2), ri(self.x1, self.x2))
        self.cells[
            (int(current_point[0] / self.cell_side_length), int(current_point[1] / self.cell_side_length))].add_point(
            current_point)
        self.points.append(current_point)
        self.available_cells.pop(
            (int(current_point[0] / self.cell_side_length), int(current_point[1] / self.cell_side_length)))
        self.available_points.append(current_point)

        while True:
            finished = False
            new_point = None
            for i in range(candidate_samples):
                self.checkEvents()

                angle = ri(1, 360)
                distance = ri(self.inner_circle_radius, self.outer_circle_radius)
                new_candidate = self.new_point(angle, distance, current_point)
                if self.distance(tuple(map(round, new_candidate)), current_point) > self.outer_circle_radius:
                    new_candidate = tuple(map(int, new_candidate))
                else:
                    new_candidate = tuple(map(round, new_candidate))
                if self.y2 <= new_candidate[0] or new_candidate[0] < self.y1 or self.x2 <= new_candidate[1] or \
                        new_candidate[1] < self.x1:
                    continue

                point_cell = (
                int(new_candidate[0] / self.cell_side_length), int(new_candidate[1] / self.cell_side_length))

                if self.cells[point_cell].point is not None:
                    continue

                nearby_points = []
                for ny in range(point_cell[0] - 3, point_cell[0] + 3):
                    for nx in range(point_cell[1] - 3, point_cell[1] + 3):
                        if self.y1 // self.cell_side_length <= ny < self.y2 // self.cell_side_length and self.x1 // self.cell_side_length <= nx < self.x2 // self.cell_side_length and (
                        ny, nx) not in self.available_cells:
                            nearby_points.append(self.cells[(ny, nx)].point)

                distances = list(set(list(map(self.distance, nearby_points, [new_candidate] * len(nearby_points)))))
                failed = False
                for dis in distances:
                    if dis <= self.inner_circle_radius:
                        failed = True
                        break

                if not failed:
                    self.points.append(new_candidate)
                    self.available_points.append(new_candidate)
                    self.cells[point_cell].add_point(new_candidate)
                    self.available_cells.pop(point_cell)
                    new_point = new_candidate
                    finished = True
                    break

            if not finished:
                self.available_points.remove(current_point)
                self.draw(current_point)
            else:
                self.draw(new_point)

            if len(self.available_points) > 0:
                current_point = ch(self.available_points)
            else:
                break
