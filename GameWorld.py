from msvcrt import setmode
import time
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
from GameObjects.Player import Player
from GameObjects.Boss import Boss
from LogSpawnerMan import LogSpawnerMan
from UIElements.ScoreCounter import Counter
from UIElements.MenuScreen import Menu

from GameObjects.Missile import Missile
import StopWatch


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
        self.gaming = False

        self.screen = pygame.display.set_mode((1200, 700))
        self.mytimer = StopWatch.StopWatch()
        self.pausetimer = StopWatch.StopWatch()
        self.now = 0
        pygame.mixer.music.load("SoundEffects/Bongobitches.wav")
        

    @property
    def deltatime(self):
        return self.deltatime

    # endregion

    def get_gameobjects(self):
        return self._gameobjects

    def get_player(self):
        return self._player

    def firstrunint(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("My Pygame window")

    def runpygame(self):
        self.__init__(self) 
        self.score.start_ticks = pygame.time.get_ticks()
        #self.now = pygame.time.get_ticks()
             
        fps = 60.0
        fpsClock = pygame.time.Clock()
        self.deltatime = 1/fps

        log = Log("Sprites\LogSprites\Log1.png", 300, 600, False, 0)
        log.shouldmove = False
        self._gameobjects.append(log)

        # self._gameobjects.append(log)
        player = Player("Sprites/Player/Player1.png")
        player.rect.x = 300
        player.rect.y = 580
        self._player.append(player)
        self.delaychecked = False
        # gameloop
        while not player.isdead:
            self.update(self, self.deltatime)
            self.draw(self, self.screen)
            self.deltatime = fpsClock.tick(fps) / 1000.0
        
        #remove all logs
        tmp = [l for l in self._gameobjects if isinstance(l, Log)]
        for x in tmp:
            self._gameobjects.remove(x)
        self.mytimer.reset()
        self._player.remove(player)
        
        

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if (self.menu.isactive):
            self.menu.menu_update(dt)
        elif (not self.menu.isactive):
            self.mytimer.update(dt)
            self.gamelogic(self, dt)

    def draw(self, screen):
        screen.fill((0, 150, 255))
        if self.menu.isactive:
            self.menu.draw(screen)
        for go in self.get_gameobjects(self):
            go.draw(screen)

        for p in self.get_player(self):
            p.draw(screen)

        if hasattr(self, '_boss'):
            self._boss.draw(screen)

        self.score.draw(screen)

        pygame.display.update()

    def gamelogic(self, dt):
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
        self.score.countup()

        self.openmenu(self)
        

    def openmenu(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            self.menu.isactive = True
            self.pausetimer.reset()

    def createlogs(self):
        self.gwspawns = self.logSpawnerMan.checkready()
        if self.gwspawns is not 0:
            self._gameobjects.append(
                self.logSpawnerMan.spawnLog(self.gwspawns))
        else:
            pass

    def leveltime(self):
        self.now = self.mytimer.get_seconds()
        
        if not self.menu.delaychecked:
            self.delay = pygame.time.get_ticks()
            self.logSpawnerMan.delayspawns(self.delay)
            self.menu.delaychecked = True

        if (self.now - (50 + self.delay/1000) > 0):
            self.newlevel = 6
            self.changelevel(self)
            self.updateboss(self)
        elif (self.now - (40 + self.delay/1000) > 0):
            self.newlevel = 5
            self.changelevel(self)
        elif (self.now - (30 + self.delay/1000) > 0):
            self.newlevel = 4
            self.changelevel(self)
        elif (self.now - (20 + self.delay/1000) > 0):
            self.newlevel = 3
            self.changelevel(self)
        elif (self.now - (10 + self.delay/1000) > 0):
            self.newlevel = 2
            self.changelevel(self)
        elif (self.now - 0 > 0):
            self.newlevel = 1
            self.changelevel(self)
            
            
            
            

    def changelevel(self):
        if self.newlevel > self.currentlevel:
            LogSpawnerMan.disableSpawn(self.logSpawnerMan, self.newlevel)
            if self.newlevel == 1 and self.newlevel > self.currentlevel:
                pygame.mixer.music.play(-1)
            if self.newlevel == 6 and self.newlevel > self.currentlevel:
                self._boss = self.spawnboss(self)
            self.score.multiplier = 1 + (1 * self.newlevel)

            self.currentlevel = self.newlevel
            print(f"you are on level {self.currentlevel}")    
    
    def spawnboss(self):
        boss = Boss("Sprites/Boss.png")
        intshoot = pygame.time.get_ticks()
        self.shootdelay = intshoot
        return boss

        
    
    def updateboss(self):
        if hasattr(self, '_boss'):
            now = pygame.time.get_ticks()
            playerpos = self._player[0].rect.x
            self._boss.move(playerpos)
            if (now - self.shootdelay > 0):
                mispos = self._boss.sprite.rect.x + 180
                missile = Missile("Sprites/Player/player1.png", mispos)
                self._gameobjects.append(missile)
                self.shootdelay += 900

    def collisionCheck(self):
        for p in self._player:
            for go in self._gameobjects:
                # abs to make sure the distance is right regardless of if it's positive or negative
                if (go.tag == "Log" and
                    abs(go.sprite.rect.bottom - p.rect.bottom) < 50 and
                        go.shouldmove):
                    if p.rect.colliderect(go.sprite.rect):

                        go.onCollision(p)
        self.playertouchinglog(self)


    def playertouchinglog(self):
        #check if player is colliding with any log                
        p = self._player[0]
        try:
            collides = [x for x in self._gameobjects if (abs(
                x.sprite.rect.bottom - p.rect.bottom) < 50 and p.rect.colliderect(x.sprite.rect))]
            if isinstance(collides[0], Log):
                p.isdead = False
        except IndexError:
            p.isdead = True
            pygame.mixer.music.stop()



        
if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
