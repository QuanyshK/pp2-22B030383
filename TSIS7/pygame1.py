
from datetime import datetime 
import pygame 
pygame.init() 
screen=pygame.display.set_mode((400,400)) 
a = datetime.now() 
image = pygame.image.load("mickeyclock.png") 
image = pygame.transform.scale(image, (400, 400)) 
handl = pygame.image.load("handl.png") 
handl = pygame.transform.scale(handl, (200, 200)) 
handr =pygame.image.load("handr.png") 
handr = pygame.transform.scale(handr, (200, 200))
#left hand 
def left_hand(surf, image, topleft, angle):  
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#right hand
def right_hand(surf, image, topleft, angle):   
    rotated_image = pygame.transform.rotate(image, angle) 
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center) 
    surf.blit(rotated_image, new_rect) 
#formula for position mickey's mouse 
anglel=(51-a.second)*6 
angleh=308-(a.minute*6) 
# firstly coordination 
x=100 
y=80 
running = True 
n=a.second 
while running: 
    #assigned another variable the method "time is now" so that the condition b.second is met!= n during the rotation of the second hand 
    b=datetime.now() 
    screen.fill((255,255,255)) 
    #include photo mickey mouse in window 
    screen.blit(image,(0,0))    
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            pygame.quit() 
            quit() 
    #return function left and right hand 
    left_hand(screen, handl, [x,y], anglel) 
    right_hand(screen, handr, [x,y], angleh) 
    #upgrade window  
    pygame.display.update()   
    #increase rotate angle arrows     
    if b.second>=0 and b.second != n: 
        n=b.second 
        anglel+=6 
    if n==0: 
        angleh+=0.1 