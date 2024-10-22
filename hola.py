import pygame
import constant
from character import character

pygame.init()

scree=pygame.display.set_mode((constant.ancho,constant.largo))

clock=pygame.time.Clock() 

running=True



movin_right=False
movin_left=False
movin_up=False
movin_down=False

#llagamos hasta aca
def scale_img(image,scale):
    w= image.get_width()
    h=image.get_height()
    
    return pygame.transform.scale(image,(w*scale,h*scale))

animation_list=[]
for i in range(4):
    img=pygame.image.load(f"Tengo-Fe/images/characters/elf/idle/{i}.png")
    img=scale_img(img,3)
    animation_list.append(img)
    

player=character(40,50,animation_list)

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
    player.update()
    
            
    pygame.display.update()
    clock.tick(constant.FPS)