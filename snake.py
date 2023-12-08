def renderApple():
    appleRect=pygame.Rect(posCalc(applePos[0]),posCalc(applePos[1]),blockScale,blockScale)
    pygame.draw.rect(screen,'green',appleRect)

def posCalc(posInt):
    pos=posInt*blockScale
    return pos

def processPos(Headpos):
    x=Headpos[0]
    y=Headpos[1]
    return (x,y)

def renderSnake():
    global snakeRect
    snakeRect=[]
    for i in range(0,snakeLength+1):
        snakeRect.append(pygame.Rect((posCalc(snakePos[i][0])),posCalc(snakePos[i][1]),blockScale,blockScale))
        pygame.draw.ellipse(screen,'red',snakeRect[i])

def snakeMove(score):
    global direction
    if event.key==pygame.K_UP:
        if (snakeLength>0 and snakePos[snakeLength-1][1] !=snakeHeadPos[1]-1) or snakeLength==0:
            snakeHeadPos[1]-=1
            if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
                snakePos.append(processPos(snakeHeadPos))
                score=eat(score)
            else:
                snakePos.append(processPos(snakeHeadPos))
                del snakePos[0]
            direction='U'
    if event.key==pygame.K_DOWN:
        if (snakeLength>0 and snakePos[snakeLength-1][1] !=snakeHeadPos[1]+1) or snakeLength==0:
            snakeHeadPos[1]+=1
            if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
                snakePos.append(processPos(snakeHeadPos))
                score=eat(score)
            else:
                snakePos.append(processPos(snakeHeadPos))
                del snakePos[0]
            direction='D'
    if event.key==pygame.K_LEFT:
        if (snakeLength>0 and snakePos[snakeLength-1][0] !=snakeHeadPos[0]-1) or snakeLength==0:
            snakeHeadPos[0]-=1
            if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
                snakePos.append(processPos(snakeHeadPos))
                score=eat(score)
            else:
                snakePos.append(processPos(snakeHeadPos))
                del snakePos[0]
            direction='L'
    if event.key==pygame.K_RIGHT:
        if (snakeLength>0 and snakePos[snakeLength-1][0] !=snakeHeadPos[0]+1) or snakeLength==0:
            snakeHeadPos[0]+=1
            if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
                snakePos.append(processPos(snakeHeadPos))
                score=eat(score)
            else:
                snakePos.append(processPos(snakeHeadPos))
                del snakePos[0]
            direction='R'
    return(score)

def eat(score):
        global snakeLength
        applePos[0]=random.randint(0,blockNumber-1)
        applePos[1]=random.randint(0,blockNumber-1)
        snakeLength+=1
        print('Eat')
        score+=1
        return(score)

def checkCollision():
    global gameState
    if snakeLength>0:
        for i in range(0,snakeLength):
            if (snakeHeadPos[0]==snakePos[i][0] and snakeHeadPos[1]==snakePos[i][1]) or snakeHeadPos[0]>blockNumber-1 or snakeHeadPos[1]>blockNumber-1 or snakeHeadPos[0]<0 or snakeHeadPos[1]<0:
                gameState=False
    else:
        if snakeHeadPos[0]>blockNumber-1 or snakeHeadPos[1]>blockNumber-1 or snakeHeadPos[0]<0 or snakeHeadPos[1]<0:
            gameState=False

def gameOver():
    screen.fill('black')
    gameOverText=font.render('Game Over!',False,(200,200,200))
    gameOverRect=gameOverText.get_rect(center=(screenScale/2,screenScale/2))
    screen.blit(gameOverText,gameOverRect)

def displayScore():
    scoreText=scoreFont.render('Score: '+str(score),False,(200,200,200))
    scoreRect=scoreText.get_rect(center=(screenScale/2,30))
    screen.blit(scoreText,scoreRect)

def snakeMoveAuto(direction,score):
    global snakeHeadPos
    if direction=='U':
        snakeHeadPos[1]-=1
        if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
            snakePos.append(processPos(snakeHeadPos))
            score=eat(score)
        else:
            snakePos.append(processPos(snakeHeadPos))
            del snakePos[0]
    if direction=='D':
        snakeHeadPos[1]+=1
        if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
            snakePos.append(processPos(snakeHeadPos))
            score=eat(score)
        else:
            snakePos.append(processPos(snakeHeadPos))
            del snakePos[0]
    if direction=='L':
        snakeHeadPos[0]-=1
        if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
            snakePos.append(processPos(snakeHeadPos))
            score=eat(score)
        else:
            snakePos.append(processPos(snakeHeadPos))
            del snakePos[0]
    if direction=='R':
        snakeHeadPos[0]+=1
        if snakeHeadPos[0]==applePos[0] and snakeHeadPos[1]==applePos[1]:
            snakePos.append(processPos(snakeHeadPos))
            score=eat(score)
        else:
            snakePos.append(processPos(snakeHeadPos))
            del snakePos[0]
        direction='R'
    return score

def restartGame(score):
    global snakeHeadPos,direction,snakePos,snakeLength,applePos
    score=0
    snakeHeadPos=[math.floor(blockNumber/2),math.floor(blockNumber/2)]
    snakePos=[(int(snakeHeadPos[0]),int(snakeHeadPos[1]))]
    snakeLength=0

    applePos=[10,5]

    direction='U'
    return score


import pygame
from sys import exit
import random
import math

pygame.init()

blockScale=40
blockNumber=21
screenScale=blockScale*blockNumber
bgColor='grey12'
screen=pygame.display.set_mode((screenScale,screenScale))
pygame.display.set_caption('Snek')
clock=pygame.time.Clock()

font=pygame.font.Font(None,80)
scoreFont=pygame.font.Font(None,80)

startPos=[math.floor(blockNumber/2),math.floor(blockNumber/2)]
snakeHeadPos=startPos
snakePos=[(int(snakeHeadPos[0]),int(snakeHeadPos[1]))]
snakeLength=0

applePos=[10,5]
gameState=True

score=0

timerEvent=pygame.USEREVENT+1

direction='U'

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if gameState:
                pygame.time.set_timer(timerEvent,500)
                score=snakeMove(score)
            else:
                if event.key==pygame.K_SPACE:
                    score=restartGame(score)
                    print(snakeHeadPos)
                    gameState=True

        if event.type==timerEvent:
            snakeMoveAuto(direction,score)
                

    if gameState:
        checkCollision()
        screen.fill(bgColor)
        displayScore()
        renderApple()
        renderSnake()

    else: 
        gameOver()
        displayScore()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
