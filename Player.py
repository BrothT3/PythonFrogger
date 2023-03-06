

import pygame


class Player():

    sprite_image =  pygame.image.load("player.png")

    sprite = pygame.sprite.Sprite()

    sprite.rect = sprite_image.get_rect()
    sprite.rect.x = 100
    sprite.rect.y = 100

    def update(self, dt):
        self.sprite.rect.x += 1
