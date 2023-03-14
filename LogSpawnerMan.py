from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
import random
from GameObjects.LogSpawnPoint import LogSpawnPoint
from collections import Counter


class LogSpawnerMan():

    def __init__(self):
        self.spawnpoints = [LogSpawnPoint(0, 0, True, 0),
                            LogSpawnPoint(710, 100, False, random.randint(0, 300)),
                            LogSpawnPoint(0, 200, True, random.randint(0, 700)),
                            LogSpawnPoint(710, 300, False, random.randint(100, 1100)),
                            LogSpawnPoint(0, 400, True, random.randint(200, 500)),
                            LogSpawnPoint(710, 500, False, random.randint(300, 1250))]
        self.logsprites = ["Sprites\LogSprites\Log1.png",
                           "Sprites\LogSprites\Log2.png",
                           "Sprites\LogSprites\Log3.png"]
        self.logamount = 0
        
    def update(self, dt):
        pass

    def spawnLog(self, gwspawns):      
            readyspawns = gwspawns
            readyamount = readyspawns.count(LogSpawnPoint)
            lane = random.randint(0, readyamount)
            currentspawn = readyspawns[lane]
            logtype = random.randint(0, 2)

            log = Log(self.logsprites[logtype], currentspawn.spawnx, currentspawn.spawny, currentspawn.direction)
            
            spawntimeplus = random.randint(1200, 1800)
            currentspawn.spawntime += spawntimeplus + (0 + (logtype * 0.5)) * 1000
            
            return log
        
    def checkready(self):
        _readySpawns = []
        readyamount = 0
        for x in self.spawnpoints:
            if x.spawnready():
                _readySpawns.append(x)  
                readyamount+=1
        if (readyamount <= 0):
            return 0
        if (readyamount >= 1):
            return _readySpawns

    