
import abc

import pygame

class GameObject():

    #if you remove the sprite in constructor it no longer works
    def __init__(self, sprite, sprite_image, tag, toberemoved):
        self.sprite = pygame.sprite.Sprite()
        self.sprite_image = pygame.image.load(sprite_image)
        self.tag = tag
        self.toberemoved = toberemoved

    
    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.sprite_image, self.sprite.rect)
        


    def onCollision(self, other):
        pass

    

