from pygame import sprite, image, transform

from Sprites.Platform import Platform


class Door(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=128)
        width = 128
        height = 256
        self.image = image.load('assets/door.png')
        self.image = transform.scale(self.image, (width, height))
        self.update_rect()

# + открытая дверь !!!!!!!!!!!!!!!!!!!!!!!!!!!!

