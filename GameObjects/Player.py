

import abc
from overrides import override
import pygame
import GameObject

class Player(GameObject.GameObject):

    #sprite_image = path 
    def __init__(self, sprite_image):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image)
        self.sprite.rect = self.sprite_image.get_rect()
        self.sprite.rect.x = 100
        self.sprite.rect.y = 100
        self.sprites = [pygame.image.load("Sprites/Player/Player1.png"),
               pygame.image.load("Sprites/Player/Player2.png"),
               pygame.image.load("Sprites/Player/Player3.png"),
               pygame.image.load("Sprites/Player/Player4.png"),
               pygame.image.load("Sprites/Player/Player5.png"),
               pygame.image.load("Sprites/Player/Player6.png"),
               pygame.image.load("Sprites/Player/Player7.png")]
        self.current_sprite = self.sprites[0]
        self.moving = False

    #dum navngivning men skal bruges
    value = 0
    moveDistance = 30
    released = True

    
    def update(self, dt):
    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.released:
            self.sprite.rect.y -= self.moveDistance
            self.moving = True
            #self.current_sprite = pygame.transform.rotate(self.sprite_image, 180)         
            self.released = False
        elif keys[pygame.K_s] and self.released:
            self.sprite.rect.y += self.moveDistance      
            self.moving = True
            self.released = False
        elif keys[pygame.K_a] and self.released:
            self.sprite.rect.x -= self.moveDistance
            self.moving = True
            #self.current_sprite = pygame.transform.rotate(self.sprite_image, -90)        
            self.released = False
        elif keys[pygame.K_d] and self.released:
            self.sprite.rect.x += self.moveDistance
            self.moving = True
            #self.current_sprite = pygame.transform.rotate(self.sprite_image, 90)         
            self.released = False

        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_w]:
            self.released = True
            self.current_sprite = self.sprites[0]
            self.moving = False
            #self.sprite_image = pygame.transform.rotate(self.sprite_image, 180)
       
        self.sprite_image = self.current_sprite
        self.animate(dt)
       

        
    
    def onCollision(self, other):
        pass

    #skal finde ud af noget med rotering
    def animate(self, dt):

        
        if self.moving:
         #ikke brugt aligevel da dt er en clock tick fra gameworld
         #self.clock.tick(dt)
        
        
         self.value += 1

         if self.value >= len(self.sprites):
            self.value = 0

         self.current_sprite = self.sprites[self.value]
         pygame.display.update()
        

