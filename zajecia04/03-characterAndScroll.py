import pygame
import os

pygame.init()
pygame.font.init()

window = pygame.display.set_mode((1000, 500)) # Utworznie ekranu o rządanej rozdzielczości
bg_image = pygame.image.load('Background.png') # wczytanie tła
bg = pygame.transform.scale(bg_image,(1000, 500)) # Przeskalowanie tła

myfont = pygame.font.SysFont('Comic Sans MS', 30) # Wczytanie czcionki o rozmiarze 30px
run = True
i = 0
width = 1000 # Zmienna odpowiedzialna za utrzymanie szerokości

# Character
stand = pygame.image.load(os.path.join("Hero", "standing.png")) # łatowanie startowego sprite
left = [] # Tworzenie listy dla spritów odwróconych na Lewo
right = [] # Tworzenie listy dla spritów odwróconych na Lewo
for i in range(0,9): # wypełnianie po przez pętlę spritami lewo i prawo
    left.append(pygame.image.load(os.path.join("Hero", "L"+str(i+1)+".png")))
    right.append(pygame.image.load(os.path.join("Hero", "R"+str(i+1)+".png")))

x = 150
y = 250
vel_x = 10
vel_y = 10
run = True
jump = False
move_left = False
move_right = False
stepIndex = 0

def draw_game(): # Utworzenei funkcji
    global stepIndex
    if stepIndex >= 9:
        stepIndex = 0
    if move_left:
        window.blit(left[stepIndex], (x, y))
        stepIndex += 1
    elif move_right:
        window.blit(right[stepIndex], (x, y))
        stepIndex += 1
    else:
        window.blit(stand, (x,y))



while run:
    if i <= -1000:
        i = 0
    i -= 3

    textsurface1 = myfont.render('obraz1:'+str(i), False, (255, 0, 0)) # Funkcja do renderowania wartości pętli
    textsurface2 = myfont.render('obraz2:' + str(i+width),50, (0, 255, 0))
    window.blit(bg, (i,0)) # Wczytanie pierwszej ilustracji tła pozycja początkowa: 0, -5, -10, -15, -20 ... -1000, 0, -5 ....
    window.blit(textsurface1, (0, 0)) # Wyświetlenie pozycji pierwszej ilustracji
    window.blit(bg, (width+i, 0)) # Wczytanie drugiej ilustracji tła pozycja początkowa 1000+(-5)=995, 995+(-5)=990
    window.blit(textsurface2, (0, 40)) # Wyświetlenie pozycji drugiej ilustracji
    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        stepIndex = 0
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y*4 # zmniejszanie wartości y (im mniejsza tym wyżej o współczynnik 4) czyli y = 250 - 10*4, y = 210 - 9*4, y = 174 - 8*4
        vel_y -= 1  # y = 142 - 7*4, y=114 - 6*4, y = 90 - 5*4, y = 70 - 4*4, y = 54 - 3*4, y = 42 - 2*4, y = 34 - 1*4, y = 30 - 0*4,
        pygame.time.delay(10) # y = 30 - -1*4, y = 34 - -2*4, y = 42 - -3*4, y = 54 - -4*4, y = 70 - -5*4, y = 90 - -6*4, .... y = 210 - -9*4 = 250
        if vel_y < -10:
            jump = False
            vel_y = 10

    if i == -1000:
        i = 0
    print(i)

    pygame.time.delay(30)
    pygame.display.update()