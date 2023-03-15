

import abc
from overrides import override
import pygame
import GameObject


class Player(GameObject.GameObject):

    # sprite_image = path
    def __init__(self, sprite_image):
        self.sprite = pygame.sprite.Sprite()
        super().__init__(self.sprite, sprite_image, "Player", False)
        self.sprite.rect = self.sprite_image.get_rect()
        self.rect = self.sprite_image.get_rect() 
        self.sprites = [pygame.image.load("Sprites/Player/Player1.png"),
                        pygame.image.load("Sprites/Player/Player2.png"),
                        pygame.image.load("Sprites/Player/Player3.png"),
                        pygame.image.load("Sprites/Player/Player4.png"),
                        pygame.image.load("Sprites/Player/Player5.png"),
                        pygame.image.load("Sprites/Player/Player6.png"),
                        pygame.image.load("Sprites/Player/Player7.png")]
        self.current_sprite = self.sprites[0]
        self.lastupdated = 0
        self.current_frame = 0
        self.moving = False
        self.animdone = True


    moveDistance = 80
    released = True

    @override
    def update(self, dt):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w] and self.released:
            self.rect.y -= self.moveDistance
            self.moving = True
            self.released = False
        elif keys[pygame.K_s] and self.released:
            self.rect.y += self.moveDistance
            self.moving = True
            self.released = False
        elif keys[pygame.K_a] and self.released:
            self.rect.x -= self.moveDistance 
            self.moving = True
            self.released = False
        elif keys[pygame.K_d] and self.released:
            self.rect.x += self.moveDistance
            self.moving = True
            self.released = False

        if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_s] and not keys[pygame.K_w]:
            self.released = True
            self.moving = False

        self.animate()

        if self.moving:
            self.animdone = False

        #keep player inside screen
        if self.rect.x <= 10:
            self.rect.x = 15
        elif self.rect.x >= 750:
            self.rect.x = 730
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 500:
            self.rect.y = 500

    @override
    def onCollision(self, other):
        pass
        #self.sprite.rect.x += other.sprite.rect.x
        #self.move(other)
        #print(self.rect.x)

    def move(self, other):
        movement = self.rect.x + other.rect.x 
        self.rect.x += movement 

    def animate(self):
        now = pygame.time.get_ticks()

        #if its longer than 25milisec since last update
        if now - self.lastupdated > 25 and not self.animdone:
            self.lastupdated = now

            #keeps it in full numbers
            self.current_frame = (self.current_frame + 1) % len(self.sprites)
            self.current_sprite = self.sprites[self.current_frame]

            if self.current_frame == 6:
                self.animdone = True

    @override
    def draw(self, screen):
        red = (255, 0, 0)
        screen.blit(self.current_sprite, self.rect)
        pygame.draw.rect(self.current_sprite, red, [0,0, self.rect.width, self.rect.height], 1)

        
        
