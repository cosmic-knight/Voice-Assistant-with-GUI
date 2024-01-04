import pygame,db
import math,os
from tkinter import *

width=800
height=400  #10.6cm(0.0265cm=1px)
window=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")

def Button(cursor, pos, width, height, text):
    buttonPos=pygame.Rect(pos, (width,height))
    if buttonPos.collidepoint(cursor):
        if text=="yes":
            db.clearer()
            os.system('cmd /c taskkill /F /IM gui.exe')
            os.system('cmd /c taskkill /F /IM python3.11.exe')
            pygame.quit()
            quit()
        elif text=="no":
            os.system('cmd /c taskkill /F /IM gui.exe')
            os.system('cmd /c taskkill /F /IM python3.11.exe')
            pygame.quit()
            quit()

def screen(ui,screen,spage=5):
    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(width / bg.get_width()) + 1
    
    screenImage=pygame.image.load(f"{ui}//{screen}.jpg")
    window.blit(screenImage, (12,10))

    exit_game=False
    fps=60
    while not exit_game:
        i = 0
        if spage==5:
            while(i < tiles):
                window.blit(bg, (bg.get_width()*i- scroll, 0))
                i += 1
                scroll += 1
        else:
            window.blit(bg, (0, 0))
    
        if abs(scroll) > bg.get_width():
            scroll = 0

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                os.system('cmd /c taskkill /F /IM gui.exe')
                os.system('cmd /c taskkill /F /IM python3.11.exe')
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button?
                    Button(event.pos, (61,235),183,50,"yes")
                    Button(event.pos, (552,235),183,50,"no")

        window.blit(screenImage, (12,10))
        
        pygame.display.update()
        clock.tick(fps)
    quit()