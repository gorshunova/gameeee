from pygame import sprite, image, transform

from Sprites.Platform import Platform


class Window(Platform):
    def __init__(self, *groups: sprite.AbstractGroup, l, h):
        super().__init__(*groups, x=l, y=h, width=1200)
        width = 192
        height = 192
        self.image = image.load('assets/window.png')
        self.image = transform.scale(self.image, (width, height))
