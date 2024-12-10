import pygame

from gameObject import GameObject


class WinningPlatform(GameObject):
    
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
       
    # overrides 
    def handle_collision(self):
        print("WON")
        # ??
        return True
    
    # overrides
    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)