import pygame

pygame.init()
screen = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()
done = False
X = 750
Y = 400
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
               done=True 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and Y<=20: Y -=20
    if pressed[pygame.K_DOWN] and Y <= 800: Y += 20
    if pressed[pygame.K_LEFT] and X >= 20: X -= 20
    if pressed[pygame.K_RIGHT] and X <= 1500: X += 20
    screen.fill((35, 35, 35))
    pygame.draw.circle(screen, ((0, 0, 255)), (X, Y), 25)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
