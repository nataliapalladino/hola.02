import pygame
import math



heredero=pygame.sprite.Sprite

class Weapon():
    def __init__(self,image,arrow_image):
        
        self.original_image=image
        self.arrow_image=arrow_image
        self.angle=0
        self.image=pygame.transform.rotate(self.original_image,self.angle)
        self.rect=self.image.get_rect()
        self.last_shot=pygame.time.get_ticks()
        self.fired=False
        
        
    def update(self,player):
        shot_cooldown=300
        arrow=None
        
        self.rect.center = player.rect.center 
        pos=pygame.mouse.get_pos()
        x_distance=pos[0] - self.rect.centerx
        y_distance=-(pos[1]-self.rect.centery)
        self.angle=math.degrees(math.atan2(y_distance,x_distance)) 
        
        tiempo=pygame.time.get_ticks() - self.last_shot
        if pygame.mouse.get_pressed()[0] and self.fired == False and tiempo >= shot_cooldown:
            arrow=Arrow(self.arrow_image,self.rect.centerx,self.rect.centery,self.angle)
            self.fired=True
            self.last_shot=pygame.time.get_ticks()
            
        if pygame.mouse.get_pressed()[0] == False:
            self.fired=False
            
        return arrow
        
    def draw(self,surface):
        
        rectx=self.rect.centerx-(int(self.image.get_width()/2))
        recty=self.rect.centery-(int(self.image.get_height()/2))
        
        self.image=pygame.transform.rotate(self.original_image,self.angle)
        surface.blit(self.image,(rectx,recty))
        
class Arrow(heredero):
    
    def __init__(self, image,x,y,angle):
        
        heredero. __init__(self)
        
        self.original_imagen = image
        self.angle=angle
        self.image=pygame.transform.rotate(self.original_imagen,self.angle-90)
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        
        self.dx=math.cos(math.radians(self.angle))*10
        self.dy=-(math.sin(math.radians(self.angle))*10)
        
    def update(self):
            
        self.rect.x += self.dx
        self.rect.y += self.dy 
        
    def draw(self,surface):
        rectx=self.rect.centerx-(int(self.image.get_width()/2))
        recty=self.rect.centery-(int(self.image.get_height()/2))
        
        self.image=pygame.transform.rotate(self.original_imagen,self.angle)
        surface.blit(self.image,(rectx,recty))
        