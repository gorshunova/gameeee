import pygame
from pygame import sprite

import ai_logic
from Sprites import Door
from Sprites.AnimationSprite import AnimationSprite
from Sprites.Platform import Platform


def can_move(player, map_group):
    collide = pygame.sprite.spritecollide(player, map_group, False)
    if collide:
        for block in collide:
            if not block.air:
                return False
    return True


images = {
    "right": (["assets/right.png", "assets/right.png"], 10),
    "left": (["assets/left.png", "assets/left.png"], 10),
    "normal": (["assets/boy.png"], 0)
}


class Player(AnimationSprite):
    MOVE_SPEED = 10
    WIDTH = 96
    HEIGHT = 96
    COLOR = "#FFFFFF"
    JUMP_POWER = 13
    GRAVITY = 0.65

    def __init__(self, x: int, y: int):
        super().__init__(images, 96)

        self.image = self.get_normal_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.onGround = False

        self.velocity = pygame.Vector2(0, 0)

    def update(self, platforms):
        self.process_animation()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.run_animation("left")
            self.velocity.x = - Player.MOVE_SPEED
        if key[pygame.K_RIGHT]:
            self.run_animation("right")
            self.velocity.x = Player.MOVE_SPEED
        if key[pygame.K_UP] and self.onGround:
            self.velocity.y = - Player.JUMP_POWER
            self.onGround = False
            self.onMovingPlatform = False

        if not self.onGround:
            self.velocity.y += Player.GRAVITY
            # if self.velocity.y > 0.65:
            #     self.state = 4

        self.onGround = False
        self.rect.y += self.velocity.y

        self.collide(0, self.velocity.y, platforms)

        if 0 < self.rect.x + self.velocity.x < 5000:
            self.rect.x += self.velocity.x
            self.collide(self.velocity.x, 0, platforms)

        self.velocity.x = 0

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
            if isinstance(platform, Platform):
                if isinstance(platform, Door):
                    platform.active1 = True
                    continue
                if sprite.collide_rect(self, platform):
                    if yvel > 0:
                        self.rect.bottom = platform.rect.top
                        self.onGround = True
                        self.velocity.y = 0
                    if yvel < 0:
                        self.rect.top = platform.rect.bottom
                        self.velocity.y = 0
                    if xvel > 0:
                        self.rect.right = platform.rect.left
                    if xvel < 0:
                        self.rect.left = platform.rect.right

        # speed сюда писать
