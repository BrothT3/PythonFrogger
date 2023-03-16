from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
from GameObjects.Player import Player
from LogSpawnerMan import LogSpawnerMan
from UIElements.ScoreCounter import Counter
from UIElements.MenuScreen import Menu


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
        self.deltatime = 0
        self.score = Counter()
        self.menu = Menu()
        self.currentlevel = 0
        self.newlevel = 1

    @property
    def deltatime(self):
        return self.deltatime

    # endregion

    def get_gameobjects(self):
        return self._gameobjects


    def get_player(self):
        return self._player

    def runpygame(self):
        self.__init__(self)
        pygame.init()
        
        
        
        screen = pygame.display.set_mode((800, 700))

        pygame.display.set_caption("My Pygame window")
        fps = 60.0
        fpsClock = pygame.time.Clock()
        self.deltatime = 1/fps

        log = Log("Sprites\LogSprites\Log1.png",300, 600, False)
        log.shouldmove = False
        self._gameobjects.append(log)
        
        #self._gameobjects.append(log)
        player = Player("Sprites/Player/Player1.png")
        player.rect.x = 300
        player.rect.y = 580
        self._player.append(player)
        
        # gameloop
        while True:
            self.update(self, self.deltatime)
            self.draw(self, screen)
            self.deltatime = fpsClock.tick(fps) / 1000.0
            self.score.countup()
        
  


            

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for p in self.get_player(self):
            p.update(dt)
        for go in self.get_gameobjects(self):
            # removes references
            if go.toberemoved:
                self._gameobjects.remove(go)
            else:
                go.update(dt)

        if (self._gameobjects.count(GameObject) <= 8):
            self.createlogs(self)

        self.leveltime(self)
        self.collisionCheck(self)

    def draw(self, screen):
        screen.fill((0, 150, 255))
        
        for go in self.get_gameobjects(self):
            go.draw(screen)

        for p in self.get_player(self):
            p.draw(screen)
        
        self.score.draw(screen)

        
        

        pygame.display.update()

    def createlogs(self):
        self.gwspawns = self.logSpawnerMan.checkready()
        if self.gwspawns is not 0:
            self._gameobjects.append(
                self.logSpawnerMan.spawnLog(self.gwspawns))
        else:
            pass

    def leveltime(self):
        now = pygame.time.get_ticks()

        if (now - 50000 > 0):
            self.newlevel = 6
            self.changelevel(self)
        elif (now - 40000 > 0):
            self.newlevel = 5
            self.changelevel(self)
        elif (now - 30000 > 0):
            self.newlevel = 4
            self.changelevel(self)
        elif (now - 20000 > 0):
            self.newlevel = 3
            self.changelevel(self)
        elif (now - 10000 > 0):
            self.newlevel = 2
            self.changelevel(self)
        elif (now - 100 > 0):
            self.newlevel = 1
            self.changelevel(self)

    def changelevel(self):
        if self.newlevel > self.currentlevel:
            LogSpawnerMan.disableSpawn(self.logSpawnerMan, self.newlevel)
            self.currentlevel = self.newlevel
            print(f"you are on level {self.currentlevel}")

    def collisionCheck(self):
        for p in self._player:
            for go in self._gameobjects:
                #abs to make sure the distance is right regardless of if it's positive or negative
                if  (go.tag == "Log" and 
                    abs(go.sprite.rect.bottom - p.rect.bottom) < 50 and
                    go.shouldmove):
                    if p.rect.colliderect(go.sprite.rect):
                        go.onCollision(p)

                
                    
                

                        


if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
