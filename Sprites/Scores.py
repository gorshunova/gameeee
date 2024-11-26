import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load() #!!!!!!!!
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        ...
