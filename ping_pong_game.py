import time
import pygame,sys,random
from pygame.locals import *
import math
from pygame import mixer

pygame.init()
screenlenth=800
screen=pygame.display.set_mode((screenlenth,screenlenth))
line=20

x=100
y=100

count=0
#background
sg1=pygame.image.load('basket_ball.jpg')
sg1=pygame.transform.scale(sg1,(800,800))

sg2=pygame.image.load('wood_texture_2.jpg')
sg2=pygame.transform.scale(sg2,(800,800))

go=pygame.image.load('godance.jpg')
go=pygame.transform.scale(go,(screenlenth,screenlenth))

def gameover():
    fonts3=pygame.font.Font('freesansbold.ttf',50)
    g2=fonts3.render("YOUR SCORE: "+str(count),True,(235, 238, 242))
    gom=mixer.Sound('astronomia_remix.wav')
    gom.play()
    screen.blit(g2,(200,650))

col=mixer.Sound('laser.wav')

p=300
px=0
pp=5

xp=random.randint(200,300)/100
yp=random.randint(200,300)/100
    
r=40
h=35
w=200
def player(x1,x2):
    pygame.draw.ellipse(screen,(255,0,0),(x2-w/2,0,w,h))
    pygame.draw.ellipse(screen,(0,255,0),(x1,screenlenth-h,w,h))

def text_objects(text, font):
    textSurfac = font.render(text, True, (255,255,255))
    return textSurfac, textSurfac.get_rect()
 
def button(text,x,y,w,h,c1,c2,ask):
    mice=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()

   

    if((x+w>mice[0]>x) and (y+h>mice[1]>y)):
        
        if click[0]==1:
            clm=mixer.Sound('laser.wav')
            clm.play()
            return ask
    else:pygame.draw.rect(screen,c1,(x,y,w,h))
    buttontext=pygame.font.Font('freesansbold.ttf',40)
    textsurf,textRect=text_objects(text,buttontext)
    textRect.center=( (x+(w/2)), (y+(h/2)) )
    screen.blit(textsurf,textRect)
playmusic=True
if playmusic:
    mixer.music.load('Pim Poy.wav ')
    mixer.music.play(-1) 


running=False
intro = True
game=True
screen.fill((66, 236, 245))


while intro:
    screen.fill((66, 236, 245))
    screen.blit(sg1,(0,0))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.quit()
        
        action= button("PLAY",300,450,200,60,(75, 97, 70),(45, 224, 0),"start")       
        if (action=="start"):
            running=True
            intro=False
        pygame.display.update()
while running:
    screen.fill((120, 57, 1))
    screen.blit(sg2,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
                sys.exit()
                running=False
        if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    running=False
        if (event.type==pygame.KEYDOWN):
              if(event.key==pygame.K_RIGHT):
                  px= pp
              elif(event.key==pygame.K_LEFT):
                  px= pp*(-1)
                
        if (event.type==pygame.KEYUP):
              if(event.key==pygame.K_RIGHT) or (event.key==pygame.K_LEFT) :
                  px=0
     
                  
    if(p<=0):
          # px=0
          p=0    
    if(p>=screenlenth-w):
          # px=0
          p=screenlenth-w         
          
    if((x>=screenlenth-r) or (x<=r)):
        xp=xp*(-1)
        
    if((y<=r+h)):
        yp=yp*(-1)
        col.play()

    if(((screenlenth-r>y>=screenlenth-r-h)) and (p<=x<=p+w)):
        yp=yp*(-1)
        y=screenlenth-r-h
        count+=1;xp=xp*1.1;yp=yp*1.1
        pp=pp*1.1
        col.play()

    if(((y>=screenlenth+r))):
          game=0
          screen.blit(go,(0,0)) 
          gameover()
          
    x+=xp
    y+=yp
    p+=px
    if(x>=screenlenth-w/2):xx=screenlenth-w/2
    elif(x<=w/2):xx=w/2
    else:xx=x
    if(game):
        pygame.draw.circle(screen,(255,255,255),(int(screenlenth/2),int(screenlenth/2)),int(200),2)
        pygame.draw.line(screen,(255,255,255),(0,int(screenlenth/2)),(screenlenth,int(screenlenth/2)),2)
        player(p,xx)
        pygame.draw.circle(screen,(int(x/4)+60,int(y/5)+55,int(((x*y)**(.5))/5)+55),(int(x),int(y)),int(r),25)
        pygame.draw.circle(screen,(0,0,0),(int(x),int(y)),int(r),1)

    
    pygame.display.update()