from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log

class LogSpawnPoint():


    def __init__(self, x, y, leftdirection, spawntime):
        self.spawnx = x
        self.spawny = y
        self.direction = leftdirection
        self.spawntime = spawntime
        self.spawnEnabled = True
        
        
    
    def spawnready(self):
        now = pygame.time.get_ticks()
        if (now - self.spawntime > 0 and self.spawnEnabled):
            return True
        else:
            return False
    
    
