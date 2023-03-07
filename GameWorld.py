from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
from GameObjects.Player import Player
import random

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class GameWorld(metaclass=Singleton):

    _gameobjects = []

    # region PROPERTIESBIATCH
    # @property
    # def gameObjects(self):
    #     return self.gameObjects

    # @gameObjects.setter
    # def gameObjects(self, value):
    #     self.gameObjects = value
    #     self._gameobjects.add(value)

    # def __init__(self):
    #     self._gameObjects = []

    # endregion
    level = 1
    spawntimer = 1
    spawntimermax = 1

    def get_gameobjects(self):
        return self._gameobjects
    
    def get_gameObjectsCount(self):
        i = 0
        for x in self._gameobjects:
            i += 1
        return i

    def runpygame(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("My Pygame window")
        fps = 60.0
        fpsClock = pygame.time.Clock()
        dt = 1/fps
        
        player = Player()
        self._gameobjects.append(player)
        # log = Log()
        # log.sprite.rect.x = 200
        # log.sprite.rect.y = 150
        # self._gameobjects.append(log)
        # log2 = Log()
        # log2.sprite.rect.x = 500
        # log2.sprite.rect.y = 300
        # self._gameobjects.append(log2)
        # print(log.sprite.rect)
        # print(log2.sprite.rect)
        
        
        # gameloop
        while True:
            self.update(self, dt)
            self.draw(self, screen)
            dt = fpsClock.tick(fps)

    # @abc.abstractclassmethod
    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for go in self.get_gameobjects(self):
            go.update(dt)
        self.spawnlog(self, dt)

  # @abc.abstractclassmethod
    def draw(self, screen):
        screen.fill((0, 0, 0))
        for go in self.get_gameobjects(self):
            screen.blit(go.sprite_image, go.sprite.rect)
        pygame.display.update()

    def spawnlog(self, dt):
        self.spawntimer -= dt
        amount = self.get_gameObjectsCount(self)
        while amount < (7- self.level) and self.spawntimer <= 10:   
            self._gameobjects.append(Log())
            amount = self.get_gameObjectsCount(self)
            self.spawntimer = self.spawntimermax

if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
