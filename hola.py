import pygame
import constant
from character import character

pygame.init()

scree=pygame.display.set_mode((constant.ancho,constant.largo))

clock=pygame.time.Clock() 

running=True

player=character(40,50)

movin_right=False
movin_left=False
movin_up=False
movin_down=False

while running:
    
    scree.fill((204,169,221))
    
    #direcciones
    Dx=0
    Dy=0 
    if movin_right == True: 
        Dx=constant.SPEED
    if movin_left == True:
        Dx=-constant.SPEED
    if movin_up == True:
        Dy=-constant.SPEED
    if movin_down == True:
        Dy=constant.SPEED

    
    player.draw(scree)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movin_up= True
            if event.key == pygame.K_DOWN:
                movin_down=True
            if event.key == pygame.K_LEFT:
                movin_left=True
            if event.key == pygame.K_RIGHT:  
                movin_right=True 
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                movin_up= False
            if event.key == pygame.K_DOWN:
                movin_down=False
            if event.key == pygame.K_LEFT:
                movin_left=False
            if event.key == pygame.K_RIGHT:  
                movin_right=False 
         
                
    player.move(Dx,Dy)         
    pygame.display.update()
    clock.tick(constant.FPS)