import pygame
import sys

pygame.init()

res = (500, 500)
screen = pygame.display.set_mode(res)

white = (255, 255, 255)
unselected_color = (170, 170, 170)  # lighter
selected_color = (100, 100, 100)  # darker
width = res[0]
height = res[1]
start_pos = (width / 2, height / 4)
font = pygame.font.SysFont('Cambria', 35)
menu_showing = True
game_speed = 2
game_mode = 0

start = font.render('START', True, 'blue')
while menu_showing:

    screen.fill(white)
    mouse = pygame.mouse.get_pos()

    # shows if selected
    if game_mode == 1:
        pygame.draw.rect(screen, 'green', [start_pos[0] - 1, start_pos[1] + 49, 142, 42])
    elif game_mode == 2:
        pygame.draw.rect(screen, 'green', [start_pos[0] - 1, start_pos[1] + 99, 142, 42])
    elif game_mode == 3:
        pygame.draw.rect(screen, 'green', [start_pos[0] - 1, start_pos[1] + 149, 142, 42])

    # start button
    if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] <= mouse[1] <= start_pos[1] + 40:
        pygame.draw.rect(screen, unselected_color, [start_pos[0], start_pos[1], 140, 40])

    else:
        pygame.draw.rect(screen, selected_color, [start_pos[0], start_pos[1], 140, 40])

    # plant trees
    if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 50 <= mouse[1] <= start_pos[1] + 90:
        pygame.draw.rect(screen, unselected_color, [start_pos[0], start_pos[1] + 50, 140, 40])

    else:
        pygame.draw.rect(screen, selected_color, [start_pos[0], start_pos[1] + 50, 140, 40])

    # normal
    if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 100 <= mouse[1] <= start_pos[1] + 140:
        pygame.draw.rect(screen, unselected_color, [start_pos[0], start_pos[1] + 100, 140, 40])

    else:
        pygame.draw.rect(screen, selected_color, [start_pos[0], start_pos[1] + 100, 140, 40])

    # cut trees
    if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 150 <= mouse[1] <= start_pos[1] + 190:
        pygame.draw.rect(screen, unselected_color, [start_pos[0], start_pos[1] + 150, 140, 40])

    else:
        pygame.draw.rect(screen, selected_color, [start_pos[0], start_pos[1] + 150, 140, 40])

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:

            # startbutton
            if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] <= mouse[1] <= start_pos[1] + 40:
                menu_showing = False
                pygame.quit()  # comment this line out

            # plant trees
            if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 50 <= mouse[1] <= start_pos[1] + 90:
                game_mode = 1
                print(1)

            # normal
            if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 100 <= mouse[1] <= start_pos[1] + 140:
                game_mode = 2
                print(2)

            # cut trees
            if start_pos[0] <= mouse[0] <= start_pos[0] + 140 and start_pos[1] + 150 <= mouse[1] <= start_pos[1] + 190:
                game_mode = 3
                print(3)

    screen.blit(start, (start_pos[0] + 20, start_pos[1]))

    pygame.display.update()
