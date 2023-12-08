def displayGrid():
    for i in range(1,blockNumber):
        pygame.draw.line(screen,mazeColor,processPos((0,i)),processPos((screenScale,i)),3)
        pygame.draw.line(screen,mazeColor,processPos((i,0)),processPos((i,screenScale)),3)

def processPos(posInt):
    posX=posInt[0]*(blockSize+3)
    posY=posInt[1]*(blockSize+3)
    return(posX,posY)

def renderMaze(visited,moveDirection):
    global mazeHeadRect
    mazeHeadRect=[]
    for i in range(0,len(visited)):
        if moveDirection[i]=='N':
            mazeHeadRect.append(pygame.Rect(processPos(visited[i])[0]+3,processPos(visited[i])[1]+3,blockSize-1.5,blockSize-1.5))
        if moveDirection[i]=='U':
            mazeHeadRect.append(pygame.Rect(processPos(visited[i])[0]+3,processPos(visited[i])[1]+3,blockSize-1.5,blockSize-1.5+6))
        if moveDirection[i]=='D':
            mazeHeadRect.append(pygame.Rect(processPos(visited[i])[0]+3,processPos(visited[i])[1]-3,blockSize-1.5,blockSize-1.5+6))
        if moveDirection[i]=='L':
            mazeHeadRect.append(pygame.Rect(processPos(visited[i])[0]+3,processPos(visited[i])[1]+3,blockSize-1.5+6,blockSize-1.5))
        if moveDirection[i]=='R':
            mazeHeadRect.append(pygame.Rect(processPos(visited[i])[0]-3,processPos(visited[i])[1]+3,blockSize-1.5+6,blockSize-1.5))
        pygame.draw.rect(screen,bgColor,mazeHeadRect[i])

def checkAvail(pos,visited,options):
    options.clear()
    left=pos[0]-1
    right=pos[0]+1
    up=pos[1]-1
    down=pos[1]+1
    for posVisited in visited:
        if (right,pos[1]) !=posVisited and right !=blockNumber and posVisited!=visited[len(visited)-1]:
            continue
        elif (right,pos[1]) !=posVisited and right !=blockNumber and posVisited==visited[len(visited)-1]:
            options.append('R')
        else:
            break
    for posVisited in visited:
        if (left,pos[1]) !=posVisited and left !=-1 and posVisited!=visited[len(visited)-1]:
            continue
        elif (left,pos[1]) !=posVisited and left !=-1 and posVisited==visited[len(visited)-1]:
            options.append('L')
        else:
            break

    for posVisited in visited:
        if (pos[0],down) !=posVisited and  down!=blockNumber and posVisited!=visited[len(visited)-1]:
            continue
        elif (pos[0],down) !=posVisited and down !=blockNumber and posVisited==visited[len(visited)-1]:
            options.append('D')
        else:
            break
    for posVisited in visited:
        if (pos[0],up) !=posVisited and up !=-1 and posVisited!=visited[len(visited)-1]:
            continue
        elif (pos[0],up) !=posVisited and up !=-1 and posVisited==visited[len(visited)-1]:
            options.append('U')
        else:
            break
    #print('options: '+str(options))
    return(options)

def moveMazeHead(mazeHeadLoc,options):
    global visited,history,moveDirection
    direction='N'
    while True:
        options=checkAvail(mazeHeadLoc,visited,options)
        if len(options)>0:
            moveDirection.append(options[random.randint(0,len(options)-1)])
            direction=moveDirection[-1]
            if direction=='U':
                mazeHeadLoc[1]-=1
            if direction=='D':
                mazeHeadLoc[1]+=1
            if direction=='L':
                mazeHeadLoc[0]-=1
            if direction=='R':
                mazeHeadLoc[0]+=1
            visited.append((mazeHeadLoc[0],mazeHeadLoc[1]))
            history.append((mazeHeadLoc[0],mazeHeadLoc[1]))
            break
        else:
            #going back 1 step
            mazeHeadLoc[0]=history[len(history)-2][0]
            mazeHeadLoc[1]=history[len(history)-2][1]
            del history[len(history)-1]
            continue
    renderMaze(visited,moveDirection)
    #displayOrder()

def displayOrder():
    i=1
    orderText=[]
    orderRect=[]
    for k in range(0,len(visited)):
        orderText.append(gameFont.render(str(i),False,'green'))
        orderRect.append(orderText[k].get_rect(topleft=(processPos(visited[k])[0]+3,processPos(visited[k])[1]+3)))
        screen.blit(orderText[k],orderRect[k])
        i+=1

def renderStartEndPoints():
    startRect=pygame.Rect(processPos(visited[0])[0]+3,processPos(visited[0])[1]+3,blockSize-1.5,blockSize-1.5)
    endRect=pygame.Rect(processPos(visited[-1])[0]+3,processPos(visited[-1])[1]+3,blockSize-1.5,blockSize-1.5)
    pygame.draw.ellipse(screen,startColor,startRect,3)
    pygame.draw.ellipse(screen,startColor,endRect,3)


import pygame
from sys import exit
import random

pygame.init()

clock=pygame.time.Clock()

gameFont=pygame.font.Font(None,5)


blockSize=10
screenScale=600
blockNumber=int(screenScale/blockSize)
screen=pygame.display.set_mode((screenScale+(3*(blockNumber+1)),screenScale+(3*(blockNumber+1))))
pygame.display.set_caption('MazeGen')

borderRect=pygame.Rect(0,0,screenScale+(3*(blockNumber+1)),screenScale+(3*(blockNumber+1)))

mazeHeadLoc=[0,0]
visited=[(0,0)]
history=[(0,0)]
options=['R','D']
moveDirection=['N']

bgColor='black'
mazeColor='red'
startColor='green'

screen.fill(bgColor)
pygame.draw.rect(screen,mazeColor,borderRect,3)
displayGrid()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    

    
    while len(visited)<=((blockNumber)*(blockNumber))-1:
        moveMazeHead(mazeHeadLoc,options)
        options.clear()
        renderStartEndPoints()
        pygame.display.flip()
        clock.tick(100)


