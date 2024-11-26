import pygame


class character():
    
    def __init__(self,x,y,panimation_list,char_type):
        
        self.char_type= char_type
        self.flip=False
        self.amination_list=panimation_list[char_type]
        self.frame_index=0
        self.action=1
        self.running=0 #no lo vamos a usar
        self.update_time=pygame.time.get_ticks()
        self.image=self.amination_list[self.action][self.frame_index]
        self.rect=pygame.Rect(0,0,40,40)
        self.rect.center=(x,y)
    
    def draw(self,superficie):
        #pygame.draw.rect(superficie, (100,255,255),self.rect)
        flip_image=pygame.transform.flip(self.image,self.flip,False)
        superficie.blit(flip_image,self.rect)
        
           
    def move(self,Dx,Dy):
        self.running=False
        if Dx<0:
            self.flip=True
            self.running=True
        elif Dx>0:
            self.flip=False
            self.running=True
            
        self.rect.x+=Dx
        self.rect.y+=Dy
        print(self.rect.x,self.rect.y)
        
    def update(self):
        if self.running == True:
            self.update_action(1)
        else:    
            self.update_action(0)
            
        amination_cooldown=100
        self.image=self.amination_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > amination_cooldown:
            self.frame_index +=1
            self.update_time = pygame.time.get_ticks()
            
        if self.frame_index>= len(self.amination_list):
            self.frame_index=0
            
            
    def update_action(self, new_action):
        if new_action != self.action:
            self.action=new_action
            self.frame_index=0
            self.update_time=pygame.time.get_ticks()