from pygame import *

display.set_caption('???🤷‍♀️🤦‍♂️🤷‍♂️🤷‍♀️🤷‍♂️🤷‍♂️')
linox=display.set_mode((700,500))
bg=transform.scale(image.load('background.png'),(700,500))
#создай окно игры
class Chvk():
    def __init__(self,png,x,y,width,heigth,hp):
        self.rect=Rect(x, y, width, heigth)
        self.png=transform.scale(image.load(png),(100,100))
        self.hp=hp
    def drawd(self):
        linox.blit(self.png,(self.rect.x,self.rect.y))
pl=Chvk('sprite1.png',100,400,100,100,1)
pl2=Chvk('sprite2.png',400,400,100,100,1)
run=True
clock=time.Clock()
FPS=60
key_p=key.get_pressed()
while run:
    display.update()
    key_p=key.get_pressed()
    linox.blit(bg,(0,0))
    pl.drawd()
    pl2.drawd()
    for e in event.get():
        if e.type==QUIT:
            run=False
            quit()
    if key_p[K_w]and pl.rect.y>0:
        pl.rect.y-=5
    if key_p[K_a]and pl.rect.x>0:
        pl.rect.x-=5
    if key_p[K_s]and pl.rect.y+100<500:
        pl.rect.y+=5
    if key_p[K_d]and pl.rect.x+100<700:
        pl.rect.x+=5
    if key_p[K_LEFT]and pl2.rect.x>0:
        pl2.rect.x-=5
    if key_p[K_RIGHT]and pl2.rect.x+100<700:
        pl2.rect.x+=5
    if key_p[K_UP]and pl2.rect.y>0:
        pl2.rect.y-=5
    if key_p[K_DOWN]and pl2.rect.y+100<500:
        pl2.rect.y+=5
    clock.tick(FPS)