

import abc
from overrides import override
import pygame
import GameObject

class Player(GameObject.GameObject):



    sprite_image =  pygame.image.load("Sprites/player.png")

    sprite = pygame.sprite.Sprite()

    sprite.rect = sprite_image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100

    moveDistance = 30
    released = True

    
    def update(self, dt):
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.released:
            self.sprite.rect.y -= self.moveDistance
            self.released = False
        elif keys[pygame.K_s] and self.released:
            self.sprite.rect.y += self.moveDistance
            self.released = False
        elif keys[pygame.K_a] and self.released:
            self.sprite.rect.x -= self.moveDistance
            self.released = False
        elif keys[pygame.K_d] and self.released:
            self.sprite.rect.x += self.moveDistance
            self.released = False

        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_w]:
            self.released = True
    
    def onCollision(self, other):
        pass



    

    

