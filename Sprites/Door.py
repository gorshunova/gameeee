from pygame import sprite, image, transform

from Sprites.Platform import Platform


class Door(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=1200)
        width = 192
        height = 192
        self.image = image.load('assets/door.png')
        self.image = transform.scale(self.image, (width, height))

# + открытая дверь !!!!!!!!!!!!!!!!!!!!!!!!!!!!

