import random
import pygame,sys

floorpos=0
gravity=0.25
pmo=0
game=True
score=0
highscore=0
def flappybird():
     global floorpos,gravity,pmo,game,score,highscore
     pygame.init()
     screen=pygame.display.set_mode((450,650))
     clock=pygame.time.Clock()

     gamefont=pygame.font.Font("freesansbold.ttf",30)

     bg_surface=pygame.image.load('D:\\game projects\\pictures\\rbg.jpg').convert()
     bg_surface=pygame.transform.scale(bg_surface,(476,650))

     floorsurface=pygame.image.load('D:\\game projects\\pictures\\base22.jpg').convert()
     floorsurface=pygame.transform.scale(floorsurface,(500,100))


     player=pygame.image.load('D:\\game projects\\pictures\\b3.png').convert()
     prect=player.get_rect(center=(100,312))

     pipe=pygame.image.load('D:\\game projects\\pictures\\mp.png').convert_alpha()
     pipe=pygame.transform.scale(pipe,(80,400))
     re=pygame.image.load('D:\\game projects\\pictures\\message.png').convert_alpha()
     re=pygame.transform.scale(re,(300,400))
     pre=re.get_rect(center=(220,270))


     pipelist=[]
     SPAWNPIPE=pygame.USEREVENT
     pygame.time.set_timer(SPAWNPIPE,1200)
     pipeheight=[300,400,350,420]


     #variables

     def floor():
          screen.blit(floorsurface,(floorpos,550))
          screen.blit(floorsurface,(floorpos+476,550))
     def createpipe():
         ran=random.choice(pipeheight)
         
         bpipe=pipe.get_rect(midtop=(600,ran+50))
         tpipe=pipe.get_rect(midbottom=(550,ran-150))
         return bpipe,tpipe
     def movepipes(pipes):
         for p in pipes:
             p.centerx-=5
         return pipes
     def drawpipes(pipes):
         for p in pipes:
             if p.bottom>=650:
                 screen.blit(pipe,p)
             else:
                 flipipe=pygame.transform.flip(pipe,False,True)
                 screen.blit(flipipe,p)
     def checkcollision(pipes):
          for p in pipes:
               if prect.colliderect(p):
                    return False
          if prect.top<=-100 or prect.bottom>= 550:
                    return False
          return True
     def scoredisplay(a):
          global score
          if a=='start':
               ptext=gamefont.render(f'{int(score)}',False,'white')
               screen.blit(ptext,(230,10))
          if a=='end':
               sd=gamefont.render(f'Score: {int(score)}',False,'white')
               screen.blit(sd,(160,10))
              
             
          if a=='end':
               hs=gamefont.render(f'Hight Score: {int(score)}',False,'white')
               screen.blit(hs,(110,500))
     def updatehs(score,highscore):
          if score > highscore:
               highscore=score
          return highscore     




     while True:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

             if  event.type == pygame.KEYDOWN:
                 if  event.key == pygame.K_SPACE and game:
                     pmo=0
                     pmo-=12
                     
                 if   event.key == pygame.K_SPACE and game==False:
                      game =True
                      pipelist.clear()
                      prect.center=(100,312)
                      pmo=0
                      score=0
       
             if event.type == SPAWNPIPE:
                  pipelist.extend(createpipe())
               
          #bg          
         screen.blit(bg_surface,(0,0))
        

         
         if game:
              #pipe
              #screen.blit(pipe,(300,300))
              pipelist=movepipes(pipelist)
              drawpipes(pipelist)
              #player
              pmo+=gravity
              prect.centery+=pmo
              screen.blit(player,prect)
              game=checkcollision(pipelist)
              score+=0.01
              scoredisplay('start')
         else:
              screen.blit(re,pre)
              highscore=updatehs(score,highscore)
              scoredisplay('end')
              
              
              
          #floor
         floorpos-=1
         floor()
         if floorpos<=-476:
             floorpos=0

         pygame.display.update()
         clock.tick(60)

