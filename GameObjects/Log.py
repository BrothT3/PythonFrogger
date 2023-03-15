
import random
import abc
from overrides import override
import pygame
import GameObject
import GameWorld

class Log(GameObject.GameObject):


    def __init__(self, sprite_image, x, y, directionleft):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Log", False)
        self.sprite.rect = self.sprite_image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        self.direction = directionleft      
        # self.lane = 0
        # self.lanedetermined = False
        # self.lanesX = [0, 710, 0, 710, 0, 710]
        # self.lanesY = [0, 100, 200, 300, 400, 500]
        # self.sprite.rect = self.sprite_image.get_rect()
        # self.determineLane()



       
              
   
    def determineLane(self):
        if not self.lanedetermined:
            self.lane = random.randint(0, 5)
            self.sprite.rect.x = self.lanesX[self.lane]
            self.sprite.rect.y = self.lanesY[self.lane]
            
            self.lanedetermined = True
        
        
    def move(self):
        if self.direction == True:
            self.sprite.rect.x += 2
        else:
            self.sprite.rect.x -= 2

        #slettes når de når de her værdier, men værden bliver mindre og mindre 
        #hver gang så skal modificeres
        if self.sprite.rect.x < -600:
            self.toberemoved = True
        elif self.sprite.rect.x >= 900:
            self.toberemoved = True
        if self.sprite.rect.y <= -100:
            self.toberemoved = True
        elif self.sprite.rect.y >= 700:
            self.toberemoved = True


    @override
    def update(self, dt):
        #self.determineLane()
        self.move()


    @override
    def onCollision(self, other):    
        dt = GameWorld.GameWorld.deltatime
        if self.direction:
            other.rect.x += (other.rect.x - self.sprite.rect.x ) * dt 
        else:
            other.rect.x -= (other.rect.x - self.sprite.rect.x) * dt 
        # if self.direction:
        #     other.rect.x += ((other.rect.x - self.sprite.rect.x ) * float(7)) / 225
        # else:
        #     other.rect.x -= ((other.rect.x - self.sprite.rect.x) * float(7)) / 225

        #other.rect.x -= (other.rect.x - self.sprite.rect.x) * float(7) /1700





    

    

