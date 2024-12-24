import pygame
import Sprites
import random

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
FRAMERATE = 60


background = pygame.image.load("./assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

sprites = pygame.sprite.Group()
scores_sprites = pygame.sprite.Group()

player = Sprites.Player(200, 80)
sprites.add(player)

#scores_sprites.add(*scores)
#sprites.add(*scores)

while running:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_SPACE:
                    up = True
                case pygame.K_LEFT:
                    left = True
                case pygame.K_RIGHT:
                    right = True
                case pygame.K_SPACE:
                    space = True
                case pygame.K_LSHIFT:
                    shift = True
        elif event.type == pygame.KEYUP:
            match event.key:
                case pygame.K_SPACE:
                    up = False
                case pygame.K_LEFT:
                    left = False
                case pygame.K_RIGHT:
                    right = False
                case pygame.K_SPACE:
                    space = False
                case pygame.K_LSHIFT:
                    shift = False

    sprites.update()

    screen.blit(background, (0, 0))
    sprites.draw(screen)
    pygame.display.flip()

platforms: list[Platform] = [
    Ground(entities)
]
def spawn_platform():
    cat_x, cat_y = cat.rect.center
    platform = Platform(entities, x=0, y=0)

    platforms.append(platform)


pygame.quit()