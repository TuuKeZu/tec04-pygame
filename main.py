from typing import List
import pygame

from gameObject import GameObject
from spike import Spike
from player import Player

pygame.init()
screen = pygame.display.set_mode([1200, 800])


running = True

clock = pygame.time.Clock()

player = Player(100, 100, 20, 20)

gameObjects: List[GameObject] = []

file = open("levels\level1.txt")
for line in file.readlines():
    data = line.rstrip().split(",")
    
    if len(data) != 5:
        print("Invalid line: " + line)
        continue
    
    x = int(data[0])
    y = int(data[1])
    w = int(data[2])
    h = int(data[3])
    
    # Type of the gameObject
    t = data[4]
    
    if t == "s":
        new_spike = Spike(x, y, w, h)
        gameObjects.append(new_spike)
    elif t == "p":
        new_gameobject = GameObject(x, y, w, h)
        gameObjects.append(new_gameobject)
    
print(gameObjects)


while running:
    # Aika edellisestä näytön päivityksestä (deltaTime)
    dt = clock.tick(60)/1000
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.vy = -200
            elif event.key == pygame.K_LEFT:
                player.moving_x = True
                player.vx = -100
            elif event.key == pygame.K_RIGHT:
                player.moving_x = True
                player.vx = 100
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.moving_x = False
                player.vx = -100
            elif event.key == pygame.K_RIGHT:
                player.moving_x = False
                player.vx = 100
                

    screen.fill((255, 255, 255))
    # Liikuta palloa 100px oikealle sekunnissa riippumatta pelin nopeudesta
    
    player.vy += 10

    # playe.x = player.vx * dt
    player.move(dt, gameObjects)

    if not player.moving_x:
        if player.vx > 0:
            player.vx -= 5
        
        if player.vx < 0:
            player.vx += 5
    

        
    player.render(screen)
    
    for g in gameObjects:
        g.render(screen)

    pygame.display.flip()


pygame.quit()