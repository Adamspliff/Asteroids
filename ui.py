import pygame, sys
from constants import *

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

            

class Text:
    def __init__(self, string, bool, color):
        self.string = string
        self.bool = bool
        self.color = color

        self.font = pygame.font.SysFont('Lato', 30)
        self.render = self.font.render(self.string, self.bool, self.color)
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),)
        
        

    def draw(self,screen):
        screen.blit(self.render, (SCREEN_WIDTH/4, SCREEN_HEIGHT/4)) 
    
    def update(self, dt, score):
        
        self.string = f"Score:{round(score)}"
        if score > 1000:
            self.color=255,100,100

        self.render = self.font.render(self.string, self.bool, self.color)
        self.surface.blit(self.render, (SCREEN_WIDTH/8, SCREEN_HEIGHT/8))

    

   


 




