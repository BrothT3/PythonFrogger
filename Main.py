from msvcrt import setmode
import pygame


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class GameWorld(metaclass=Singleton):

    @property
    def gameObjects(self):
        return self.gameObjects

    @gameObjects.setter
    def gameObjects(self, value):
        self.gameObjects = value

    def __init__(self):
        self._gameObjects = []

    def runpygame(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("My Pygame window")
        fps = 60.0
        fpsClock = pygame.time.Clock()
        dt = 1/fps

        # gameloop
        while True:
            self.update(self, dt)
            self.draw(self, screen)
            dt = fpsClock.tick(fps)

    #@abc.abstractclassmethod
    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

  # @abc.abstractclassmethod
    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.display.update()


if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
