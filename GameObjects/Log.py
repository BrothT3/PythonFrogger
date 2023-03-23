
import random
import abc
from overrides import override
import pygame
import GameObject
import GameWorld
from StopWatch import StopWatch

class Log(GameObject.GameObject):


    def __init__(self, sprite_image, x, y, directionleft, movespeed):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Log", False)
        self.sprite.rect = self.sprite_image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.direction = directionleft 
        self.movespeed = float(movespeed)     
        self.shouldmove = True



       
    @property
    def shouldmove(self):
        return self._shouldmove
    
    @shouldmove.setter
    def shouldmove(self, value):
        self._shouldmove = value
        self.stopwatch = StopWatch()
   
    def determineLane(self):
        if not self.lanedetermined:
            self.lane = random.randint(0, 5)
            self.sprite.rect.x = self.lanesX[self.lane]
            self.sprite.rect.y = self.lanesY[self.lane]
            
            self.lanedetermined = True
        
        
    def move(self):
        if self.direction == True:
            self.sprite.rect.x += self.movespeed
        else:
            self.sprite.rect.x -= self.movespeed

        if self.sprite.rect.x < -600:
            self.toberemoved = True
        elif self.sprite.rect.x >= 1250:
            self.toberemoved = True
        if self.sprite.rect.y <= -100:
            self.toberemoved = True
        elif self.sprite.rect.y >= 700:
            self.toberemoved = True


    @override
    def update(self, dt):
        
        if self.shouldmove:
            self.move()

        if hasattr(self, 'stopwatch'):
            self.stopwatch.update(dt)
            if self.stopwatch.countdown >= 10:
                self.toberemoved = True
        
    @override
    def draw(self, screen):
        screen.blit(self.sprite_image, self.sprite.rect)
  


    @override
    def onCollision(self, other):    
        if self.direction:
            other.rect.x += self.movespeed
        else:
            other.rect.x -= self.movespeed






    

    

