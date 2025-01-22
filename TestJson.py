import json

import pygame.sprite

from Sprites import *

def parse_json():
    with open('m.json') as file:
        file_parse = json.load(file)

        for l in file_parse:
            level = pygame.sprite.Group()
            for item in l:
                cls = item.get('class', None)
                x = item.get('x', 0)
                y = item.get('y', 0)

                if cls is None:
                    continue

                if cls == 'Player':
                    sprite = Player(x, y)
                    level.add(sprite)
                elif cls == 'Player2':
                    sprite = Player2(x, y)
                    level.add(sprite)
                elif cls == 'Desk':
                    sprite = Desk(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'LongDesk':
                    sprite = LongDesk(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'Shelf':
                    sprite = Shelf(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'Door':
                    sprite = Door(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'Window':
                    sprite = Window(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'Bookcase':
                    sprite = Bookcase(level, l=x, h=y)
                    level.add(sprite)
                elif cls == 'Scores':
                    sprite = Scores(level, x, y)
                    level.add(sprite)
                elif cls == 'ScoresGirl':
                    sprite = ScoresGirl(level, x, y)
                    level.add(sprite)
                elif cls == 'ScoresBoy':
                    sprite = ScoresBoy(level, x, y)
                    level.add(sprite)

        yield level


