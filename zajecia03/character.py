import pygame
import os

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pierwsza Gra")

stand = pygame.image.load(os.path.join("Hero", "standing.png"))
left = []
right = []
for i in range(0,9):
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

def draw_game():
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




   # pygame.draw.circle(window, (255, 0, 0), (int(x+30), int(y+30)), radius)
    #if x < 510:
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
        y -= vel_y*3
        vel_y -= 1
        pygame.time.delay(10)
        if vel_y < -10:
            jump = False
            vel_y = 10


    pygame.time.delay(30)
    pygame.display.update()
