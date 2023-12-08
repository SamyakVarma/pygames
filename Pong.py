#Python 3.11.4

def ballRestart():
    global ballSpeedX,ballSpeedY,ballColInt,shotCounter
    shotCounter=0
    ballColInt=0
    ball.center=(screenWidth/2-15,screenHeight/2-15)
    ballSpeedY=7*random.choice((1,-1))
    ballSpeedX=7*random.choice((1,-1))
    return shotCounter

def displayScore():
    scoreText1=font.render('P1: '+str(score1) ,True, lightGrey)
    scoreRect1=scoreText1.get_rect(center=(screenWidth/4,40))

    scoreText2=font.render('P2: '+str(score2) ,True, lightGrey)
    scoreRect2=scoreText1.get_rect(center=(screenWidth-(screenWidth/4),40))

    screen.blit(scoreText1,scoreRect1)
    screen.blit(scoreText2,scoreRect2)

def restartGame():
    paddle1.center=(10,screenHeight/2)
    paddle2.center=(screenWidth-20,screenHeight/2)
    ball.center=(0,0)
    ballSpeedY=7*random.choice((1,-1))
    ballSpeedX=7*random.choice((1,-1))
    paddleSpeed1=0
    paddleSpeed1=0

def compPlay(opponentSpeed):
    if paddle2.top<ball.y:
        paddle2.top+=opponentMove
    if paddle2.bottom>ball.y:
        paddle2.bottom-=opponentMove

def startScreen(colorInt):
    if colorInt<1.9:
        colorInt=colorInt+0.05
    else:
        colorInt=0
    screen.fill(bgColor)
    titleText=font.render('| PONG |',True, lightGrey)
    titleRect=titleText.get_rect(center=(screenWidth/2,80))

    if gameSelected==1:
        players1Text=font.render('1 Player',True, lightGrey)
        players1Rect=players1Text.get_rect(center=(screenWidth/4,170))

        players2Text=font.render('2 Players',True, (100,100,100))
        players2Rect=players2Text.get_rect(center=(screenWidth-(screenWidth/4),170))
    
    if gameSelected==0:
        players1Text=font.render('1 Player',True, (100,100,100))
        players1Rect=players1Text.get_rect(center=(screenWidth/4,170))

        players2Text=font.render('2 Players',True,lightGrey)
        players2Rect=players2Text.get_rect(center=(screenWidth-(screenWidth/4),170))

    difficultyText=font.render('Difficulty: '+str(difficultyLevel[difficulty]),True, lightGrey)
    difficultyRect=difficultyText.get_rect(center=(screenWidth/2,screenHeight/2))

    playText=font.render('Press SPACE to play!',True, clickColor[int(colorInt)])
    playRect=playText.get_rect(center=(screenWidth/2,screenHeight-150))

    screen.blit(titleText,titleRect)
    screen.blit(players1Text,players1Rect)
    screen.blit(players2Text,players2Rect)
    screen.blit(difficultyText,difficultyRect)
    screen.blit(playText,playRect)
    return colorInt

def powerShot(shotCounter):
    global ballColInt,ballSpeedX
    fastBallSpeed=14
    if shotCounter==5:
        ballColInt=1
        ballSpeedX=fastBallSpeed
    if shotCounter==7 :
        ballColInt=0
        shotCounter=0
        if ballSpeedX>0:
            ballSpeedX=7
        if ballSpeedX<0:
            ballSpeedX=-7

    return shotCounter

def pauseScreen():
    menuText=font.render('Menu(Press M)',True, lightGrey)
    menuRect=menuText.get_rect(center=(screenWidth/2,screenHeight/2))
    screen.fill((20,20,20))
    pygame.draw.rect(screen,(100,100,100),paddle1)
    pygame.draw.rect(screen,(100,100,100),paddle2)
    pygame.draw.ellipse(screen,(100,100,100),ball)
    pygame.draw.aaline(screen,(100,100,100),(screenWidth/2,0),(screenWidth/2,screenHeight))
    screen.blit(menuText,menuRect)
    displayScore()


import pygame, random
from sys import exit
pygame.init()

screenWidth=900
screenHeight=560
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Pong')
clock=pygame.time.Clock()

ball=pygame.Rect(screenWidth/2-15,screenHeight/2-15,30,30)
paddle2=pygame.Rect(screenWidth-20,screenHeight/2-70,10,140)
paddle1=pygame.Rect(10,screenHeight/2-70,10,140)

font=pygame.font.Font(None,80)

bgColor=pygame.Color('grey12')
lightGrey=(200,200,200)

ballSpeedX=7*random.choice((1,-1))
ballSpeedY=7*random.choice((1,-1))

paddleSpeed=0
paddleMove=12
opponentSpeed=0
opponentMove=12

score1=0
score2=0

gameSelected=1

difficulty=0
difficultyLevel=['Easy','Medium','Hard']

gameState=False
paused=False
pauseClicked=False

clickColor=[(200,200,200),(100,100,100)]
colorInt=0

paddleSpeed1=0
paddleSpeed2=0
paddleSpeedStep=1
movePressed1=False
movePressed2=False
movePressDirection1='N'
movePressDirection2='N'

ballColInt=0
ballCol=[lightGrey,(100,0,0)]
shotCounter=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if gameState:
                if difficulty!=2:
                    if event.key==pygame.K_DOWN and gameState==True:
                        paddleSpeed1+=paddleMove
                    if event.key==pygame.K_UP and gameState==True:
                        paddleSpeed1-=paddleMove
                    if gameSelected==0:
                        if event.key==pygame.K_s:
                            paddleSpeed2+=paddleMove

                        if event.key==pygame.K_w:
                            paddleSpeed2-=paddleMove
                if difficulty==2:
                    if event.key==pygame.K_DOWN:
                        movePressDirection1='D'
                        movePressed1=True
                    if event.key==pygame.K_UP:
                        movePressDirection1='U'
                        movePressed1=True
                    if gameSelected==0:
                        if event.key==pygame.K_s:
                            movePressDirection2='D'
                            movePressed2=True
                        if event.key==pygame.K_w:
                            movePressDirection2='U'
                            movePressed2=True
                if event.key==pygame.K_ESCAPE and paused==False and pauseClicked==False:
                    print('paused')
                    paused=True
                    pauseClicked=True
                if (event.key==pygame.K_SPACE or event.key==pygame.K_ESCAPE) and paused ==True and pauseClicked==False:
                    paused=False
                    pauseClicked=True

                if paused==True:
                    if event.key==pygame.K_m:
                        print('menu')
                        paused=False
                        pauseClicked=False
                        gameState=False
                        startScreen(colorInt)
            if event.key==pygame.K_SPACE and paused == False:
                restartGame()
                gameState=True
                score1=0
                score2=-1
            if gameState==False:
                if event.key==pygame.K_DOWN:
                    if difficulty>0:
                        difficulty-=1
                if event.key==pygame.K_UP:
                    if difficulty<2:
                        difficulty+=1
                if event.key==pygame.K_LEFT:
                    if gameSelected==0:
                        gameSelected=1
                if event.key==pygame.K_RIGHT:
                    if gameSelected==1:
                        gameSelected=0
        if event.type==pygame.KEYUP:
            if difficulty != 2:
                if event.key==pygame.K_DOWN and gameState==True:
                    paddleSpeed1-=paddleMove
                if event.key==pygame.K_UP and gameState==True:
                    paddleSpeed1+=paddleMove
                if gameSelected==0:
                    if event.key==pygame.K_s:
                        paddleSpeed2-=paddleMove
                    if event.key==pygame.K_w:
                        paddleSpeed2+=paddleMove

            if difficulty == 2:
                if event.key==pygame.K_DOWN and gameState==True:
                    movePressed1=False
                    movePressDirection1='N'
                if event.key==pygame.K_UP and gameState==True:
                    movePressed1=False
                    movePressDirection1='N'
                if gameSelected==0:
                    if event.key==pygame.K_s and gameState==True:
                        movePressed2=False
                        movePressDirection2='N'
                    if event.key==pygame.K_w and gameState==True:
                        movePressed2=False
                        movePressDirection2='N'
            if event.key==pygame.K_ESCAPE and pauseClicked==True:
                pauseClicked=False
    
    if gameState and (not paused):
        ball.x+=ballSpeedX
        ball.y+=ballSpeedY

        paddle1.y+=paddleSpeed1

        if difficulty!=2:
            if paddle1.top<=0:
                paddle1.top=0
            if paddle1.bottom>=screenHeight:
                paddle1.bottom=screenHeight
            if paddle2.top<=0:
                paddle2.top=0
            if paddle2.bottom>=screenHeight:
                paddle2.bottom=screenHeight

        if ball.top<=0 or ball.bottom>=screenHeight:
                ballSpeedY*=-1
        
        if difficulty!=0:
            shotCounter=powerShot(shotCounter)
            
        if difficulty==1:
            if paddleSpeed1>0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=7
            if paddleSpeed1<0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=7
            if paddleSpeed1>0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=7
            if paddleSpeed1<0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=7
            
            if paddleSpeed2>0 and ballSpeedY>0 and ball.colliderect(paddle2) and ballSpeedY<=7:
                ballSpeedY+=7
            if paddleSpeed2<0 and ballSpeedY<0 and ball.colliderect(paddle2) and ballSpeedY>=-7:
                ballSpeedY-=7
            if paddleSpeed2>0 and ballSpeedY<0 and ball.colliderect(paddle2) and ballSpeedY<=7:
                ballSpeedY+=7
            if paddleSpeed2<0 and ballSpeedY>0 and ball.colliderect(paddle2) and ballSpeedY>=-7:
                ballSpeedY-=7
            if ballSpeedY==0:
                ballSpeedY=3

        if difficulty==2:
            if movePressed1==True:
                if movePressDirection1=='D':
                    paddleSpeed1+=paddleSpeedStep
                if movePressDirection1=='U':
                    paddleSpeed1-=paddleSpeedStep
                if paddle1.top<=0:
                    paddle1.top=0
                if paddle1.bottom>=screenHeight:
                    paddle1.bottom=screenHeight
            if gameSelected==0:
                if movePressed2==True:
                    if movePressDirection2=='D':
                        paddleSpeed2+=paddleSpeedStep
                    if movePressDirection2=='U':
                        paddleSpeed2-=paddleSpeedStep
                    if paddle2.top<=0:
                        paddle2.top=0
                    if paddle2.bottom>=screenHeight:
                        paddle2.bottom=screenHeight
            
            if movePressed1==False and paddleSpeed1>0:
                paddleSpeed1-=0.5
                if paddle1.bottom>=screenHeight:
                    paddleSpeed1*=-1

            if movePressed1==False and paddleSpeed1<0:
                paddleSpeed1+=0.5
                if paddle1.top<=0:
                    paddleSpeed1*=-1
            if gameSelected==0:
                if movePressed2==False and paddleSpeed2>0:
                    paddleSpeed2-=0.5
                    if paddle2.bottom>=screenHeight:
                        paddleSpeed2*=-1

                if movePressed2==False and paddleSpeed2<0:
                    paddleSpeed2+=0.5
                    if paddle2.top<=0:
                        paddleSpeed2*=-1
            
            if paddleSpeed1>0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=min(paddleSpeed1/2,20)
                if ballSpeedY>20: ballSpeedY=20
            if paddleSpeed1<0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=max(paddleSpeed1/2,-20)
                if ballSpeedY<-20: ballSpeedY=-20
            if paddleSpeed1>0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=min(paddleSpeed2/2,20)
                if ballSpeedY>20: ballSpeedY=20
            if paddleSpeed1<0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=max(paddleSpeed2/2,-20)
                if ballSpeedY<-20: ballSpeedY=-2
            
            if paddleSpeed2>0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=min(paddleSpeed2/2,20)
                if ballSpeedY>20: ballSpeedY=20
            if paddleSpeed2<0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=max(paddleSpeed2/2,-20)
                if ballSpeedY<-20: ballSpeedY=-20
            if paddleSpeed2>0 and ballSpeedY<0 and ball.colliderect(paddle1) and ballSpeedY<=7:
                ballSpeedY+=min(paddleSpeed2/2,20)
                if ballSpeedY>20: ballSpeedY=20
            if paddleSpeed2<0 and ballSpeedY>0 and ball.colliderect(paddle1) and ballSpeedY>=-7:
                ballSpeedY-=max(paddleSpeed2/2,-20)
                if ballSpeedY<-20: ballSpeedY=-20
                            

            if ballSpeedY==0:
                ballSpeedY=3


        if ball.left<=0 or ball.right>=screenWidth:
            if ball.left<=0: score2+=1
            if ball.right>=screenWidth: score1+=1
            shotCounter=ballRestart()

        if gameSelected==1: 
            compPlay(opponentSpeed)
        else:
            paddle2.y+=paddleSpeed2

        if ball.colliderect(paddle1) or ball.colliderect(paddle2):
            ballSpeedX*=-1
            shotCounter+=1
        
        screen.fill(bgColor)
        pygame.draw.rect(screen,lightGrey,paddle1)
        pygame.draw.rect(screen,lightGrey,paddle2)
        pygame.draw.ellipse(screen,ballCol[ballColInt],ball)
        pygame.draw.aaline(screen,lightGrey,(screenWidth/2,0),(screenWidth/2,screenHeight))
        displayScore()
    if gameState and paused:
        pauseScreen()
        
    if not gameState:
        colorInt=startScreen(colorInt)

    pygame.display.flip()


    pygame.display.update()
    clock.tick(60)
