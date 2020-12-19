import pygame
import time
import random
pygame.init()

red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
gameWindow= pygame.display.set_mode((800,600))
pygame.display.set_caption('welcome to snake game(SHRIKANT GAMING ) ')

block = 20
clk=pygame.time.Clock()
font=pygame.font.SysFont(None,35)
def snake(block,snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameWindow,black,[XnY[0],XnY[1],block,block])
def message(msg,color):
    screen_text=font.render(msg,True,color)
    gameWindow.blit(screen_text,[50,300])
def loop():
    start_x = 400
    start_y = 200
    update_x = 0
    update_y = 0
    snakeList=[]
    snakeLength=1
    gameclose = False
    gamover=False
    rApplex=round(random.randrange(0,800-block)/20)*20
    rAppley=round(random.randrange(0,600-block )/20)*20
    while not gameclose:
        while gamover==True:
            gameWindow.fill(white)
            message("[you lose the game] , press R to replay or press Q to quit", black)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameclose=True
                        gamover=False
                    if event.key==pygame.K_r:
                        loop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameclose=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    update_x = -block
                    update_y=0
                if event.key==pygame.K_RIGHT:
                   update_x=+block
                   update_y=0
                if event.key==pygame.K_UP:
                    update_y= -block
                    update_x=0
                if event.key==pygame.K_DOWN:
                    update_y=+block
                    update_x=0
        if start_x>=800 or start_x<0 or start_y>=600 or start_y<0:
            gamover=True

        start_x+=update_x
        start_y+=update_y
        gameWindow.fill(red)
        pygame.draw.rect(gameWindow,white,[rApplex,rAppley,block,block])
        snakHead = []
        snakHead.append(start_x)
        snakHead.append(start_y)
        snakeList.append(snakHead)
        if len(snakeList) > snakeLength:
            del (snakeList[0])
        for eachsegment in snakeList[-1]:
            if eachsegment == snakHead:
                gamover = True

        snake(block, snakeList)

        pygame.display.update()
        if start_x==rApplex and start_y==rAppley:
            rApplex = round(random.randrange(0, 800 - block) / 20) * 20
            rAppley = round(random.randrange(0, 600 - block) / 20) * 20
            snakeLength+=1

        clk.tick(13)

    pygame.quit()
    quit()
loop()