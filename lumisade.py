import pygame
import random


def alusta():
    """ Alustaa pygame ikkunan ja palauttaa näyttöolion """
    pygame.init()
    naytto = pygame.display.set_mode((1280, 700))
    return naytto


naytto = alusta()


lumi1 = pygame.image.load("lumihiutale1.png")
lumi2 = pygame.image.load("lumihiutale2.png")
lumi3 = pygame.image.load("lumihiutale3.png")
x_sijainti = 0
y_sijainti = 0
hiutaleet1 = ()
hiutaleet2 = ()
hiutaleet3 = ()
hiutale_maara = 0


def hiutale1():
    global hiutaleet1
    hiutaleet1 +=(random.randint(0,1280),)
    hiutaleet1 +=(-200,)
def hiutale2():
    global hiutaleet2
    hiutaleet2+=(random.randint(0,1280),)
    hiutaleet2+=(-200,)
def hiutale3():
    global hiutaleet3
    hiutaleet3+=(random.randint(0,1280),)
    hiutaleet3+=(-200,)
   
ajastin = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
    naytto.fill((0,0,0))
    if hiutale_maara < 30:
        ind=random.randint(0,100)
        if ind == 1:
            hiutale1()
            hiutale_maara +=1
        elif ind == 2:
            hiutale2()
            hiutale_maara +=1
        elif ind == 3:
            hiutale3()
            hiutale_maara +=1
       
    i=0
    while i < len(hiutaleet1)-1:
        naytto.blit(lumi1, (hiutaleet1[i],hiutaleet1[i+1]))
        lista=list(hiutaleet1)
        lista[i+1]+=1
        if lista[i+1] > 800:
            hiutale_maara-=1
        hiutaleet1=tuple(lista)
        i+=2
    i=0
    while i < len(hiutaleet2)-1:
        naytto.blit(lumi2, (hiutaleet2[i],hiutaleet2[i+1]))
        lista=list(hiutaleet2)
        lista[i+1]+=2
        if lista[i+1] > 700:
            hiutale_maara-=1
        hiutaleet2=tuple(lista)
        i+=2
    i=0
    while i < len(hiutaleet3)-1:
        naytto.blit(lumi3, (hiutaleet3[i],hiutaleet3[i+1]))
        lista=list(hiutaleet3)
        lista[i+1]+=3
        if lista[i+1] > 800:
            hiutale_maara-=1
        hiutaleet3=tuple(lista)
        i+=2
    pygame.display.flip()
    ajastin.tick(250)
