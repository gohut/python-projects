
import random
import pygame,sys
xpos=7*random.choice((1,-1))
ypos=7*random.choice((1,-1))
playerspeed=0
enemyspeed=7
playerscore=0
enemyscore=0
scoretime=True
def pong():
    global xpos,ypos,playerspeed,enemyspeed,playerscore,enemyscore,scoretime
    pygame.init()
    clock=pygame.time.Clock()
    width=900
    height=600
    screen=pygame.display.set_mode((width,height))
    pygame.display.set_caption('pong')

    
    #score
    
    gamefont=pygame.font.Font("freesansbold.ttf",32)
    #function
    def ballani():
        global xpos,ypos,playerscore,enemyscore,scoretime
        ball.x+=xpos
        ball.y+=ypos
        
        if ball.top <=0 or ball.bottom>= height:
            ypos*=-1
        if ball.left<=0:
            playerscore+=1
            scoretime=pygame.time.get_ticks()

        if ball.right>=width:
            enemyscore+=1
            scoretime=pygame.time.get_ticks()

            
        if ball.colliderect(player) and xpos>0 :
            xpos*=-1
        if     ball.colliderect(enemy)and xpos<0 :
            xpos*=-1
            
    def playerani():
         player.y+=playerspeed
         if player.top <=0:
             player.top=0
         if player.bottom>=height:
             player.bottom=height
    def enemyani():
        if enemy.top <ball.y:
            enemy.top+=enemyspeed
        if enemy.bottom>ball.y:
            enemy.bottom-=enemyspeed
        if enemy.top<=0:
            enemy.top=0
        if enemy.bottom>=height:
            enemy.bottom-=height
        
             
    def restart():
        global xpos,ypos,playerscore,enemyscore,scoretime

        currenttime=pygame.time.get_ticks()
        ball.center=(width/2,height/2)

        if currenttime-scoretime<2100:
            xpos,ypos=0,0
        else:
            ypos=7*random.choice((1,-1))
            xpos=7*random.choice((1,-1))
           
            scoretime=None
        

        



    #rects
    ball=pygame.Rect(width/2-15,height/2-15,15,15)
    player=pygame.Rect(width-10,height/2-80,5,100)
    enemy=pygame.Rect(0,height/2-70,5,100)

    bg=pygame.Color('white')




    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if  event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    playerspeed+=7
                if event.key==pygame.K_UP:
                    playerspeed-=7
            if  event.type==pygame.KEYUP:
               if event.key==pygame.K_DOWN:
                   playerspeed-=7
               if event.key==pygame.K_UP:
                   playerspeed+=7        
           
                    
                        

        ballani()
        playerani()
        enemyani()
        if scoretime:
            restart()    
       
        screen.fill(bg)       
        pygame.draw.rect(screen,'black',player)
        pygame.draw.rect(screen,'black',enemy)       
        pygame.draw.ellipse(screen,'grey12',ball)       
        pygame.draw.aaline(screen,'black',(width/2,0),(width/2,height))

     
        
        ptext=gamefont.render(f'score: {playerscore}',False,'grey')
        screen.blit(ptext,(600,10))

        etext=gamefont.render(f'score: {enemyscore}',False,'grey')
        screen.blit(etext,(120,10))



        pygame.display.flip()
        clock.tick(60)
  
