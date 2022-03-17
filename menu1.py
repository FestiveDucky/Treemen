import pygame

ORANGE = (243, 170, 78)
DARK_BLUE = (17, 24, 32)
SEMI_DARK_BLUE = (47, 54, 62)
BLUE = (77, 84, 92)


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
        self.display_val = sliderfont.render(str(curval), True, ORANGE)

    def update(self, mouse_held, screen, mouse, percent=False):
        if mouse_held:
            if self.x1 + 20 <= mouse[0] <= self.x1 + self.len - 20 and self.y1 + 14 <= mouse[1] <= self.y1 + 26:
                self.circlex = mouse[0]
        self.curval = self.minval + (self.circlex - self.x1 - 20) * (self.maxval - self.minval) // (self.len - 40)
        if percent:
            value = f"{self.curval}%"
        else:
            value = str(self.curval)
        self.display_val = self.slider_font.render(value, True, ORANGE)
        # pygame.draw.rect(screen, white, [self.x1, self.y1, self.len, 40])
        pygame.draw.rect(screen, SEMI_DARK_BLUE, [self.x1 + 15, self.y1 + 15, self.len - 30, 10])
        pygame.draw.circle(screen, BLUE, [self.circlex, self.y1 + 20], 12)
        screen.blit(self.display_val, (self.x1 + self.len + 10, self.y1 + 5))


def show_menu1(width, height, screen):
    start_pos = (width / 2 - 100, height * 7 / 10)
    font = pygame.font.SysFont('Cambria', 50)

    Titlefont = pygame.font.SysFont('Cambria', 60)
    smalltextfont = pygame.font.SysFont('Cambria', 20)
    menu_showing = True
    mouse_held = False
    start = font.render('START', True, ORANGE)

    # Need to make the slider outside the loop otherwise it will remake the slider every frame
    text1 = smalltextfont.render('Number of Starting Trees', True, ORANGE)
    numtrees = Slider(150, 450, 300, 10, 30, 20)
    text2 = smalltextfont.render('Natural Deathrate of Trees (%)', True, ORANGE)
    deathrate = Slider(150, 600, 120, 1, 11, 6)
    text3 = smalltextfont.render('Trees Planted Every Ten Years', True, ORANGE)
    newtrees = Slider(700, 450, 140, 15, 45, 30)
    text4 = smalltextfont.render('Trees Cut Every Ten Years (%)', True, ORANGE)
    cuttrees = Slider(700, 600, 250, 40, 60, 50)

    title1 = Titlefont.render('Planting Trees to Increase', True, ORANGE)
    title2 = Titlefont.render('Carbon Dioxide Absorbtion Rate', True, ORANGE)

    text5 = smalltextfont.render('This Simulation Analyzes Three Scenarios', True, ORANGE)
    text6 = smalltextfont.render('CUTTING| Where Oaks are Cut for Construction and Other Purposes', True, ORANGE)
    text7 = smalltextfont.render('BASE| The Natural Tree Cycle Without Human Interference', True, ORANGE)
    text8 = smalltextfont.render('PLANTING| Where More Trees are Planted in Addition to the Base Case', True, ORANGE)

    while menu_showing:
        screen.fill(DARK_BLUE)
        mouse = pygame.mouse.get_pos()
        # start button
        if start_pos[0] <= mouse[0] <= start_pos[0] + 170 and start_pos[1] <= mouse[1] <= start_pos[1] + 60:
            pygame.draw.rect(screen, BLUE, [start_pos[0], start_pos[1], 170, 60])
        else:
            pygame.draw.rect(screen, SEMI_DARK_BLUE, [start_pos[0], start_pos[1], 170, 60])

        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONUP:
                mouse_held = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_held = True
                # start button
                if start_pos[0] <= mouse[0] <= start_pos[0] + 170 and start_pos[1] <= mouse[1] <= start_pos[1] + 60:
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
        pygame.draw.rect(screen, SEMI_DARK_BLUE, [1200, 500, 600, 10])
        screen.blit(text6, (1210, 550))
        screen.blit(text7, (1250, 600))
        screen.blit(text8, (1200, 650))
        pygame.display.update()

    return numtrees.curval, deathrate.curval, newtrees.curval, cuttrees.curval
