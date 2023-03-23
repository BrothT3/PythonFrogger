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

    def __init__(self):
        self.logSpawnerMan = LogSpawnerMan()
        self.deltatime = 0
        self.score = Counter()
        self.currentlevel = 0
        self.newlevel = 1
        self.gaming = False
        self.mytimer = StopWatch.StopWatch()
        self.now = 0
        pygame.mixer.music.load("SoundEffects/Bongobitches.wav")
        

    @property
    def deltatime(self):
        return self.deltatime

    def getcount(self):
        return len(self._gameobjects)
    def get_gameobjects(self):
        return self._gameobjects

    def get_player(self):
        return self._player

    def firstruninit(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Frogger")
        self.screen = pygame.display.set_mode((1200, 700))
        self.deathsound = pygame.mixer.Sound("SoundEffects/plunk.wav")
        self.menu = Menu()

    def runpygame(self):
        self.__init__(self) 
        self.score.start_ticks = pygame.time.get_ticks()

             
        fps = 60.0
        fpsClock = pygame.time.Clock()
        self.deltatime = 1/fps

        log = Log("Sprites\LogSprites\Log1.png", 300, 600, False, 0)
        log.shouldmove = False
        self._gameobjects.append(log)

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
        
        #region GameWorldCleanUp
        #remove all logs and missiles when it breaks gameloop
        tmp = [l for l in self._gameobjects if isinstance(l, Log) or isinstance(l, Missile)]
        #because iterating through the list normally doesn't work..
        for x in tmp:
            self._gameobjects.remove(x)
        self.mytimer.reset()
        self._player.remove(player)
        if hasattr(self, '_boss'):
            del(self._boss)
        self.menu.currentscore = self.score.seconds
        self.deathsound.play()
        self.menu.isactive = True
        #endregion
        

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
        
        for go in self.get_gameobjects(self):
            go.draw(screen)


        if self.menu.isactive:
            self.menu.draw(screen)

        else:
            self.score.draw(screen)


        for p in self.get_player(self):
            p.draw(screen)

        if hasattr(self, '_boss'):
            self._boss.draw(screen)

        if self.menu.isactive:
            self.menu.draw(screen)
        else:
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
        #amount of logs that can be spawned at a time
        if (len(self.get_gameobjects(self)) <= 12):
            self.createlogs(self)
           

        self.leveltime(self)
        self.collisionCheck(self)
        self.score.countup()
        self.openmenu(self)
        

    def openmenu(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            self.menu.isactive = True
            self.pausesecs = self.mytimer.get_seconds()


    def createlogs(self):
        self.gwspawns = self.logSpawnerMan.checkready()
        try:
         if len(self.gwspawns) < 8:
            self._gameobjects.append(
                self.logSpawnerMan.spawnLog(self.gwspawns))  
         else:
             pass
        except TypeError:
            pass

    def leveltime(self):
        self.now = self.mytimer.get_seconds()
        
        if not self.menu.delaychecked:
            self.delay = pygame.time.get_ticks()
            self.logSpawnerMan.delayspawns(self.delay)
            self.menu.delaychecked = True



        if ((self.now) - (50) > 0):
            self.newlevel = 6
            self.changelevel(self)
            self.updateboss(self)

        elif (self.now - (40) > 0):
            self.newlevel = 5
            self.changelevel(self)

        elif (self.now - (30) > 0):
            self.newlevel = 4
            self.changelevel(self)

        elif (self.now - (20) > 0):
            self.newlevel = 3
            self.changelevel(self)

        elif (self.now - (10) > 0):
            self.newlevel = 2
            self.changelevel(self)

        elif (self.now - 0 > 0):
            self.newlevel = 1
            self.changelevel(self)
            
            
            
    def changelevel(self):
        if self.newlevel > self.currentlevel:
            self.logSpawnerMan.disableSpawn(self.newlevel)
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
                missile = Missile("Sprites/Laser.png", mispos)
                missile.tag = "Missile"
                self._gameobjects.append(missile)
                self.shootdelay += 900

    def collisionCheck(self):
        self.playertouchinglog(self)
        for p in self._player:
            for go in self._gameobjects:
                # abs to make sure the distance is right regardless of if it's positive or negative
                if (go.tag == "Log" and
                    abs(go.sprite.rect.bottom - p.rect.bottom) < 50 and
                        go.shouldmove):
                    if p.rect.colliderect(go.sprite.rect):
                        go.onCollision(p)
                if (go.tag == "Missile" and 
                    abs(go.sprite.rect.bottom - p.rect.bottom) < 20):
                      if p.rect.colliderect(go.sprite.rect):
                       p.isdead = True
                       self.logSpawnerMan.resetspawns()
                       self.delaychecked = False

       

    #check if player is colliding with any log      
    def playertouchinglog(self):
        p = self._player[0]
        #if collides finds nothing it can't make a list and index first spot
        #so if it throws an exception player is no longer touching.....
        #I miss C#
        try:
            collides = [x for x in self._gameobjects if (abs(
                x.sprite.rect.bottom - p.rect.bottom) < 40 and p.rect.colliderect(x.sprite.rect))]
            if isinstance(collides[0], Log):
                p.isdead = False
        except IndexError:
            self.menu.currentscore = self.score.seconds
            p.isdead = True
            self.logSpawnerMan.resetspawns()
            self.delaychecked = False
            pygame.mixer.music.stop()



        
if __name__ == '__main__':

    GameWorld.runpygame(GameWorld)
