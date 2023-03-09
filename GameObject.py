
import abc

import pygame

class GameObject(metaclass=abc.ABCMeta):

    #if you remove the sprite in constructor it no longer works
    def __init__(self, sprite, sprite_image):
        self.sprite = pygame.sprite.Sprite()
        self.sprite_image = pygame.image.load(sprite_image)

    @abc.abstractclassmethod
    def update(self, dt):
        pass

    @abc.abstractclassmethod
    def onCollision(self, other):
        pass
