from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
from GameObjects.Player import Player
from LogSpawnerMan import LogSpawnerMan

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class GameWorld(metaclass=Singleton):

    _gameobjects = []
    _player = []

    # region PROPERTIESBIATCH
    # @property
    # def gameObjects(self):
    #     return self.gameObjects

    # @gameObjects.setter
    # def gameObjects(self, value):
    #     self.gameObjects = value
    #     self._gameobjects.add(value)

    def __init__(self):
        self.logSpawnerMan = LogSpawnerMan()

    # endregion

    def get_gameobjects(self):
        return self._gameobjects
    
    def get_player(self):
        return self._player

    def runpygame(self):
        self.__init__(self)
        pygame.init()
        screen = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("My Pygame window")
        fps = 60.0
        fpsClock = pygame.time.Clock()
        dt = 1/fps

        player = Player("Sprites/Player/Player1.png")
        self._player.append(player)
        
        



        # gameloop
        while True:
            self.update(self, dt)
            self.draw(self, screen)
            #dt = fpsClock.tick(fps) / 1000.0
            dt = fpsClock.tick(fps) 


    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for p in self.get_player(self):
            p.update(dt)
        for go in self.get_gameobjects(self):
            go.update(dt)
        if(self._gameobjects.count(GameObject) <= 8):
            self.createlogs(self)



    def draw(self, screen):
        screen.fill((0, 0, 0))
        
        for go in self.get_gameobjects(self):
           go.draw(screen) 
           
        for p in self.get_player(self):
            p.draw(screen)
            
        pygame.display.update()
    def createlogs(self):
        self.gwspawns = self.logSpawnerMan.checkready()
        if self.gwspawns is not 0:
            self._gameobjects.append(self.logSpawnerMan.spawnLog(self.gwspawns))
        else:
            pass

if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
