import pygame


class Counter():

    def __init__(self):
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.start_ticks = pygame.time.get_ticks()
        self.multiplier = 1
        self.seconds = 0

    def countup(self):
        self.seconds += 0.01 * self.multiplier
        

    def draw(self, screen):
        self.text_surface = self.my_font.render(
            f"{int(self.seconds)}", False, (0, 0, 0))
        screen.blit(self.text_surface, (500, 10))
