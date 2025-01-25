import pygame
import Sprites


from Sprites import Player, Platform, Player2
from Sprites.Player2 import Player2
from Sprites.Ground import Ground
from TestJson import parse_json

WIDTH = 1200
HEIGHT = 700



screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
FRAMERATE = 60


background = pygame.image.load("./assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

levels = list(parse_json())

sprites = levels[0]
scores_sprites = pygame.sprite.Group()

# player = Sprites.Player(32, 518)
# sprites.add(player)
#
# player_2 = Sprites.Player2.Player2(80, 518)
# sprites.add(player_2)


#scores_sprites.add(*scores)
#sprites.add(*scores)
platforms: list[Platform] = [Ground(sprites, h=HEIGHT-32)]

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

    sprites.update(platforms=sprites)

    # screen.blit(background, (0, 0))
    screen.fill((232, 228, 190))
    # for platform in platforms:
    #     screen.blit(platform.image, platform.rect.topleft)

    sprites.draw(screen)
    pygame.display.flip()


pygame.quit()