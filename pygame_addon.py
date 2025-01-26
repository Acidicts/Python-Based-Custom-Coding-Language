
import pygame

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
            case 'events':
                self.events()
            case 'is':
                return self.vars(line)
            case 'fill':
                self.fill(line)
            case _:
                print(line.split(maxsplit=1)[1])
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

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def fill(self, line):
        colour = line.split(maxsplit=2)[2]
        print(colour)
        self.screen.fill(colour)
