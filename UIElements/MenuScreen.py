import sys
import pygame


class Menu():

    def __init__(self):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.sprite = pygame.sprite.Sprite()
        self.sprite_image = pygame.image.load("Sprites/frogger1.png")
        self.sprite.rect = self.sprite_image.get_rect()
        self.welcomebutton = self.my_font.render(
            "Click To Play", False, (255, 255, 255))
        self.exitbutton = self.my_font.render("Exit", False, (255, 0, 0))
        self.ebuttonrect = pygame.Rect(750, 500, 50, 50)
        # self.rect = self.text_surface.get_rect()
        self.wbuttonrect = pygame.Rect(250, 500, 220, 50)
        self.wsurface = pygame.Surface((self.wbuttonrect.width, self.wbuttonrect.height))
        self.currentscore = 0
        self.isactive = True
        self.delaychecked = False

    def menu_update(self, dt):

        point = pygame.mouse.get_pos()

        wbuttoncollide = self.wbuttonrect.collidepoint(point)
        if wbuttoncollide and pygame.mouse.get_pressed()[0]:
            self.isactive = False
        ebuttoncollide = self.ebuttonrect.collidepoint(point)
        if ebuttoncollide and pygame.mouse.get_pressed()[0]:
          sys.exit()


    def draw(self, screen):

        screen.fill((0, 150, 155))
        
        screen.blit(self.sprite_image, self.sprite.rect)
        screen.blit(self.welcomebutton, (250, 500))
        pygame.draw.rect(self.welcomebutton, (255,255,255), [
                         0, 0, self.wbuttonrect.width-48 , self.wbuttonrect.height-10], 1)

        screen.blit(self.exitbutton, (750, 500))
        pygame.draw.rect(self.exitbutton, (0,0,0), [
                         0, 0, self.ebuttonrect.width+8, self.ebuttonrect.height-10], 1)

        if self.currentscore != 0:      
         self.text_surface = self.my_font.render(
            f"Previous Score: {int(self.currentscore)}", False, (0, 0, 0))
         screen.blit(self.text_surface, (450, 10))
