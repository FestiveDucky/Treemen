import pygame

BLACK = (0, 0, 0)
ORANGE = (229, 157, 33)
GREY = (194, 174, 145)


class Slider:
    def __init__(self, x1, y1, length, minval, maxval, curval):
        self.x1 = x1
        self.y1 = y1
        self.len = length
        self.x2 = x1 + length
        self.y2 = y1 + 40
        self.minval = minval
        self.maxval = maxval
        self.curval = curval
        self.circlex = (self.curval - self.minval) * (self.len - 40) // (self.maxval - self.minval) + self.x1 + 20
        self.slider_font = sliderfont = pygame.font.SysFont('Cambria', 25)
        self.display_val = sliderfont.render(str(curval), True, BLACK)

    def update(self, mouse_held, screen, mouse, percent=False):
        if mouse_held:
            if self.x1 + 20 <= mouse[0] <= self.x1 + self.len - 20 and self.y1 + 14 <= mouse[1] <= self.y1 + 26:
                self.circlex = mouse[0]
        self.curval = self.minval + (self.circlex - self.x1 - 20) * (self.maxval - self.minval) // (self.len - 40)
        if percent:
            value = f"{self.curval}%"
        else:
            value = str(self.curval)
        self.display_val = self.slider_font.render(value, True, BLACK)
        # pygame.draw.rect(screen, white, [self.x1, self.y1, self.len, 40])
        pygame.draw.rect(screen, (154, 134, 105), [self.x1 + 15, self.y1 + 15, self.len - 30, 10])
        pygame.draw.circle(screen, (224, 204, 175), [self.circlex, self.y1 + 20], 12)
        screen.blit(self.display_val, (self.x1 + self.len + 10, self.y1 + 5))


def show_menu1(width, height, screen):
    start_pos = (width / 2 - 100, height * 7 / 10)
    font = pygame.font.SysFont('Cambria', 50)

    Titlefont = pygame.font.SysFont('Cambria', 60)
    smalltextfont = pygame.font.SysFont('Cambria', 20)
    menu_showing = True
    mouse_held = False
    start = font.render('START', True, BLACK)

    # Need to make the slider outside the loop otherwise it will remake the slider every frame
    text1 = smalltextfont.render('Number of Starting Trees', True, BLACK)
    numtrees = Slider(150, 450, 300, 10, 30, 20)
    text2 = smalltextfont.render('Natural Deathrate of Trees (%)', True, BLACK)
    deathrate = Slider(150, 600, 120, 1, 11, 6)
    text3 = smalltextfont.render('Trees Planted Every Ten Years', True, BLACK)
    newtrees = Slider(700, 450, 140, 15, 45, 30)
    text4 = smalltextfont.render('Trees Cut Every Ten Years (%)', True, BLACK)
    cuttrees = Slider(700, 600, 250, 40, 60, 50)

    title1 = Titlefont.render('Planting Trees to Increase', True, BLACK)
    title2 = Titlefont.render('Carbon Dioxide Absorbtion Rate', True, BLACK)

    text5 = smalltextfont.render('This Simulation Analyzes Three Scenarios', True, BLACK)
    text6 = smalltextfont.render('CUTTING| Where Oaks are Cut for Construction and Other Purposes', True, BLACK)
    text7 = smalltextfont.render('BASE| The Natural Tree Cycle Without Human Interference', True, BLACK)
    text8 = smalltextfont.render('PLANTING| Where More Trees are Planted in Addition to the Base Case', True, BLACK)

    while menu_showing:
        screen.fill(GREY)
        mouse = pygame.mouse.get_pos()
        # start button
        if start_pos[0] <= mouse[0] <= start_pos[0] + 170 and start_pos[1] <= mouse[1] <= start_pos[1] + 50:
            pygame.draw.rect(screen, (224, 204, 175), [start_pos[0], start_pos[1], 170, 60])
        else:
            pygame.draw.rect(screen, (154, 134, 105), [start_pos[0], start_pos[1], 170, 60])

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                mouse_held = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True
                # start button
                if start_pos[0] <= mouse[0] <= start_pos[0] + 170 and start_pos[1] <= mouse[1] <= start_pos[1] + 50:
                    menu_showing = False

        screen.blit(start, (start_pos[0] + 10, start_pos[1]))

        screen.blit(text1, (150, 425))
        numtrees.update(mouse_held, screen, mouse)
        screen.blit(text2, (150, 575))
        deathrate.update(mouse_held, screen, mouse, True)
        screen.blit(text3, (700, 425))
        newtrees.update(mouse_held, screen, mouse)
        screen.blit(text4, (700, 575))
        cuttrees.update(mouse_held, screen, mouse, True)

        screen.blit(title1, (600, 100))
        screen.blit(title2, (550, 175))

        screen.blit(text5, (1300, 450))
        pygame.draw.rect(screen, (154, 134, 105), [1200, 500, 600, 10])
        screen.blit(text6, (1210, 550))
        screen.blit(text7, (1250, 600))
        screen.blit(text8, (1200, 650))
        pygame.display.update()

    return numtrees.curval, deathrate.curval, newtrees.curval, cuttrees.curval
