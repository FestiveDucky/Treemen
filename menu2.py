import pygame

ORANGE = (229, 157, 33)
GREY = (194, 174, 145)

def show_menu2(screen, averageTrees, treeCounts):
    smalltextfont = pygame.font.SysFont('Cambria', 25)
    boldtextfont = pygame.font.SysFont('Cambria', 35)
    font = pygame.font.SysFont('Cambria', 50)
    boldtextfont.set_bold(True)
    Titlefont = pygame.font.SysFont('Cambria', 100)
    mediumtextfont = pygame.font.SysFont('Cambria', 60)
    close = font.render('CLOSE', True, (0, 0, 0))
    
    title1 = Titlefont.render('Planting Trees to Increase', True, (0, 0, 0))
    title2 = Titlefont.render('Carbon Dioxide Absorbtion Rate', True, (0, 0, 0))
    
    subtitle1 = mediumtextfont.render('Cutting', True, (0, 0, 0))
    subtitle2 = mediumtextfont.render('Base', True, (0, 0, 0))
    subtitle3 = mediumtextfont.render('Planting', True, (0, 0, 0))
    
    text1 = smalltextfont.render('Average Trees Per Year', True, (0, 0, 0))
    text2 = smalltextfont.render('Final Tree Count', True, (0, 0, 0))
    text3 = smalltextfont.render('Trees Needed to Cover 100%', True, (0, 0, 0))
    text4 = smalltextfont.render("of One Human's Base Carbon Footprint", True, (0, 0, 0))
    text5 = smalltextfont.render('Absorbtion of Base Carbon Footprint', True, (0, 0, 0))
    
    averageTrees1 = smalltextfont.render(f'{averageTrees[1]}', True, (0, 0, 0))
    averageTrees2 = smalltextfont.render(f'{averageTrees[0]}', True, (0, 0, 0))
    averageTrees3 = smalltextfont.render(f'{averageTrees[2]}', True, (0, 0, 0))
    
    treeCount1 = smalltextfont.render(f'{treeCounts[1]}', True, (0, 0, 0))
    treeCount2 = smalltextfont.render(f'{treeCounts[0]}', True, (0, 0, 0))
    treeCount3 = smalltextfont.render(f'{treeCounts[2]}', True, (0, 0, 0))
    
    treesNeeded = smalltextfont.render('15', True, (0, 0, 0))
    
    absorbtion1 = boldtextfont.render(f'{round(averageTrees[1] / 9, 1)}%', True, (0, 0, 0))
    absorbtion2 = boldtextfont.render(f'{round(averageTrees[0] / 9, 1)}%', True, (0, 0, 0))
    absorbtion3 = boldtextfont.render(f'{round(averageTrees[2] / 9, 1)}%', True, (0, 0, 0))

    close_pos = (1920 / 2 - 100, 1080 * 7 / 10 + 200)
    running = True
    while running:
        mouse = pygame.mouse.get_pos()

        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                if close_pos[0] <= mouse[0] <= close_pos[0] + 170 and close_pos[1] <= mouse[1] <= close_pos[1] + 50:
                    running = False

        screen.fill(GREY)

        if close_pos[0] <= mouse[0] <= close_pos[0] + 170 and close_pos[1] <= mouse[1] <= close_pos[1] + 50:
            pygame.draw.rect(screen, (224, 204, 175), [close_pos[0], close_pos[1], 170, 60])
        else:
            pygame.draw.rect(screen, (154, 134, 105), [close_pos[0], close_pos[1], 170, 60])
        screen.blit(close, (close_pos[0] + 10, close_pos[1]))
    
        screen.blit(title1, (350, 20))
        screen.blit(title2, (250, 120))
    
        screen.blit(subtitle1, (550, 300))
        screen.blit(subtitle2, (885, 300))
        screen.blit(subtitle3, (1140, 300))
    
        screen.blit(text1, (20, 450))
        screen.blit(text2, (20, 575))
        screen.blit(text3, (20, 700))
        screen.blit(text4, (20, 725))
        screen.blit(text5, (20, 850))
    
        screen.blit(averageTrees1, (620, 450))
        screen.blit(averageTrees2, (920, 450))
        screen.blit(averageTrees3, (1220, 450))
    
        screen.blit(treeCount1, (620, 575))
        screen.blit(treeCount2, (920, 575))
        screen.blit(treeCount3, (1220, 575))
    
        screen.blit(treesNeeded, (620, 715))
        screen.blit(treesNeeded, (920, 715))
        screen.blit(treesNeeded, (1220, 715))
    
        screen.blit(absorbtion1, (620, 850))
        screen.blit(absorbtion2, (920, 850))
        screen.blit(absorbtion3, (1220, 850))
    
        pygame.draw.rect(screen, (154, 134, 105), [650, 250, 600, 10])
        pygame.draw.rect(screen, (154, 134, 105), [500, 320, 10, 600])
        pygame.draw.rect(screen, (154, 134, 105), [800, 320, 10, 600])
        pygame.draw.rect(screen, (154, 134, 105), [1100, 320, 10, 600])
        pygame.draw.rect(screen, (154, 134, 105), [1400, 320, 10, 600])
    
        pygame.display.update()