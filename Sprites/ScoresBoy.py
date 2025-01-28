import pygame


class ScoresBoy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.image.load('assets/score_boy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

