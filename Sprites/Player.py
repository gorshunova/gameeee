import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load() #!!!!!!!!
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #speed сюда писать





