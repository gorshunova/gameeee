import pygame
from pygame import sprite

import ai_logic
from Sprites.AnimationSprite import AnimationSprite


def can_move(player, map_group):
    collide = pygame.sprite.spritecollide(player, map_group, False)
    if collide:
        for block in collide:
            if not block.air:
                return False
    return True


images = {
    'right': (["assets/right.png"], 10),
    'left': (["assets/left.png", "assets/left.png"], 10),
    "normal": (["assets/boy.png"], 0)
}


# поменять картинки


class Player(AnimationSprite):
    MOVE_SPEED = 10
    WIDTH = 64
    HEIGHT = 64
    COLOR = "#FFFFFF"
    JUMP_POWER = 13
    GRAVITY = 0.65

    def __init__(self, x: int, y: int):
        super().__init__(images)
        self.image = self.get_normal_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.onGround = False
        self.__speed = 5

    def update(self):
        self.process_animation()
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.run_animation("left")

    def compute(self, scores, map_group):
        x, y = self.rect.center
        score_x, score_y = ai_logic.get_min_lenght_score(
            x, y, list(map(lambda x: x.rect.center, scores))
        )
        virtual_player = Player(*self.rect.topleft)
        virtual_player.rect.center = ai_logic.move(x, y, score_x, score_y, self.__speed)
        if can_move(virtual_player, map_group):
            self.rect.center = virtual_player.rect.center

    def collide(self, xvel, yvel, platforms):
        if platforms is None:
            return

        for platform in platforms:
            if sprite.collide_rect(self, platform):
                if yvel > 0:
                    self.rect.bottom = platform.rect.top
                    self.onGround = True
                    self.velocity.y = 0
                    if isinstance(platform):
                        self.velocity.x = platform.speed_x
                if yvel < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0

                if xvel > 0:
                    self.rect.right = platform.rect.left
                if xvel < 0:
                    self.rect.left = platform.rect.right

        # speed сюда писать
