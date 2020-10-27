import pygame
pygame.init()
pygame.font.init()

window = pygame.display.set_mode((1000, 500)) # Utworznie ekranu o rządanej rozdzielczości
bg_image = pygame.image.load('Background.png') # wczytanie tła
bg = pygame.transform.scale(bg_image,(1000, 500)) # Przeskalowanie tła

myfont = pygame.font.SysFont('Comic Sans MS', 30) # Wczytanie czcionki o rozmiarze 30px

run = True
i = 0
width = 1000 # Zmienna odpowiedzialna za utrzymanie szerokości
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    textsurface1 = myfont.render('obraz1:'+str(i), False, (255, 0, 0)) # Funkcja do renderowania wartości pętli
    textsurface2 = myfont.render('obraz2:' + str(i+width),50, (0, 255, 0))
    window.blit(bg, (i,0)) # Wczytanie pierwszej ilustracji tła pozycja początkowa: 0, -5, -10, -15, -20 ... -1000, 0, -5 ....
    window.blit(textsurface1, (0, 0)) # Wyświetlenie pozycji pierwszej ilustracji
    window.blit(bg, (width+i, 0)) # Wczytanie drugiej ilustracji tła pozycja początkowa 1000+(-5)=995, 995+(-5)=990
    window.blit(textsurface2, (0, 40)) # Wyświetlenie pozycji drugiej ilustracji


    if i == -1000:
        i = 0
    i -= 5
    print(i)
    pygame.time.delay(30)

    pygame.display.update()