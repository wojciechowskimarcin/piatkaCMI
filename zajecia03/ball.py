import pygame

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pierwsza Gra")

x = 250
y = 250
radius = 15
vel_x = 10
vel_y = 10
run = True
jump = False

while run:

    window.fill((0,0,0))
    pygame.draw.circle(window, (255, 255, 255), (int(x), int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if userInput[pygame.K_RIGHT] and x < 500:
        x += vel_x
    if userInput[pygame.K_UP] and y > 0:
        y -= vel_y
    if userInput[pygame.K_DOWN] and y < 500:
        y += vel_y

    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        y -= vel_y*3
        vel_y -= 1
        pygame.time.delay(10)
        print(vel_y, " ", y)
        if vel_y < -10:
            jump = False
            vel_y = 10


    pygame.time.delay(10)
    pygame.display.update()
