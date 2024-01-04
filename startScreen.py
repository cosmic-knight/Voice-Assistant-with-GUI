import pygame,keyInput,projectPkg
import math,os,voiceInput

window=pygame.display.set_mode((800,400))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")
projectPkg.wishMe(1)
def Button(cursor, pos0, pos1, width, height, text,ui):
    buttonPos=pygame.Rect((pos0,pos1), (width,height))
    if buttonPos.collidepoint(cursor):
        if text=="key":
            keyInput.screen(ui)
        elif text=="voice":
            voiceInput.screen(ui)

def screen(ui,spage=5):
    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(800 / bg.get_width()) + 1
    screenImage=pygame.image.load(f"{ui}//p4.jpg")
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
                    Button(event.pos, 50,305,183,50,"key",ui)
                    Button(event.pos, 565,305,183,50,"voice",ui)
        
        pygame.display.update()
        clock.tick(fps)
    quit()