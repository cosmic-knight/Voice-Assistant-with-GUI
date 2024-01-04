import pygame,keyInput
import math,os,voiceInput

window=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")

def Button(cursor, pos0, pos1, width, height, text, nxt, ui, txtsize=20,voice=1,spage=5):
    buttonPos=pygame.Rect((pos0,pos1), (width,height))
    if buttonPos.collidepoint(cursor):
        if text=="v1":
            if voice==1:
                screen(nxt,ui,txtsize,0,spage)
            else:
                screen(nxt,ui,txtsize,1,spage)
        elif text=="v2":
            if voice==0:
                screen(nxt,ui,txtsize,1,spage)
            else:
                screen(nxt,ui,txtsize,0,spage)
        elif text=="f1":
            if txtsize>19:
                screen(nxt,ui,txtsize-1,voice,spage)
        elif text=="f2":
            if txtsize<29:
                screen(nxt,ui,txtsize+1,voice,spage)
        elif text=="u1":
            if ui>1:
                screen(nxt,ui-1,txtsize,voice,spage)
            else:
                screen(nxt,5,txtsize,voice,spage)
        elif text=="u2":
            if ui<5:
                screen(nxt,ui+1,txtsize,voice,spage)
            else:
                screen(nxt,1,txtsize,voice,spage)
        elif text=="b1":
            if spage==5:
                screen(nxt,ui,txtsize,voice,spage=6)

            elif spage==6:
                screen(nxt,ui,txtsize,voice,spage=5)
        elif text=="save":
            if nxt==1:
                keyInput.screen(ui,txtsize,voice,spage)
            if nxt==2:
                voiceInput.screen(ui,txtsize,voice,spage)

def screen(nxt,ui,txtsize=20,voice=1,spage=5):
    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(800 / bg.get_width()) + 1
    screenImage=pygame.image.load(f"{ui}//p{spage}.jpg")
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
        window.blit(screenImage, (12,10))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                os.system('cmd /c taskkill /F /IM gui.exe')
                os.system('cmd /c taskkill /F /IM python3.11.exe')
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button?
                    Button(event.pos, 50,40,35,35,"v1",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 707,40,35,35,"v2",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 50,110,35,35,"f1",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 707,110,35,35,"f2",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 50,188,35,35,"u1",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 707,188,35,35,"u2",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 707,258,35,35,"b1",nxt,ui,txtsize,voice,spage)
                    Button(event.pos, 305,320,190,45,"save",nxt,ui,txtsize,voice,spage)
        
        pygame.display.update()
        clock.tick(fps)
    quit()