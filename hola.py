import pygame
import constant
from character import character
from weanpon import Weapon

pygame.init()

scree=pygame.display.set_mode((constant.ancho,constant.largo))

clock=pygame.time.Clock() 

running=True
bow_image=pygame.image.load("Tengo-Fe/images/weapons/bow.png")


movin_right=False
movin_left=False
movin_up=False
movin_down=False

#llagamos hasta aca
def scale_img(image,scale):
    w= image.get_width()
    h=image.get_height()
    
    return pygame.transform.scale(image,(w*scale,h*scale))

mob_animation=[]
mob_types=["big_demon","elf","imp","muddy","skeleton","tiny_zombie","goblin"]

animation_types=["idle","run"]
for mob in mob_types:
    animation_list=[]

    for animation in animation_types:
        temp_list=[]
        for i in range(4):
            img=pygame.image.load(f"Tengo-Fe/images/characters/{mob}/{animation}/{i}.png")
            img=scale_img(img,3)
            temp_list.append(img)
        animation_list.append(temp_list)
    mob_animation.append(animation_list)
    

player=character(40,50,mob_animation,1)
arrow=pygame.image.load("tengo-fe/images/weapons/arrow.png")
arrow_image=scale_img(arrow,constant.SCALE)

bow=Weapon(bow_image,arrow_image)
bow=Weapon(bow_image,arrow_image)
arrow_group=pygame.sprite.Group()
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

    arrow=bow.update(player)
    if arrow:
        arrow_group.add(arrow)
    player.draw(scree)
    bow.draw(scree)
    for arrow in arrow_group:
        arrow.draw(scree)
    
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
    bow.update(player)
    
            
    pygame.display.update()
    clock.tick(constant.FPS)