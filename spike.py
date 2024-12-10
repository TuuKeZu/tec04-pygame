import pygame

from gameObject import GameObject


class Spike(GameObject):
    
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
       
    # overrides 
    def handle_collision(self):
        print("SPIKE!")
    
    # overrides
    def render(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)