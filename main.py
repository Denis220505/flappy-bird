import pygame
from class_bird import Bird
from class_tube import Tube
clock = pygame.time.Clock()
bird = Bird()
tube = Tube()
pygame.time.set_timer(pygame.USEREVENT,100)
NEWTUBE = pygame.USEREVENT + 1
new_tube = pygame.event.Event(NEWTUBE)
pygame.time.set_timer(NEWTUBE,17000)
HIGH = 600
SIZE = 800
gamedisplay = pygame.display.set_mode((SIZE, HIGH))
sprite = pygame.sprite.Group()
sprite.add(bird)
sprite.add(tube)
game = True
while game:
    for event in pygame.event.get():
        if event.type == NEWTUBE:
            print("kjh")
            tube = Tube()
            sprite.add(tube)
        if event.type == pygame.QUIT:
            game = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     y -= 10
        if event.type == pygame.USEREVENT:
            print('gfd')
            sprite.update()
    gamedisplay.fill((0,0,0))
    sprite.draw(gamedisplay)
    pygame.display.update()
    clock.tick(60)
pygame.quit()