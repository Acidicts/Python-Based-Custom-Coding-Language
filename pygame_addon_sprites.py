import pygame


class Sprite:
    def __init__(self, colour, x, y, type, collides=False):
        self.image = pygame.surface.Surface((32, 32))
        self.image.fill(pygame.Color(colour))
        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)
        self.type = type
        self.collides = collides

    def draw(self, screen, x=None, y=None):
        if x is None and y is None:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, (int(x), int(y)))

    def update(self, game):
        pass


class Player(Sprite):
    def __init__(self, colour, x, y, type, game):
        super().__init__(colour, x, y, type)
        self.vec = pygame.math.Vector2(0, 0)
        self.game = game
        self.jump = True
        self.fall_bool = True
        self.fall_height = 0
        self.falling_speed = 0

    def wasd(self, vec):
        self.vec = vec

    def move(self, vec):
        self.rect.x += vec.x
        self.rect.y += vec.y

        for sprite in self.game.sprites:
            if self.rect.colliderect(sprite.rect) and self != sprite and sprite.type == "Collide":
                self.rect.x -= vec.x
                self.rect.y -= vec.y
                self.jump = True
                self.fall_bool = True
                break

    def update(self, game):
        self.rect.x += self.vec.x * 5
        self.rect.y += self.vec.y * 5

        for sprite in game.sprites:
            if self.rect.colliderect(sprite.rect) and self != sprite and sprite.type == "Collide":
                self.rect.x -= self.vec.x * 5
                self.rect.y -= self.vec.y * 5
                self.jump = True
                break


class Collide(Sprite):
    def __init__(self, colour, x, y, type):
        super().__init__(colour, x, y, type)

    def update(self, game):
        pass
