import pygame

successes, failures = pygame.init() # zwraca true jeżeli success
print("inicjuje : {0} submodułów udało się i {1} nie udało się.".format(successes, failures))
win = pygame.display.set_mode((500, 500)) # Tworzę ono o rozdzielczości 500x500px
pygame.display.set_caption("Pierwsza gra") # Wyświetlam tytuł okna Pierwsza gra
clock = pygame.time.Clock() # Utworzenie zegara
FPS = 60  # Klatki na sekundę (Frame Per Second)


run = True
while run: # Tworzę pętlę do momentu uzyskania zdarzenia (event) --> pygame.Quit.
    clock.tick(FPS) # Funkcja tick odmierza czas w PyGame
    for event in pygame.event.get(): # oczekiwanie na zdarzenie
        if event.type == pygame.QUIT: # jeśli zdarzenie to pygame.QUIT --> czyli ktoś klinął na krzyżyk zamknięcia okna
            run = False # wtedy pętla się kończy bo zależy od warunku while

    pygame.display.update() # aktualizacja ekranu
