
from pygame import sprite, image, transform

from Sprites.Platform import Platform


class Ground(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, h):
        super().__init__(*groups, x=0, y=h, width=1200)
        width = 1200
        self.image = image.load('assets/platform.png')
        self.image = transform.scale(self.image, (width, 32))



