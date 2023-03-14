
import random
import abc
from overrides import override
import pygame
import GameObject

class Log(GameObject.GameObject):


    def __init__(self, sprite_image, x, y, directionleft):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Log")
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
        # if self.lane == 0 or self.lane == 3 or self.lane == 5:
        #     self.sprite.rect.x += 3
        # else:
        #     self.sprite.rect.x -= 3
        
        # if (self.sprite.rect.x == -10 or self.sprite.rect.x == 810):
        #     pass
        if self.direction == True:
            self.sprite.rect.x += 3
        else:
            self.sprite.rect.x -= 3


    @override
    def update(self, dt):
        #self.determineLane()
        self.move()


    @override
    def onCollision(self, other):     
        other.rect.x -= (other.rect.x - self.sprite.rect.x) * float(7) /1700




    

    

