import pygame
pygame.init()
pygame.font.init()

window = pygame.display.set_mode((1000, 500))
bg_image = pygame.image.load('Background.png')
bg = pygame.transform.scale(bg_image,(1000, 500))

myfont = pygame.font.SysFont('Comic Sans MS', 30)


run = True
i = 0
width = 1000
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    textsurface1 = myfont.render('obraz1:'+str(i), False, (255, 0, 0))
    textsurface2 = myfont.render('obraz2:' + str(i+width),50, (0, 255, 0))
    window.fill((0,0,0))
    window.blit(bg, (i,0))
    window.blit(textsurface1, (0, 0))
    window.blit(bg, (width+i, 0))
    window.blit(textsurface2, (0, 40))


    if i == -1000:
        i = 0
    i -= 5
    print(i)
    pygame.time.delay(100)

    pygame.display.update()