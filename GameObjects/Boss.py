import random
import abc
from overrides import override
import pygame
import GameObject



class Boss(GameObject.GameObject):

    def __init__(self, sprite_image):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Player", False)
        self.shootdelay = 0
        self.missiles = []
        self.sprite.rect = self.sprite_image.get_rect()
        self.rect = self.sprite_image.get_rect() 
        self.posx = 0

    def move(self, playerpos):
        destination = random.randint(playerpos -10, playerpos + 10)
        if self.sprite.rect.x < destination:
            self.sprite.rect.x += 4
        elif self.sprite.rect.x > destination:
            self.sprite.rect.x -= 4

        
        

