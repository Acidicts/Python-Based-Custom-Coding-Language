import pygame


class Sprite():
    def __init__(self, colour, x, y):
        self.image = pygame.surface.Surface((32, 32))
        self.image.fill(pygame.Color(colour))
        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

    def draw(self, screen, x=None, y=None):
        if x is None and y is None:
            screen.blit(self.image, self.rect)
        else:
            screen.blit(self.image, (int(x), int(y)))

    def update(self):
        pass
