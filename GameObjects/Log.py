
import random
import abc
from overrides import override
import pygame
import GameObject

class Log(GameObject.GameObject):



    sprite_image =  pygame.image.load("Sprites/player.png")

    sprite = pygame.sprite.Sprite()

    sprite.rect = sprite_image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100

    
    lanedetermined = False
    lane = 0
    lanesX = [0, 710, 0, 710, 0, 710]
    lanesY = [0, 100, 200, 300, 400, 500]
    def determineLane(self):
        if not self.lanedetermined:
            self.lane = random.randint(0, 5)
            self.sprite.rect.x = self.lanesX[self.lane]
            self.sprite.rect.y = self.lanesY[self.lane]
            
            self.lanedetermined = True
        
    def move(self):
        if self.lane == 0 or self.lane == 3 or self.lane == 5:
            self.sprite.rect.x += 3
        else:
            self.sprite.rect.x -= 3
        
        if (self.sprite.rect.x == -10 or self.sprite.rect.x == 810):
            pass

    def update(self, dt):
        self.determineLane()
        self.move()

    
    def onCollision(self, other):
        pass
        # if other.tag == "log"
            #lanedetermined = false



    

    

