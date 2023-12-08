def TBlock(pos,o):
    Tlocs=[]
    o=o%4
    match o:
        case 0:
            if pos[0]==0:
                pos[0]+=1
            elif pos[0]==NUM_BLOCKS_X-1:
                pos[0]-=1
            Tlocs=[[pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0],pos[1]+1]]
        case 1:
            if pos[0]==0:
                pos[0]+=1
            Tlocs=[[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0]-1,pos[1]]]
        case 2:
            if pos[0]==0:
                pos[0]+=1
            elif pos[0]==NUM_BLOCKS_X-1:
                pos[0]-=1
            Tlocs=[[pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0],pos[1]-1]]
        case 3:
            if pos[0]==NUM_BLOCKS_X-1:
                pos[0]-=1
            Tlocs=[[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]]]
    return Tlocs

def LBlock(pos,o,mirrored):
    LLocs=[]
    o=o%4
    if not mirrored:
        match o:
            case 0:             
                LLocs=[[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]+1]]
            case 1:
                if pos[0]==0:
                    pos[0]+=1
                LLocs=[[pos[0]+1,pos[1]],[pos[0],pos[1]],[pos[0]-1,pos[1]],[pos[0]-1,pos[1]+1]]
            case 2:
                LLocs=[[pos[0],pos[1]+1],[pos[0],pos[1]],[pos[0],pos[1]-1],[pos[0]-1,pos[1]-1]]
            case 3:
                if pos[0]==NUM_BLOCKS_X-1:
                    pos[0]-=1   
                LLocs=[[pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0]+1,pos[1]-1]]
    else:
        match o:
            case 0:
                LLocs=[[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0]-1,pos[1]+1]]
            case 1:
                if pos[0]==NUM_BLOCKS_X-1:
                    pos[0]-=1   
                LLocs=[[pos[0]+1,pos[1]],[pos[0],pos[1]],[pos[0]-1,pos[1]],[pos[0]-1,pos[1]-1]]
            case 2:
                LLocs=[[pos[0],pos[1]+1],[pos[0],pos[1]],[pos[0],pos[1]-1],[pos[0]+1,pos[1]-1]]
            case 3:
                if pos[0]==0:
                    pos[0]+=1
                LLocs=[[pos[0]-1,pos[1]],[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0]+1,pos[1]+1]]
    return LLocs

def ZBlock(pos,o,mirrored):
    zLocs=[]
    o=o%2
    if not mirrored:
        match o:
            case 0:
                ZLocs=[[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0],pos[1]+1],[pos[0]-1,pos[1]+1]]
            case 1:
                ZLocs=[[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0]-1,pos[1]],[pos[0]-1,pos[1]-1]]
    else:
        match o:
            case 0:
                ZLocs=[[pos[0],pos[1]],[pos[0]-1,pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]+1]]
            case 1:
                ZLocs=[[pos[0],pos[1]],[pos[0],pos[1]-1],[pos[0]-1,pos[1]],[pos[0]-1,pos[1]+1]]
    return ZLocs

def SBlock(pos):
    sLocs=[[pos[0],pos[1]],[pos[0]+1,pos[1]],[pos[0],pos[1]+1],[pos[0]+1,pos[1]+1]]
    return sLocs

def IBlock(pos,o):
    ILocs=[]
    o=o%2
    match o:
        case 0:
            ILocs=[[pos[0],pos[1]-1],[pos[0],pos[1]],[pos[0],pos[1]+1],[pos[0],pos[1]+2]]
        case 1:
            if pos[0]==0:
                pos[0]+=2
            if pos[0]==NUM_BLOCKS_X-1:
                pos[0]-=1   
            ILocs=[[pos[0]+1,pos[1]],[pos[0],pos[1]],[pos[0]-1,pos[1]],[pos[0]-2,pos[1]]]
    return ILocs

def displayGrid():
    for i in range(1,NUM_BLOCKS_X):
        pygame.draw.line(screen,gridCol,(i*GRID_SIZE+(i-1)*GRID_LINE_THICKNESS,0),(i*GRID_SIZE+(i-1)*GRID_LINE_THICKNESS,SCREEN_H),GRID_LINE_THICKNESS)
    for i in range(1,NUM_BLOCKS_Y):
        pygame.draw.line(screen,gridCol,(0,i*GRID_SIZE+(i-1)*GRID_LINE_THICKNESS),(SCREEN_W,i*GRID_SIZE+(i-1)*GRID_LINE_THICKNESS),GRID_LINE_THICKNESS)

# def displayCurrentBlock(locs):
#     blockRects=[]
#     for i,pos in enumerate(locs):
#         blockRects.append(pygame.Rect(posCalc(pos)[0],posCalc(pos)[1],GRID_SIZE,GRID_SIZE))
#         pygame.draw.rect(screen,"red",blockRects[i])

def displayBlocks(locs):
    blocks=[]
    for i,pos in enumerate(locs):
        blocks.append(pygame.Rect(posCalc(pos)[0],posCalc(pos)[1],GRID_SIZE,GRID_SIZE))
        pygame.draw.rect(screen,"red",blocks[i])

def posCalc(initPos):
    x=initPos[0]*(GRID_LINE_THICKNESS+GRID_SIZE)-GRID_LINE_THICKNESS/4
    y=initPos[1]*(GRID_LINE_THICKNESS+GRID_SIZE)-GRID_LINE_THICKNESS/4
    return(x,y)

def pickRandomBlock():
    blockType=random.randint(0,4)
    mirrored=0
    rot=random.randint(0,4)
    if BLOCKTYPES[blockType]=="z" or BLOCKTYPES[blockType]=="L":
        mirrored=random.randint(0,1)
    return(blockType,mirrored,rot)

def generateNewBlock():
    blockType,mirrored,rot=pickRandomBlock()
    limits=[0,0,0]
    locs=[]
    if blockType==0:
        limits[0]=1
        limits[1]=1
        if rot%4!=0:
            limits[2]=1
    elif blockType==1:
        if rot%4==0:
            limits[1]=1
            limits[2]=1
            if mirrored:
                limits[0]=1
                limits[1]=0
        elif rot%4==1:
            limits[0]=1
            limits[1]=1
            if mirrored:
                limits[2]=1
        elif rot%4==2:
            limits[0]=1
            limits[2]=1
            if mirrored:
                limits[0]=0
                limits[1]=1
        elif rot%4==3:
            limits[0]=1
            limits[1]=1
            limits[2]=1
            if mirrored:
                limits[2]=0
    elif blockType==2:
        limits[0]=1
        limits[1]=1
        if rot%2==1:
            limits[2]=1
    elif blockType==3:
        limits[1]=1
    elif blockType==4:
        if rot%2==0:
            limits[2]=1
        else:
            limits[0]=2
            limits[1]=1

    xPos=random.randint(limits[0],blockNumberX-limits[1]-1)
    if blockType==0:
        locs=TBlock((xPos,limits[2]),rot)
    elif blockType==1:
        locs=LBlock((xPos,limits[2]),rot,mirrored)
    elif blockType==2:
        locs=ZBlock((xPos,limits[2]),rot,mirrored)
    elif blockType==3:
        locs=SBlock((xPos,limits[2]))
    elif blockType==4:
        locs=IBlock((xPos,limits[2]),rot)
    #displayStaticBlocks(locs)
    return [xPos,limits[2]],locs,mirrored,blockType
    

def fall(initPos,genLoc):
    global staticBlocks
    if collisionCheck(initPos):
        staticBlocks=checkRowDone()
        return 1,[],[]
    for i in range(0,len(initPos)):
        initPos[i][1]+=1
    genLoc[1]+=1

    return 0,initPos,genLoc

def collisionCheck(locs):
    for pos in locs:
        if ([pos[0],pos[1]+1] in staticBlocks) or (pos[1]+1>=NUM_BLOCKS_Y):
            collision(locs)
            return 1
        else: continue
    return 0

def collision(locs):
    global score
    print("land")
    for pos in locs:
        if pos[1]==0:
            GameOver()
        staticBlocks.append(pos)
        score=score+1

def rotate(genLoc,o,m,blockType,initLocs):
    tempBlocs=[]
    match blockType:
        case 0:
            tempBlocs=TBlock(genLoc,o)
        case 1:
            tempBlocs= LBlock(genLoc,o,m)
        case 2:
            tempBlocs= ZBlock(genLoc,o,m)
        case 3:
            tempBlocs=SBlock(genLoc)
        case 4:
            tempBlocs= IBlock(genLoc,o)
    for pos in tempBlocs:
        if pos in staticBlocks:
            return initLocs
    return tempBlocs

def move(genLoc,locs,d):
    if d:
        for pos in locs:
            if [pos[0]+1,pos[1]] in staticBlocks or pos[0]+1>NUM_BLOCKS_X-1:
                return genLoc,locs
        for i,pos in enumerate(locs):
            locs[i][0]=pos[0]+1
        genLoc[0]+=1
    else:
        for pos in locs:
            if [pos[0]-1,pos[1]] in staticBlocks or pos[0]-1<0:
                return genLoc,locs
        for i,pos in enumerate(locs):
            locs[i][0]=pos[0]-1
        genLoc[0]-=1
    return genLoc,locs

def checkRowDone():
    for i in range(0,NUM_BLOCKS_Y):
        k=0
        for j in range(0,NUM_BLOCKS_X):
            if [j,i] in staticBlocks:
                k+=1
        if k==NUM_BLOCKS_X:
            n=0
            while n!=len(staticBlocks)-1:
                if staticBlocks[n][1]==i:
                    staticBlocks.remove(staticBlocks[n])
                else: n+=1
            for j,block in enumerate(staticBlocks):
                if staticBlocks[j][1]<i:
                    staticBlocks[j]=[block[0],block[1]+1]
    return staticBlocks

def GameOver():
    print("Game Over")
    pygame.quit()

def displayScore():
    scoreText=scoreFont.render('Score: '+str(score),False,(200,200,200))
    scoreRect=scoreText.get_rect(center=(SCREEN_W/2,30))
    screen.blit(scoreText,scoreRect)


import pygame
import random

pygame.init()

GRID_LINE_THICKNESS=3
NUM_BLOCKS_X=10
BLOCK_RATIO=(1,1.8)
NUM_BLOCKS_Y=int(NUM_BLOCKS_X*BLOCK_RATIO[1]/BLOCK_RATIO[0]) 
GRID_SIZE=40
SCREEN_W=((NUM_BLOCKS_X-1)*GRID_LINE_THICKNESS)+GRID_SIZE*NUM_BLOCKS_X
SCREEN_H=((NUM_BLOCKS_Y-1)*GRID_LINE_THICKNESS)+GRID_SIZE*NUM_BLOCKS_Y

BLOCKTYPES=["T","L","z","s","i"] 


gridCol="grey12"
bgColor='black'

scoreFont=pygame.font.Font(None,20)

blockNumberX=int(SCREEN_W/GRID_SIZE)
blockNumberY=int(SCREEN_H/GRID_SIZE)
screen=pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Tetris")
clock=pygame.time.Clock()

timerEvent=pygame.USEREVENT+1


testStart=(1,1)

genLoc,blockPos,mirrored,blockType=generateNewBlock()
Locs=[]
rotation=0
staticBlocks=[]

run=False
paused=False
f=0
score=0
while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type==pygame.KEYDOWN:
            if not run:
                run=True
                pygame.time.set_timer(timerEvent,300)
            else:
                if event.key==pygame.K_UP:
                    rotation-=1
                    blockPos=rotate(genLoc,rotation,mirrored,blockType,blockPos)
                elif event.key==pygame.K_DOWN:
                    rotation+=1
                    blockPos=rotate(genLoc,rotation,mirrored,blockType,blockPos)
                elif event.key==pygame.K_LEFT:
                    genLoc,blockPos=move(genLoc,blockPos,0)
                elif event.key==pygame.K_RIGHT:
                    genLoc,blockPos=move(genLoc,blockPos,1)
                elif event.key==pygame.K_SPACE:
                    if paused:
                        paused=False
                    else:
                        paused=True

        if event.type==timerEvent and not paused:
            f,blockPos,genLoc=fall(blockPos,genLoc)
            if f==1:
                f=0
                genLoc,blockPos,mirrored,blockType=generateNewBlock()
    
    if not paused:
        screen.fill(bgColor)
        displayGrid()
        displayScore()
        displayBlocks(blockPos)
        displayBlocks(staticBlocks)
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)         

