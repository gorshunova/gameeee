from pygame import sprite, Surface

from Sprites.Platform import Platform


class Ground(Platform):
    def __init__(self, *groups: sprite.AbstractGroup):
        super().__init__(*groups, x=0, y=750, width=1000, height=50)
        self.image = Surface((1000, 50))
        self.image.fill((165, 227, 136))
