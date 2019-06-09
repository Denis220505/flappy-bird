import pygame
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedy = 3
        self.grav = 1
        self.image = pygame.image.load("bird.png")
        self.rect = self.image.get_rect()
        self.rect.y = 0
        self.image = pygame.transform.scale(self.image,(50,75))
        self.image.fill((235,56,97))
    def update(self):
        self.rect.y += self.speedy
