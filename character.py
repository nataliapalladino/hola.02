import pygame

class character():
    
    def __init__(self,x,y,panimation_list):
        
        self.flip=False
        self.amination_list=panimation_list
        self.frame_index=0
        self.action=0
        self.running=0#no lo vamos a usar
        self.update_time=0
        self.update_time=pygame.time.get_ticks()
        self.image=self.amination_list[self.frame_index]
        self.rect=pygame.Rect(0,0,40,40)
        self.rect.center=(x,y)
    
    def draw(self,superficie):
        pygame.draw.rect(superficie, (100,255,255),self.rect) 
        
    def move(self,Dx,Dy):
        self.rect.x+=Dx
        self.rect.y+=Dy
        print(self.rect.x,self.rect.y)