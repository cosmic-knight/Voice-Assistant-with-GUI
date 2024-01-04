import pygame,historyScreen,voiceInput,helpScreen
import math,os,settingScreen,db,closeScreen
from tkinter import *
import projectPkg

width=800
height=400  #10.6cm(0.0265cm=1px)
window=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")
icon=pygame.image.load("icon.ico")
pygame.display.set_icon(icon)

curpath=os.getcwd()

def likho(answer,base_font,point):
    z=0
    for i,j in enumerate(answer):
        if i>point:
            a=12*z
            b=520
            h=110
            ans_surface=base_font.render(j,True,"white")
            if a<b:
                window.blit(ans_surface,(40+((a)%(b)),h))
            elif a<(b*2):
                window.blit(ans_surface,(40+((a)%(b)),h+30))
            elif a<(b*3):
                window.blit(ans_surface,(40+((a)%(b)),h+60))
            elif a<(b*4):
                window.blit(ans_surface,(40+((a)%(b)),h+90))
            elif a<(b*5):
                window.blit(ans_surface,(40+((a)%(b)),h+120))
            elif a<(b*6):
                window.blit(ans_surface,(40+((a)%(b)),h+150))
            elif a<(b*7):
                window.blit(ans_surface,(40+((a)%(b)),h+180))
            elif a<(b*8):
                window.blit(ans_surface,(40+((a)%(b)),h+210))
            z+=1
    pygame.display.update()

def Button(cursor, pos, width, height, text,ui, draw=1,voice=1,spage=5,txtsize=20):
    buttonPos=pygame.Rect(pos, (width,height))
    if draw==1:
        pygame.draw.rect(window,"#FFFFFF",buttonPos,border_radius=20)
    if buttonPos.collidepoint(cursor):
        if text=="history":
            historyScreen.screen(1,ui,txtsize,spage,voice)
        elif text=="voice":
            voiceInput.screen(ui,txtsize,voice,spage)
        elif text=="close":
            closeScreen.screen(ui,"p8",spage)
        elif text=="settings":
            settingScreen.screen(1,ui,txtsize,voice,spage)

history=[]
h=0
def screen(ui,txtsize=20,voice=1,spage=5):
    pointer=-1
    user_text=""    #can take upto 67characters
    answer=""
    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(width / bg.get_width()) + 1
    white=(255,255,255)
    base_font=pygame.font.Font("AGENCYR.TTF", txtsize)
    chars=[" ","'","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!",",","@","#","$","%","^","&","*","(",")","_","+","=","-","{","}","|",":","<",">","?","/",".",",",";","]","[","]"]
    
    screenImage=pygame.image.load(f"{ui}//p2.jpg")
    window.blit(screenImage, (12,10))

    exit_game=False 
    fps=60
    while not exit_game:
        
        window.blit(screenImage, (12,10))
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
        
        window.blit(screenImage, (12,10))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                os.system('cmd /c taskkill /F /IM gui.exe')
                os.system('cmd /c taskkill /F /IM python3.11.exe')
                
            if event.type==pygame.KEYDOWN:
                os.chdir(curpath)
                if event.unicode=="\x08":
                    user_text=user_text[:-1]
                elif event.unicode=="\x7f":
                    user_text=""
                elif event.unicode in chars:
                    user_text+=event.unicode
                elif event.scancode==82:
                    user_text=history[-1]
                elif event.scancode==81:
                    user_text=""
                elif event.unicode=="\r":
                    try:
                        db.dbPasser(user_text)
                        if len(history)>9:
                            history.pop(0)
                        history.append(user_text)
                        if user_text=="help":
                            helpScreen.screen(1,ui,txtsize,spage,voice)
                        answer=projectPkg.takeCommand(user_text,voice)
                        user_text=""
                        pointer=-1
                    except Exception:
                        answer=""
                        user_text=""
                elif event.scancode==79:
                    if pointer<347:
                        pointer+=347
                elif event.scancode==80:
                    if pointer>345:
                        pointer-=347
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                os.chdir(curpath)
                if event.button == 1:  # left mouse button?
                    Button(event.pos, (595,103),170,50,"history",ui,0,voice,spage,txtsize)
                    Button(event.pos, (595,171),170,50,"voice",ui,0,voice,spage,txtsize)
                    Button(event.pos, (595,240),170,50,"close",ui,0,spage=spage)
                    Button(event.pos, (595,309),170,50,"settings",ui,0,voice,spage)

        text_surface=base_font.render(user_text,True,white)
        window.blit(text_surface,(40,30))
        likho(answer,base_font,pointer)
        pygame.display.update()
        clock.tick(fps)
    quit()