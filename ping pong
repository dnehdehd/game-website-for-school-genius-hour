import random
import pygame
import time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("shapes!!")
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
pink=(175,0,175)
orange=(240,100,0)
white=(250,250,250)
black=(0,0,0)
yellow=(250,250,0)
a=[red,blue,green,pink,orange]
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
y2=300
xc=200
yc=240
y=240
w=0
s=0
y1=255
u=0
d=0
m=+0.70
pls=0
m2=+0.63
pls2=0
lh=1
r=20
a= 'LEVEL 1'
bls=0.80
bls2=0.72
WX=260
time.sleep(5)
while True:
    screen.fill(black)
    show_text(f"player 1 score {pls} .",5,5,green,10)
    show_text(f"player 2 score {pls2} .",520,5,green,10)
    show_text(f"{a}",WX,300,green,32)
    pygame.draw.rect(screen,blue,(30,y,10,120))
    pygame.draw.rect(screen,blue,(560,y1,10,120))
    pygame.draw.circle(screen,blue,(xc,yc),r)
    if pls==11:
        while True:
            screen.fill(black)
            show_text(f" PLAYER 1 WINS ",lh,300,green,50)
            pygame.display.update()
            lh+=0.5
            if lh==600:
                lh=-300
    if pls2==11:
        while True:
            screen.fill(black)
            show_text(f" PLAYER 2 WINS ",lh,300,green,50)
            pygame.display.update()
            lh+=0.5
            if lh==600:
                lh=-300
    if pls==2 and pls!=3 and pls2!=3 and pls<3 and pls2<3 or pls2==2 and pls!=3 and pls2!=3 and pls<3 and pls2<3 :
        a=' LEVEL 2'
        r=15
    elif pls>=3 and pls!=5 and pls2!=5 or pls2>=3 and pls!=5 and pls2!=5:
        a=' LEVEL 3'
        bls=0.90
        bls2=0.81
    if pls>=5 and pls<=7 and pls2<=7 or pls2>=5 and pls<=7 and pls2<=7:
        a=' LEVEL 4'
        bls=1
        bls2=0.90
    if pls>=7 or pls2>=7:
        a=' LEVEL 5 FINAL LEVEL'
        WX=200
        bls=1.10
        bls2=1
    if w:
        y-=0.45
    elif s:
        y+=0.45
    if u:
        y1-=0.45
    elif d:
        y1+=0.45
    pygame.display.update()
    if y<=0:
        y=0
    if y>=480:
        y=480
    if y1<=0:
        y1=0
    if y1>=480:
        y1=480
    
    if yc>=600-r:
        m2=-bls2
    if yc<=0+r:
        m2+=bls2
    if xc>=550 and yc>=y1-r and yc<=y1+120:
        m=-bls
    elif xc>=580:
        pls+=1
        xc=300
        yc=200
        y=240
        y1=255
        pygame.time.delay(1500)
    if xc<=50 and yc>=y-r and yc<=y+120:
        m=bls
    elif xc<=20:
        pls2+=1
        xc=300
        yc=400
        y=240
        y1=255
        pygame.time.delay(1500)
    xc+=m
    yc+=m2
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                w=1
                s=0
            if event.key==pygame.K_s:
                w=0
                s=1
            if event.key==pygame.K_UP:
                u=1
                d=0
            if event.key==pygame.K_DOWN:
                d=1
                u=0
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                w=0
                s=0
            if event.key==pygame.K_s:
                s=0
                w=0
            if event.key==pygame.K_UP:
                u=0
            if event.key==pygame.K_DOWN:
                d=0
