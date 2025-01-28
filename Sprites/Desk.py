import pygame
from pygame import sprite, image, transform

from Sprites.Platform import Platform

class Desk(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=96, height=96)
        width = 96
        height = 96
        self.image = image.load('assets/desk.png')
        self.image = transform.scale(self.image, (width, height))
        self.update_rect()
