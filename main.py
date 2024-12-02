import pygame
import Sprites

WIDTH = 1000
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

sprites = pygame.sprite.Group()
scores_sprites = pygame.sprite.Group()

player = Sprites.Player(
    ...
)
sprites.add(player)

#scores_sprites.add(*scores)
#sprites.add(*scores)

while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sprites.update()
    player.compute(scores_sprites)

    screen.fill((128, 128, 128))
    sprites.draw(screen)
    pygame.display.flip()


pygame.quit()