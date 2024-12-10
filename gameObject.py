import pygame

class GameObject():
    
    
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        
    def handle_collision(self):
        pass     
        
    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)