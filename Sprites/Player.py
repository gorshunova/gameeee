import pygame
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
    "falling": ([
                    "assets/jump.png",
                    "assets/right.png",
                    "assets/left.png"
                ], 5),
    "normal": (["assets/boy.png"], 0)
}


#поменять картинки


class Player(AnimationSprite):
    def __init__(self, x: int, y: int):
        super().__init__(images)

        self.image = self.get_normal_image()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.__speed = 5

    def update(self):
        self.process_animation()

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.run_animation("falling")

    def compute(self, scores, map_group):
        x, y = self.rect.center
        score_x, score_y = ai_logic.get_min_lenght_score(
            x, y, list(map(lambda x: x.rect.center, scores))
        )
        virtual_player = Player(*self.rect.topleft)
        virtual_player.rect.center = ai_logic.move(x, y, score_x, score_y, self.__speed)
        if can_move(virtual_player, map_group):
            self.rect.center = virtual_player.rect.center


        #speed сюда писать





