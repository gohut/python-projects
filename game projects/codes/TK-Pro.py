from tkinter import*
from PIL import ImageTk,Image
import flappybird,PONG
import spinv

gwidth=1100
gheight=600
win=Tk()
win.geometry(f'{gwidth}x{gheight}')
win.title('retro game zone')
#images
fr1=                  'D:\\game projects\\pictures\\frame1.jpg'
fr2=                  'D:\\game projects\\pictures\\frame2.jpg'
fr3=                  'D:\\game projects\\pictures\\frame3.jpg'
fr4=                  'D:\\game projects\\pictures\\frame4.jpg'
fr5=                  'D:\\game projects\\pictures\\frameoni.jpg'
spaceinvader='D:\\game projects\\pictures\\spaceinvader.jpg'
pong=              'D:\\game projects\\pictures\\pong.png'
flapybird=       'D:\\game projects\\pictures\\flapybrd.png'
enterb=           'D:\\game projects\\pictures\\enter.jpg'
onlineb=         'D:\\game projects\\pictures\\ongame.jpg'
oflineb=          'D:\\game projects\\pictures\\ofgame.jpg'
pause=            'D:\\game projects\\pictures\\pause.png'
mm=               'D:\\game projects\\pictures\\MM.jpg'
settings=        'D:\\game projects\\pictures\\settings.jpg'
back=             'D:\\game projects\\pictures\\back.jpg'
EF=                 'D:\\game projects\\pictures\\exitfrm.jpg'
gm1=             'D:\\game projects\\pictures\\g1.webp'
gm2=             'D:\\game projects\\pictures\\g2.jpg'
gm3=             'D:\\game projects\\pictures\\g3.jfif'
gm4=             'D:\\game projects\\pictures\\g4.jpg'
gm5=             'D:\\game projects\\pictures\\g5.png'
gm6=             'D:\\game projects\\pictures\\g6.jpg'
gm7 =            'D:\\game projects\\pictures\\g7.jpg'
gm8=            'D:\\game projects\\pictures\\ff.png'
font22=         'C:\\Users\\Ajithkumar\\OneDrive\\Pictures\\fontm.ttf'

frame2=Frame(win,width=gwidth,height=gheight)
frame2.place(anchor='center',relx=0.5,rely=0.5)
bg1=Image.open(fr2)
bg2=bg1.resize((gwidth,gheight))
mbg=ImageTk.PhotoImage(bg2)
label=Label(frame2,image=mbg)
label.pack(side=TOP)
bg1.bg2=mbg

def frm3():
    fm3=Frame(win,width=gwidth,height=gheight)
    fm3.place(x=0,y=0)
    bg1=Image.open(fr3)
    bg2=bg1.resize((gwidth,gheight))
    mbg=ImageTk.PhotoImage(bg2)
    bg1=Label(fm3,image=mbg)
    bg1.place(x=0,y=0)
    bg1.bg2=mbg
    def frm4():
        fm4=Frame(win,width=gwidth,height=gheight)
        fm4.place(x=0,y=0)
        bg1=Image.open(fr4)
        bg2=bg1.resize((gwidth,gheight))
        mbg=ImageTk.PhotoImage(bg2)
        bg1=Label(fm4,image=mbg)
        bg1.place(x=0,y=0)
        bg1.bg2=mbg
        
        bimg=Image.open(spaceinvader)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fm4,image=bimg3,command=spinv.spaceinvader)
        enter.place(x=100,y=100)
        enter.bimg2=bimg3
        l1=Label(fm4,text='space invaders',font=(font22,10),bg='white').place(x=110,y=210)
        
        bimg=Image.open(flapybird)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fm4,image=bimg3,command=flappybird.flappybird)
        enter.place(x=250,y=100)
        enter.bimg2=bimg3
        l2=Label(fm4,text='flappybird',font=(font22,10),bg='white').place(x=270,y=210)
        
        
        bimg=Image.open(pong)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fm4,image=bimg3,command=PONG.pong)
        enter.place(x=400,y=100)
        enter.bimg2=bimg3
        l3=Label(fm4,text='pong',font=(font22,10),bg='white').place(x=440,y=210)
        
        def exitframe():
            frmef=Frame(win,width=300,height=300)
            frmef.place(x=450,y=100)
            bg1=Image.open(EF)
            bg2=bg1.resize((300,300))
            mbg=ImageTk.PhotoImage(bg2)
            bg1=Label(frmef,image=mbg)
            bg1.place(x=0,y=0)
            bg1.bg2=mbg
    
        
            
            def f1():      
                fm4.destroy()
                frmef.destroy()

            bimg=Image.open(back)
            bimg2=bimg.resize((250,50))
            bimg3=ImageTk.PhotoImage(bimg2)
            enter=Button(frmef,image=bimg3,command=f1)
            enter.place(x=20,y=50)
            enter.image=bimg3

            
            def f():
                
                fm4.destroy()
                fm3.destroy()
                frmef.destroy()
                
            bimg=Image.open(mm)
            bimg2=bimg.resize((250,50))
            bimg3=ImageTk.PhotoImage(bimg2)
            enter=Button(frmef,image=bimg3,command=f)
            enter.place(x=20,y=150)
            enter.enter=bimg3
                    

        bimg=Image.open(pause)
        bimg2=bimg.resize((50,50))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fm4,image=bimg3,command=exitframe)
        enter.place(x=5,y=5)
        enter.bimg2=bimg3

    def frameon():
        fmon=Frame(win,width=gwidth,height=gheight)
        fmon.place(x=0,y=0)
        bg1=Image.open(fr5)
        bg2=bg1.resize((gwidth,gheight))
        mbg=ImageTk.PhotoImage(bg2)
        bg1=Label(fmon,image=mbg)
        bg1.place(x=0,y=0)
        bg1.bg2=mbg
        
        bimg=Image.open(gm1)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=100,y=100)
        enter.bimg2=bimg3
        l1=Label(fmon,text='street fighters',font=(font22,10),bg='white').place(x=110,y=210)
        

        bimg=Image.open(gm2)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=250,y=100)
        enter.bimg2=bimg3
        l1=Label(fmon,text='grand theft auto',font=(font22,10),bg='white').place(x=250,y=210)
       
        
        bimg=Image.open(gm3)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=400,y=100)
        enter.bimg2=bimg3
        l1=Label(fmon,text='pac man',font=(font22,10),bg='white').place(x=430,y=210)
       
        
        bimg=Image.open(gm4)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=100,y=250)
        enter.bimg2=bimg3
        l1=Label(fmon,text='super sonic',font=(font22,10),bg='white').place(x=110,y=360)
       
        
        bimg=Image.open(gm5)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=250,y=250)
        enter.bimg2=bimg3
        l1=Label(fmon,text='Zelda',font=(font22,10),bg='white').place(x=290,y=360)
       
        
        bimg=Image.open(gm6)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=400,y=250)
        enter.bimg2=bimg3
        l1=Label(fmon,text='Mortal Combat',font=(font22,10),bg='white').place(x=410,y=360)
       
         
        bimg=Image.open(gm7)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=100,y=400)
        enter.bimg2=bimg3
        l1=Label(fmon,text='Big Hand',font=(font22,10),bg='white').place(x=120,y=510)
       

        bimg=Image.open(gm8)
        bimg2=bimg.resize((100,100))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3)
        enter.place(x=250,y=400)
        enter.bimg2=bimg3
        l1=Label(fmon,text='Free Fire',font=(font22,10),bg='white').place(x=270,y=510)
       
        def exitframe2():
            frmef2=Frame(win,width=300,height=300)
            frmef2.place(x=450,y=100)
            bg1=Image.open(EF)
            bg2=bg1.resize((300,300))
            mbg=ImageTk.PhotoImage(bg2)
            bg1=Label(frmef2,image=mbg)
            bg1.place(x=0,y=0)
            bg1.bg2=mbg
    
            def f1():      
                fmon.destroy()
                frmef2.destroy()

            bimg=Image.open(back)
            bimg2=bimg.resize((250,50))
            bimg3=ImageTk.PhotoImage(bimg2)
            enter=Button(frmef2,image=bimg3,command=f1)
            enter.place(x=20,y=50)
            enter.image=bimg3

            
            def f():
                
                fmon.destroy()
                fm3.destroy()
                frmef2.destroy()
                
            bimg=Image.open(mm)
            bimg2=bimg.resize((250,50))
            bimg3=ImageTk.PhotoImage(bimg2)
            enter=Button(frmef2,image=bimg3,command=f)
            enter.place(x=20,y=150)
            enter.enter=bimg3
            
        
        


        bimg=Image.open(pause)
        bimg2=bimg.resize((50,50))
        bimg3=ImageTk.PhotoImage(bimg2)
        enter=Button(fmon,image=bimg3,command=exitframe2)
        enter.place(x=5,y=5)
        enter.bimg2=bimg3
    
    bimg=Image.open(onlineb)
    bimg2=bimg.resize((250,50))
    bimg3=ImageTk.PhotoImage(bimg2)
    enter=Button(fm3,image=bimg3,command=frameon)
    enter.place(x=170,y=150)
    enter.bimg2=bimg3

    
    
    bimg=Image.open(oflineb)
    bimg2=bimg.resize((250,50))
    bimg3=ImageTk.PhotoImage(bimg2)
    enter=Button(fm3,image=bimg3,command=frm4)
    enter.place(x=170,y=280)
    enter.bimg2=bimg3




bimg=Image.open(enterb)
bimg2=bimg.resize((250,50))
bimg3=ImageTk.PhotoImage(bimg2)
enter=Button(frame2,image=bimg3,command=frm3)
enter.place(x=670,y=370)
enter.bimg2=bimg3


bimg=Image.open(settings)
bimg2=bimg.resize((250,50))
bimg3=ImageTk.PhotoImage(bimg2)
enter=Button(frame2,image=bimg3,command=frm3)
enter.place(x=670,y=470)
enter.bimg2=bimg3


frame=Frame(win,width=gwidth,height=gheight)
frame.place(anchor='center',relx=0.5,rely=0.5)
img=Image.open(fr1)
nimg=img.resize((gwidth,gheight))
img2=ImageTk.PhotoImage(nimg)
label=Label(frame,image=img2)
label.pack(side=TOP)
win.after(3000,frame.destroy)
    

    


