import pygame
import Sprites
import random

from Sprites import Player, Platform
from Sprites.Ground import Ground

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

player = Sprites.Player(400, 518)
sprites.add(player)

#scores_sprites.add(*scores)
#sprites.add(*scores)
platforms: list[Platform] = [Ground(sprites, h=HEIGHT-32)]

def spawn_platform():
    platform = Platform.Platform(sprites, x=500, y=690)
    platforms.append(platform)

while running:
    clock.tick(FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
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
            if event.key == pygame.K_ESCAPE:
                running = False
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

    sprites.update(platforms=platforms)

    # screen.blit(background, (0, 0))
    screen.fill((0, 0, 0))
    for platform in platforms:
        screen.blit(platform.image, platform.rect.topleft)

    sprites.draw(screen)
    pygame.display.flip()


pygame.quit()