import pygame
from pygame_addon_sprites import *


class Game:
    def __init__(self, ev):
        self.inteprt = ev

        pygame.init()

        self.screen = None
        self.clock = None
        self.running = False
        self.sprites = []

    def ev(self, line):
        match line.split()[1]:
            case 'init':
                self.init(line)
            case 'update':
                try:
                    pygame.display.flip()
                except Exception as e:
                    print(e)
                    pass
            case 'sprite':
                self.sprite(line)
            case 'events':
                self.events()
            case 'is':
                return self.vars(line)
            case 'fill':
                self.fill(line)
            case 'draw':
                self.draw()
            case 'add':
                self.add_sprite(line)
            case 'wasd':
                self.wasd()
            case 'space':
                keys = pygame.key.get_pressed()
                for sprite in self.sprites:
                    if sprite.type == "Player" and keys[pygame.K_SPACE] and sprite.jump:
                        sprite.jump = False
                        sprite.move(pygame.math.Vector2(0, -100))
            case 'clock':
                self.clock.tick(int(line.split()[2]))
            case _:
                print(line.split(maxsplit=1)[1])
                print("Unknown command")

    def wasd(self):
        for sprite in self.sprites:
            if sprite.type == "Player":
                self.wasd_move(sprite)

    @staticmethod
    def wasd_move(sprite):
        keys = pygame.key.get_pressed()
        vec = pygame.math.Vector2(0, 0)
        vec.x = keys[pygame.K_d] - keys[pygame.K_a]
        vec.y = keys[pygame.K_s] - keys[pygame.K_w]

        if vec.length() > 0:
            vec.normalize_ip()

        sprite.wasd(vec)

    def sprite(self, line):
        match line.split()[2]:
            case 'add':
                self.add_sprite(line)
            case 'update':
                self.update()
            case 'move':
                sprite = self.sprites[int(line.split()[3])]
                if sprite.type != "Player":
                    sprite.rect.x += int(line.split()[4])
                    sprite.rect.y += int(line.split()[5])
                else:
                    sprite.move(pygame.math.Vector2(int(line.split()[4]), int(line.split()[5])))
            case _:
                print("Unknown command")

    def vars(self, line):
        match line.split()[2]:
            case 'running':
                return self.running
            case _:
                print("Unknown variable")

    def init(self, line):
        w = line.split()[2]
        h = line.split()[3]
        try:
            title = line.split()[4]
            pygame.display.set_caption(title)
        except Exception as e:
            print(e)
            pass

        self.screen = pygame.display.set_mode((int(w), int(h)))
        self.clock = pygame.time.Clock()
        self.running = True

        print(f"Game initialized with size ( {w} x {h} )")
        print(" ")

    def draw(self):
        for sprite in self.sprites:
            sprite.draw(self.screen)

    def update(self):
        for sprite in self.sprites:
            sprite.update(self)

    def add_sprite(self, line):
        if line.split()[6] == "Collide":
            x = line.split()[3]
            y = line.split()[4]
            type = line.split()[6]
            colour = line.split()[5]
            self.sprites.append(Collide(colour, x, y, type))
        elif line.split()[6] == "Player":
            x = line.split()[3]
            y = line.split()[4]
            type = line.split()[6]
            colour = line.split()[5]
            self.sprites.append(Player(colour, x, y, type, self))
        else:
            x = line.split()[3]
            y = line.split()[4]
            type = line.split()[6]
            colour = line.split()[5]
            self.sprites.append(Sprite(colour, x, y, type))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def fill(self, line):
        colour = line.split(maxsplit=2)[2]
        colour = (int(colour.split()[0]), int(colour.split()[1]), int(colour.split()[2]))
        self.screen.fill(colour)
