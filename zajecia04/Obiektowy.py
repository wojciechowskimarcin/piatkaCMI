import pygame
import os

# Init and Create Window (win)
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

# Load and Size Images
background = pygame.transform.scale(pygame.image.load(os.path.join("", "Background.png")), (win_width, win_height))
bullet_img = pygame.transform.scale(pygame.image.load(os.path.join("images", "bullet.png")), (10,10))
stationary = pygame.image.load(os.path.join("Hero", "standing.png"))
left = [pygame.image.load(os.path.join("Hero", "L1.png")),
        pygame.image.load(os.path.join("Hero", "L2.png")),
        pygame.image.load(os.path.join("Hero", "L3.png")),
        pygame.image.load(os.path.join("Hero", "L4.png")),
        pygame.image.load(os.path.join("Hero", "L5.png")),
        pygame.image.load(os.path.join("Hero", "L6.png")),
        pygame.image.load(os.path.join("Hero", "L7.png")),
        pygame.image.load(os.path.join("Hero", "L8.png")),
        pygame.image.load(os.path.join("Hero", "L9.png"))
        ]
right =[pygame.image.load(os.path.join("Hero", "R1.png")),
        pygame.image.load(os.path.join("Hero", "R2.png")),
        pygame.image.load(os.path.join("Hero", "R3.png")),
        pygame.image.load(os.path.join("Hero", "R4.png")),
        pygame.image.load(os.path.join("Hero", "R5.png")),
        pygame.image.load(os.path.join("Hero", "R6.png")),
        pygame.image.load(os.path.join("Hero", "R7.png")),
        pygame.image.load(os.path.join("Hero", "R8.png")),
        pygame.image.load(os.path.join("Hero", "R9.png"))
        ]


class Hero:
    def __init__(self, x, y):
        # Walk
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        # Jump
        self.jump = False
        self.bullets = []

    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            print(self.x)
            self.face_right = True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            print(self.x)
            self.face_right = False
            self.face_left = True
        else:
            self.stepIndex = 0
            self.face_right = False
            self.face_left = False

    def draw(self, win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if not self.face_left and not self.face_right:
            win.blit(stationary, (self.x, self.y))

    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -10:
            self.jump = False
            self.vely = 10

    def direction(self):
        if self.face_right:
            return 1
        if self.face_left:
            return -1

    def shoot(self):
        if userInput[pygame.K_f]:
            bullet = Bullet(self.x, self.y, self.direction())
            self.bullets.append(bullet)
        for bullet in self.bullets:
            bullet.move()

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x+15
        self.y = y+25
        self.direction = direction
    def draw_bullet(self):
        if self.direction == 1 or self.direction == -1:
            win.blit(bullet_img, (self.x, self.y))
    def move(self):
        if self.direction == 1:
            self.x += 15
        if self.direction == -1:
            self.x -= 15

# Draw Game
def draw_game():
    win.blit(background, (0,0))
    player.draw(win)
    for bullet in player.bullets:
        bullet.draw_bullet()
    #player1.draw(win)
    pygame.time.delay(30)
    pygame.display.update()

# Tworzenie instancji obiektu
player = Hero(0, 290)
#player1 = Hero(100, 290)
# Główna pętla programu
run = True
while run:

    # Wyjście z gry
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Wejście
    userInput = pygame.key.get_pressed()

    # Strzelanie
    player.shoot()

    # Poruszanie się
    player.move_hero(userInput)
    player.jump_motion(userInput)

    # Utworzenie gry
    draw_game()

