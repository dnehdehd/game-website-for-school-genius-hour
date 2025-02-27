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
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
l=['x','o']
p=0
x=0
y=0
x1=0
o=0
p1=0
x2=0
o1=0
a=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0
x3=0
x4=0
x5=0
x6=0
x7=0
x8=0
x9=0
o2=0
o3=0
o4=0
o5=0
o6=o
o7=0
o8=0
t=0
while True:
    pygame.draw.line(screen,white,(240,150),(240,540))
    pygame.draw.line(screen,white,(370,150),(370,540))
    pygame.draw.line(screen,white,(110,280),(500,280))
    pygame.draw.line(screen,white,(110,410),(500,410))
    pygame.draw.rect(screen,white,(110,150,390,390),1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEMOTION:
            x,y=event.pos
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                x,y=event.pos
                if x>=110 and x<=239 and y>=150 and y<=279:
                    p+=1
                    if p>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",110,50,white,240)
                        if a==0:
                            x1+=1
                        else:
                            o+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=240 and x<=369 and y>=150 and y<=279:
                    p1+=1
                    if p1>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",240,50,white,240)
                        if a==0:
                            x2+=1
                        else:
                            o1+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=370 and x<=500 and y>=150 and y<=279:
                    p2+=1
                    if p2>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",370,50,white,240)
                        if a==0:
                            x3+=1
                        else:
                            o2+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=110 and x<=239 and y>=280 and y<=409:
                    p3+=1
                    if p3>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",110,180,white,240)
                        if a==0:
                            x4+=1
                        else:
                            o3+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=240 and x<=369 and y>=280 and y<=409:
                    p4+=1
                    if p4>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",240,180,white,240)
                        if a==0:
                            x5+=1
                        else:
                            o4+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=370 and x<=500 and y>=280 and y<=409:
                    p5+=1
                    if p5>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",370,180,white,240)
                        if a==0:
                            x6+=1
                        else:
                            o5+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=110 and x<=239 and y>=410 and y<=540:
                    p6+=1
                    if p6>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",110,310,white,240)
                        if a==0:
                            x7+=1
                        else:
                            o6+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=240 and x<=369 and y>=410 and y<=540:
                    p7+=1
                    if p7>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",240,310,white,240)
                        if a==0:
                            x8+=1
                        else:
                            o7+=1
                        a+=1
                        if a==2:
                            a=0
                if x>=370 and x<=500 and y>=410 and y<=540:
                    p8+=1
                    if p8>=2:
                        continue
                    else:
                        show_text(f"{l[a]}",370,310,white,240)
                        if a==0:
                            x9+=1
                        else:
                            o8+=1
                        a+=1
                        if a==2:
                            a=0
    if x1==1 and x2==1 and x3==1 or x4==1 and x5==1 and x6==1 or x7==1 and x8==1 and x9==1 or x1==1 and x4==1 and x7==1 or x2==1 and x5==1 and x8==1 or x3==1 and x6==1 and x9==1 or x1==1 and x5==1 and x9==1 or x3==1 and x5==1 and x7==1:
        show_text(' X Wins',240,300,red,32)
        pygame.display.update()
        time.sleep(5)
        break
    if o==1 and o1==1 and o2==1 or o3==1 and o4==1 and o5==1 or o6==1 and o7==1 and o8==1 or o==1 and o3==1 and o6==1 or o1==1 and o4==1 and o7==1 or o2==1 and o5==1 and o8==1 or o==1 and o4==1 and o8==1 or o2==1 and o4==1 and o6==1:
        show_text(' O Wins',240,300,red,32)                  
        pygame.display.update()
        break
    if x1+x2+x3+x4+x5+x6+x7+x8+x9+o+o1+o2+o3+o4+o5+o6+o7+o8==9:
        show_text(' TIE  ',240,300,red,32)
        pygame.display.update()
        break
