import pygame
import os

ander = ['bedroom-in-my-head-official-audio.mp3', 'Daft Punk - Veridis Quo (Music Video).mp3', 'Dido - Thank You.mp3', 'gorillaz-on-melancholy-hill-official-video.mp3']
pppn = ['pause.png', 'play.jpg', 'next.jpg', 'previous.png']
photos = ['inmyhead.jpg', 'veridisquo.jpg', 'thankyou.jpg', 'onmelancholyhill.jpg']
pygame.mixer.init()
screen = pygame.display.set_mode((1310, 900))
done = False
i = 0
def start(i):
    screen.blit(pygame.image.load(photos[i]), (395, 5))
    pygame.mixer.music.load(ander[i])
    pygame.mixer.music.play()
start(i)

screen.blit(pygame.image.load(pppn[0]), (475, 525))
screen.blit(pygame.image.load(pppn[3]), (50, 525))
screen.blit(pygame.image.load(pppn[2]), (900, 525))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        mouse_pos = pygame.mouse.get_pos()
        left = pygame.mouse.get_pressed()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(paused == False):
                pygame.mixer.music.pause()
                paused = True
                screen.blit(pygame.image.load(pppn[1]), (475, 525))
            else:
                pygame.mixer.music.unpause()
                paused = False 
                screen.blit(pygame.image.load(pppn[0]), (475, 525))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if i==3: i=0
            else: i+=1
            screen.blit(pygame.image.load(photos[i]), (395, 5))
            start(i)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if i==0: i=3
            else: i-=1
            screen.blit(pygame.image.load(photos[i]), (395, 5))
            start(i)
        if left:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 475 <=mouse_pos[0]<= 835 and 525 <= mouse_pos[1]<= 885:
                    if(paused == False):
                        pygame.mixer.music.pause()
                        paused = True
                        screen.blit(pygame.image.load(pppn[1]), (475, 525))
                    else:
                        pygame.mixer.music.unpause()
                        paused = False 
                        screen.blit(pygame.image.load(pppn[0]), (475, 525))
                if 50 <= mouse_pos[0] <= 410 and 525 <= mouse_pos[1] <= 885:
                    if i==0: i=3
                    else: i-=1
                    screen.blit(pygame.image.load(photos[i]), (395, 5))
                    start(i)
                if 900 <= mouse_pos[0] <= 1260 and 525 <= mouse_pos[1] <= 885:
                    if i==3: i=0
                    else: i+=1
                    screen.blit(pygame.image.load(photos[i]), (395, 5))
                    start(i)
    pygame.display.flip()

pygame.quit()