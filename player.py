import pygame


class Player():
    
    
    def __init__(self, x, y, w, h):
        self.vx = 0
        self.vy = 0
        
        self.rect = pygame.Rect(x, y, w, h)
        
        self.moving_x = False 
        
    def move(self, dt, gameObjects):
        x_step = self.vx
        y_step = self.vy
        
        collided = False
        
        self.rect.move_ip(x_step * dt, 0)
        
        for object in gameObjects:
            if self.rect.colliderect(object):
                self.rect.move_ip(-x_step * dt, 0)
                self.vx = 0
                if object.handle_collision():
                    collided = True
                
                
        
        self.rect.move_ip(0, y_step * dt)
        
        for object in gameObjects:
            if self.rect.colliderect(object):
                self.rect.move_ip(0, -y_step * dt)
                self.vy = 0
                if object.handle_collision():
                    collided = True
                
                # ...
                if self.rect.bottomright[1] != object.rect.topright[1]:
                    if self.rect.bottomright[1] < object.rect.topright[1]:
                        self.rect.move_ip(0, -(self.rect.bottomright[1] - object.rect.topright[1]))
                        
        return collided
        
    
    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)