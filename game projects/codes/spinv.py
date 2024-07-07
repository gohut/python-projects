import pygame,sys 
from random import choice,randint

def spaceinvader():
       class Player(pygame.sprite.Sprite):
           def __init__(self,pos,constrain,speed):
               super().__init__()
               self.image=pygame.image.load('D:\\game projects\\pictures\\player.png').convert_alpha()
               self.rect=self.image.get_rect(midbottom=pos)
               self.spd=speed
               self.con=constrain
               self.ready=True
               self.lasertime=0
               self.lasercooldown=600
               self.lasers=pygame.sprite.Group()
               
           def ginput(self):
               keys=pygame.key.get_pressed()
               if keys[pygame.K_RIGHT]:
                   self.rect.x +=self.spd
               elif keys[pygame.K_LEFT]:
                   self.rect.x -=self.spd
               elif keys[pygame.K_SPACE] and self.ready:
                   self.shootlasser()
                   self.ready=False
                   self.lasertime=pygame.time.get_ticks()
           def recharge(self):
               if  not self.ready:
                   currentime=pygame.time.get_ticks()
                   if (currentime - self.lasertime) >=self.lasercooldown:
                       self.ready=True
                   

               
           def dconstrain(self):
               if self.rect.left<=0:
                   self.rect.left=0
               if self.rect.right>=self.con:
                   self.rect.right=self.con


           def shootlasser(self):
               self.lasers.add(Laser((self.rect.center),-8,600))

           def  update(self):
               self.ginput()
               self.dconstrain()
               self.recharge()
               self.lasers.update()

       class Alien(pygame.sprite.Sprite):
           def __init__(self,color,x,y):
               super().__init__()
               file='D:\\game projects\\pictures\\'+color+'.png'
               self.image=pygame.image.load(file).convert_alpha()
               self.rect=self.image.get_rect(topleft=(x,y))
           def update(self,direction):
               self.rect.x+=direction
       class Extra(pygame.sprite.Sprite):
           def __init__(self,side,width):
               super().__init__()
               self.image=pygame.image.load('D:\\game projects\\pictures\\extra.png').convert_alpha()
               if side=='right':
                   x=width+50
                   self.speed=-3
               else:
                   x=-50
                   self.speed=3
               self.rect=self.image.get_rect(topleft=(x,80))
           def update(self):
               self.rect.x+=self.speed
       class Laser(pygame.sprite.Sprite):
           def __init__(self,pos2,speed,height):
               super().__init__()
               self.image=pygame.Surface((4,20))
               self.image.fill('white')
               self.rect=self.image.get_rect(center=pos2)
               self.spd=speed
               self.heigh=height
           def destroy(self):
               if self.rect.y<=-50 or self.rect.y>=self.heigh+50:
                   self.kill()
           def  update(self):
               self.rect.y+=self.spd
               self.destroy()
       class Block(pygame.sprite.Sprite):
           def __init__(self,size,x,y):
               super().__init__()
               self.image=pygame.Surface((size,size))
               self.image.fill('red')
               self.rect=self.image.get_rect(topleft=(x,y))

               
              
               

       class game(Player,Alien,Extra,Laser,Block):
              def __init__(self):
               #player
               psprite=Player((300,600),width,5)
               self.player=pygame.sprite.GroupSingle(psprite)
               #helth&score
               self.lives=3
               self.livesurf=pygame.image.load('D:\\game projects\\pictures\\player.png').convert_alpha()
               self.livesrtpos=width-(self.livesurf.get_size()[0]*2+20)
               self.score=0
               self.font=pygame.font.Font('D:\\game projects\\pictures\\font.ttf',20)




               
               #obstacal
               shape=[
       '    xxx    ',    
       '  xxxxxxx  ',
       'xxxxxxxxxxx',
       'xxxxxxxxxxx',
       'xxxxxxxxxxx',
       'xxx     xxx',
       'xx       xx']
               self.shape=shape
               self.blocksize=5
               self.blocks=pygame.sprite.Group()
               self.obstacleno=4
               self.obxpos=[num*(width/self.obstacleno) for num in range(self.obstacleno)]
               self.multipleobstacle(*self.obxpos,xpos=50,ypos=480)
               #alien
               self.aliens=pygame.sprite.Group()
               self.alienset(rows=6,cols=8)
               self.aliendir=1
               self.alienlaser=pygame.sprite.Group()
               #extra
               self.extra=pygame.sprite.GroupSingle()
               self.spawntime=randint(40,80)

               
               
              def  obstaclem(self,xpos,ypos,offx):
                     for row_index,row in enumerate(self.shape):
                            for col_index,col in enumerate(row):
                                   if col=='x':
                                          x= xpos+col_index*self.blocksize+offx
                                          y= ypos+row_index*self.blocksize          
                                          block=Block(self.blocksize,x,y)
                                          self.blocks.add(block)

              def  multipleobstacle(self,*offset,xpos,ypos,):
                 for offx in offset:
                     self.obstaclem(xpos,ypos,offx)
                       
               
              def alienset(self,rows,cols,xdis=60,ydis=48,xoff=70,yoff=100):
                     for row_index,row in enumerate(range(rows)):
                            for col_index,col in enumerate(range(cols)):
                                   x=col_index*xdis+xoff
                                   y=row_index*ydis+yoff
                                   if row_index==0: aliensprite=Alien('yellow',x,y)
                                   elif 1<= row_index <=2: aliensprite=Alien('green',x,y)
                                   else : aliensprite=Alien('red',x,y)
                                   self.aliens.add(aliensprite)    
               
               
              def alienposcheck(self):
                     allalien=self.aliens.sprites()
                     for alien in allalien:
                            if alien.rect.right>=width:
                                   self.aliendir=-1
                                   self.alienmovedown(2)
                            elif alien.rect.left<=0:
                                   self.aliendir=1
                                   self.alienmovedown(2)
              def alienmovedown(self,distance):
                     if self.aliens:
                            for alien in self.aliens.sprites():
                                   alien.rect.y+=distance
              def dislives(self):
                     for live in range(self.lives-1):
                            x=self.livesrtpos+(live*self.livesurf.get_size()[0]+10)
                            screen.blit(self.livesurf,(x,8))

              def alienshoot(self):
                     if self.aliens.sprites():
                            ranaliens=choice(self.aliens.sprites())
                            self.alienlaser.add(Laser((ranaliens.rect.center),6,600))

              def extratimer(self):
                     self.spawntime-=1
                     if self.spawntime<=0:
                            ch=choice(['right','left'])
                            self.extra.add(Extra(ch,600))
                            self.spawntime=randint(400,800)
              def collisioncheck(self):
                     if self.player.sprite.lasers:
                            for laser in self.player.sprite.lasers:
                                   if pygame.sprite.spritecollide(laser,self.blocks,True):
                                          laser.kill()
                                   if pygame.sprite.spritecollide(laser,self.extra,True):
                                          self.score+=500
                                          laser.kill()
                                   if pygame.sprite.spritecollide(laser,self.aliens,True):
                                          self.score+=100
                                          laser.kill()
                     if self.alienlaser:
                            for laser in self.alienlaser:
                                   if pygame.sprite.spritecollide(laser,self.blocks,True):
                                          laser.kill()
                                   if pygame.sprite.spritecollide(laser,self.player,False):
                                          laser.kill()
                                          self.lives-=1
                                          if self.lives<=0:
                                                 pygame.quit()
                                                 sys.exit()
                     if self.aliens:
                            for alien in self.aliens:
                                   pygame.sprite.spritecollide(alien,self.blocks,True)
                                   if pygame.sprite.spritecollide(alien,self.player,False):
                                          pygame.quit()
                                          sys.exit()
                                          
                                                               
              def disscore(self):
                     scoresurf=self.font.render(f'score:{self.score}',False,'white')
                     scorerect=scoresurf.get_rect(topleft=(0,0))
                     screen.blit(scoresurf,scorerect)


              def victorydisplay(self):
                     if not self.aliens.sprites():
                            vicsurf=self.font.render('You Won',False,'white')
                            vicrect=vicsurf.get_rect(center=(300,300))
                            screen.blit(vicsurf,vicrect)



                     
              def run(self):
                  self.player.update()
                  self.extra.update()
                  self.alienlaser.update()
                  
                  self.aliens.update(self.aliendir)
                  self.extratimer()
                  self.alienposcheck()
                  self.collisioncheck()
                  self.dislives()
                  self.disscore()
                  self.victorydisplay()
                  
                  self.player.sprite.lasers.draw(screen)
                  self.player.draw(screen)
                  self.blocks.draw(screen)
                  self.aliens.draw(screen)
                  self.alienlaser.draw(screen)
                  self.extra.draw(screen)
                  
                  
                  
                  
                  









       if  __name__ =='__main__':
              global width,height,screen,clock
              pygame.init()
              height=600
              width=600
              screen=pygame.display.set_mode((width,height))
              clock=pygame.time.Clock()
              g=game()
              ALIENLASER=pygame.USEREVENT +1
              pygame.time.set_timer(ALIENLASER,800)
              while True:
                     for event in pygame.event.get():
                            if event.type==pygame.QUIT:
                                   pygame.quit()
                                   sys.exit()
                            if event.type==ALIENLASER:
                                   g.alienshoot()
                     screen.fill('black')
                     g.run()
                     pygame.display.flip()
                     clock.tick(60)
spaceinvader()


                     

