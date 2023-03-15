from msvcrt import setmode
import pygame, sys
from GameObject import GameObject
from GameObjects.Log import Log
import random
from GameObjects.LogSpawnPoint import LogSpawnPoint
from collections import Counter


class LogSpawnerMan():

    def __init__(self):
        self.spawnpoints = [LogSpawnPoint(-500, 0, True, 0),
                            LogSpawnPoint(810, 100, False, random.randint(0, 300)),
                            LogSpawnPoint(-500, 200, True, random.randint(0, 700)),
                            LogSpawnPoint(810, 300, False, random.randint(100, 2100)),
                            LogSpawnPoint(-500, 400, True, random.randint(200, 1500)),
                            LogSpawnPoint(810, 500, False, random.randint(300, 2250))]
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
            
            
            match logtype:
                case 0:
                    spawntimeplus = random.randint(3000, 4000)
                case 1:
                    spawntimeplus = random.randint(4500, 5250)
                case 2:
                    spawntimeplus = random.randint(6000, 7500)
            currentspawn.spawntime += spawntimeplus
            
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
        
    def disableSpawn(self, newlevel):
        currentlevel = newlevel -1
        i = 0
        for x in self.spawnpoints:
            if (currentlevel == 0):
                break
            x.spawnEnabled = False
            i += 1
            if i >= currentlevel:
                break
            

    