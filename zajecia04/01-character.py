import pygame
import os

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pierwsza Gra")

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
    window.fill((0, 0, 0))
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


    pygame.time.delay(30)
    pygame.display.update()
