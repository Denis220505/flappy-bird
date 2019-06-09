import pygame
class Tube(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 3
        self.image = pygame.Surface((150,300))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.x = 800
    def update(self):
        self.rect.x -= self.speedx
