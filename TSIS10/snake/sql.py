import csv
import psycopg2
import pygame
import random
from random import randrange

conn = psycopg2.connect(host = "localhost", user = "postgres", database = "snake", password = "kukamerey26")
cur = conn.cursor()
createtb = ('''
    CREATE TABLE IF NOT EXISTS snake(
    name varchar,
    scores varchar
    )''')
pygame.init()
level=1
level1=1
level3=20
level2=9
sup = 10
mon=800
size=50
fps=60
bg = pygame.image.load("background.jpg")
bg=pygame.transform.scale(bg,(800,800)) 
x,y= 300,300
length=1 
snake=[(x,y)]


buttons={
    'w':True,
    'a':True,
    'd':True,
    's':True
}
score_font = pygame.font.SysFont("Verdana", 20)
level_font = pygame.font.SysFont("Verdana", 20)
front=pygame.font.SysFont('Ariel',26,True)
def add_user():
    name = input("Newuser:")
    score = input("Score:")
    cur.execute("INSERT INTO snake VALUES(%s, %s)", (name, score))
    conn.commit()
def show():
    name = input("User:")
    cur.execute("SELECT * FROM snake WHERE name ILIKE %s", (name, score))
    conn.commit()
def delete():
    name = input("Delete user:")
    cur.execute("DELETE FROM snake name ILIKE %s", [name])
    conn.commit()

count=0

walls={ #уровни препятствий,
    1:[(50,50),(50,100),(50,150),(50,200),(150,0),(200,0),(250,0),(500,500),(550,500),(500,550),(600,500),(650,500)],
    2:[(700,700),(650,700),(700,650),(600,700),(700,600),(700,550),(650,550),(650,500)],
    3:[(0,0),(50,0),(100,0),(150,0),(200,0),(250,0),(300,0),(350,0),(400,0),(450,0),(500,0),(550,0),(600,0),(650,0),(700,0),(0,50),(0,100),(0,150),(0,200),(0,250),(0,300),(0,350),(0,400),(0,450),(0,500),(0,550),(0,600),(0,650),(0,700)]
}

speed=7 #скорость для clock
sup=10 #для 44,45 а так же для 124 строки нужнo, для range чтобы узнать попадает ли score в range
score=2# очки за каждое яблоко
dx,dy=0,0 #направление 

clock=pygame.time.Clock()
time=50 

apple=randrange(50,mon,size),randrange(0,mon,size) #спавн яблока
while apple in walls:
    apple=randrange(50,mon,size),randrange(0,mon,size)

screen=pygame.display.set_mode([mon,mon])



working=True
while working:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            working=False

        if event.type == pygame.KEYDOWN :# полностью движение 
            if event.key == pygame.K_w and buttons['w']: # если нажали w то змейка будет двигать вверх, ибо dy будет равен -1(тоесть вы будете двигаться по координа dy в минусовыю часть, тоесть вверх)
                #а buttonsp['w'] нужен для того чтобы при движений вниз s  мы не могли двигаться одновременно вверх
                buttons={
                    'w':True,
                    'a':True,
                    'd':True,
                    's':False
                }
                dx,dy=0,-1
            elif event.key == pygame.K_s and buttons['s']:
                dx,dy=0,1
                buttons={
                    'w':False,
                    'a':True,
                    'd':True,
                    's':True
                }
            elif event.key == pygame.K_a and buttons['a']:
                dx,dy=-1,0
                buttons={
                    'w':True,
                    'a':True,
                    'd':False,
                    's':True
                }
            elif event.key == pygame.K_d and buttons['d']:
                dx,dy=1,0
                buttons={
                    'w':True,
                    'a':False,
                    'd':True,
                    's':True #sw
                }
    screen.blit(bg,(0,0)) #рисуем задний фон

    if snake[-1] in walls[level]: # если координаты головы есть в координатах стен то игра останавливается
        pygame.quit()

    if apple in walls[level]:#нужна для проверки если яблоко появилось внутри стен
        apple=randrange(50,mon,size),randrange(0,mon,size)

    [(pygame.draw.rect(screen,pygame.Color('green'),(i,j,size-2,size-2))) for i, j in snake]# рисуем змейку

    pygame.draw.rect(screen, pygame.Color('red'), (*apple, size-2,size-2))# рисуем яблоко

    for i in walls[level]: #рисуем стены определенного уровня
        pygame.draw.rect(screen,(0,0,0),(i[0],i[1],48,48))
    render_score=front.render(f'SCORE:{count}',1,pygame.Color('purple'))#пишем score
    screen.blit(render_score,(5,5))#рисуем score
    render_level=front.render(f'LEVEL:{level1}',1,pygame.Color('purple'))#пишем score
    screen.blit(render_level,(5,20))
    if time ==0:#время для случая, если время для сьедания яблока истекло
        apple=randrange(50,mon,size),randrange(0,mon,size)
        time=50

    x+=dx*size #непрерывное движение
    y+=dy*size

    time-=1 #раз в 50 speed мы обновляем местоположение яблоки, это нужно нам для 111 строки

    snake.append((x,y))#координаты змейки
   
    snake=snake[-length:]#для того чтобы мы брали только змейку, а не места где она прошлась

    if count in range(level2,level3):#нужна для переноса в след уровень,а так же для увеличения награды за яблоко, скорость, 
        level1+=1
        level2+=sup
        level3+=sup
        sup+=20
        level+=1
        score+=1
        speed+=2
        if level==4:level=1

    if snake[-1]==apple: #в случае если координата яблоки и головы змейки совпала
        count+=score
        length+=1
        time=50
        apple=randrange(50,mon,size),randrange(0,mon,size)

    if x<0 or x> mon-size or y<0 or y >mon-size or len(snake) != len(set(snake)):#выход за пределы поля или змейка входит в себя
        working=False

    pygame.display.flip()
    clock.tick(speed)
