import pygame

class Menu():

    def __init__(self):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.text_surface = self.my_font.render("Welcome To Frawger", False, (0,0,0))
        #self.rect = self.text_surface.get_rect()
        self.rect = pygame.Rect(400,500, 220, 50)
        self.isactive = True
        self.delaychecked = False


    def menu_update(self, dt):

        
         point = pygame.mouse.get_pos()

         collide = self.rect.collidepoint(point)
         if collide and pygame.mouse.get_pressed()[0]:
            #print("it be colliding")
            if (self.isactive):
                self.delaychecked = False
            self.isactive = False
            
        

    
    def draw(self, screen):
        
         screen.fill((0, 150, 155))
         screen.blit(self.text_surface, (400,500))
         pygame.draw.rect(self.text_surface, (255,0,0),[0,0, self.rect.width +72, self.rect.height-10], 1)


    