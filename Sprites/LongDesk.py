from pygame import sprite, image, transform

from Sprites.Platform import Platform


class LongDesk(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=1200)
        width = 192
        height = 96
        self.image = image.load('assets/long_desk.png')
        self.image = transform.scale(self.image, (width, height))
