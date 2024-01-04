import pygame,historyScreen,keyInput
import math,os,settingScreen,pyttsx3
from tkinter import *
import projectPkg,closeScreen,db
import speech_recognition as sr

width=800
height=400  #10.6cm(0.0265cm=1px)
window=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)
engine.runAndWait()

def takeCommand():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            inText=r.recognize_google(audio)
        except Exception:
            inText=""
            return ("Please say again")
    
    if len(inText)>0:
        if len(history)>9:
            history.pop(9)
        history.insert(0,inText)
        db.dbPasser(inText)
        user_text=inText
        answer=projectPkg.takeCommand(inText)
        return answer

def Button(cursor, pos, width, height, text,ui, draw=1,voice=1,spage=5,txtsize=20):
    buttonPos=pygame.Rect(pos, (width,height))
    if draw==1:
        pygame.draw.rect(window,"#FFFFFF",buttonPos,border_radius=20)
    if buttonPos.collidepoint(cursor):
        if text=="history":
            historyScreen.screen(2,ui,txtsize,spage,voice)
        elif text=="key":
            keyInput.screen(ui,txtsize,voice,spage)
        elif text=="close":
            closeScreen.screen(ui,"p7",spage)
        elif text=="settings":
            settingScreen.screen(2,ui,txtsize,voice,spage)

history=[]
h=0

def screen(ui,txtsize=20,voice=1,spage=5):
    answer=""
    
    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(width / bg.get_width()) + 1
    white=(255,255,255)
    base_font=pygame.font.Font("AGENCYR.TTF", txtsize)

    screenImage=pygame.image.load(f"{ui}//p1.jpg")
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
            
            if event.type==pygame.KEYDOWN:
                if event.unicode==" ":
                    answer=""
                    answer=takeCommand()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button?
                    Button(event.pos, (595,103),170,50,"history",ui,0,voice,spage,txtsize)
                    Button(event.pos, (595,171),170,50,"key",ui,0,voice,spage,txtsize)
                    Button(event.pos, (595,240),170,50,"close",ui,0,spage=spage)
                    Button(event.pos, (595,309),170,50,"settings",ui,0,voice,spage)

        window.blit(screenImage, (12,10))
        if len(history)>0:
            user_text=history[0] #can take upto 67characters
            text_surface=base_font.render(user_text,True,white)
            window.blit(text_surface,(40,30))

        for i,j in enumerate(answer):
            a=12*i
            b=520
            h=110
            ans_surface=base_font.render(j,True,white)
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
        pygame.display.update()
        clock.tick(fps)
    quit()