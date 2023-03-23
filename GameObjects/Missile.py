import abc
from overrides import override
import pygame
import GameObject


class Missile(GameObject.GameObject):

    def __init__(self, sprite_image, position):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Log", False)
        self.sprite.rect = self.sprite_image.get_rect()
        self.rect = self.sprite_image.get_rect() 
        self.sprite.rect.x = position
        self.sprite.rect.y = 30
        self.shouldmove = True

    @override
    def update(self, dt):
        self.move()
    
    def move(self):
        self.sprite.rect.y += 8

        if self.sprite.rect.x < -600:
            self.toberemoved = True
        elif self.sprite.rect.x >= 1250:
            self.toberemoved = True
        if self.sprite.rect.y <= -100:
            self.toberemoved = True
        elif self.sprite.rect.y >= 700:
            self.toberemoved = True
    
    def onCollision(self, other):
        pass