from pygame import sprite, image, transform

from Sprites.Platform import Platform


class Door(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=192)
        width = 32
        height = 64
        self.image = image.load('assets/opened_door.png')
        self.image = transform.scale(self.image, (width, height))

# + открытая дверь !!!!!!!!!!!!!!!!!!!!!!!!!!!!

