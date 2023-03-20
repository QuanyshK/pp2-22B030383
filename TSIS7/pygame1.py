import pygame
import time
import datetime
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
done = False
myClock = pygame.image.load('mickeyout.jpg')
myClock = pygame.transform.scale(myClock, (600, 600))
minute_arrow = pygame.image.load('mickeyleft.jpg')
minute_arrow = pygame.transform.scale(minute_arrow, (30 // 1.5, 350 // 1.5))
second_arrow = pygame.image.load('mickeyright.jpg')

second_arrow = pygame.transform.scale(second_arrow, (25 // 1.5, 400 // 1.5))
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        my_time = datetime.datetime.now()
        minuteINT = int(my_time.strftime("%M"))
        secondINT = int(my_time.strftime("%S"))
        angleMINUTE = minuteINT * 6 * -1
        angleSECOND = secondINT * 6 * -1

        minute = pygame.transform.rotate(minute_arrow, angleMINUTE)
        second = pygame.transform.rotate(second_arrow, angleSECOND)
        

        screen.fill((255, 255, 255))
        screen.blit(myClock, (100, 100))
        screen.blit(second, (500 - int(second.get_width() / 2), 500- int(second.get_height() / 2)))
        screen.blit(minute, ((500 - int(minute.get_width() / 2), 500 - int(minute.get_height() / 2))))
        pygame.display.flip()
        clock.tick(60)
pygame.quit()