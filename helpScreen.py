import pygame,keyInput
import math,os,voiceInput

width=800
height=400  #10.6cm(0.0265cm=1px)
window=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
pygame.display.set_caption("Assistant v1.11.03")

def Button(cursor, pos, width, height, text, screen,ui, draw=1,spage=5,txtsize=20,voice=1):
    buttonPos=pygame.Rect(pos, (width,height))
    if draw==1:
        pygame.draw.rect(window,"#FFFFFF",buttonPos,border_radius=1)
    if buttonPos.collidepoint(cursor):
        if text=="close":
            if screen==1:
                keyInput.screen(ui,txtsize,voice,spage)
            if screen==2:
                voiceInput.screen(ui,txtsize,voice,spage)

def screen(screen,ui,txtsize=20,spage=5,voice=1):

    pygame.init()
    bg = pygame.image.load(f"{ui}//p.jpg")
    scroll = 0
    tiles = math.ceil(width / bg.get_width()) + 1
    white=(255,255,255)
    base_font=pygame.font.Font("AGENCYR.TTF", 20)
    
    screenImage=pygame.image.load(f"{ui}//p3.jpg")
    window.blit(screenImage, (12,10))
    ans=[]
    
    for i in com:
        ans.append(i)
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
                quit()
            
            elif event.type == pygame.KEYDOWN:
                if event.scancode==79:
                    ans=com[10:]
                elif event.scancode==80:
                    ans=com[0:]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button?
                    Button(event.pos, (739,25),26,27,"close",screen,ui,0,spage,txtsize,voice)

        window.blit(screenImage, (12,10))
        
        for i,j in enumerate(ans):	#can have upto 10
            if i<10:
                ans_surface=base_font.render(j,True,white)
                window.blit(ans_surface,(38,(70+(30*i))))
        pygame.display.update()
        clock.tick(fps)
    quit()
    #screen1=keys screen2=voice
com=["news/headlines: Today's headlines","open 'website_name': Opens specific website", "open 'file_name': Opens specific file", "search 'file_name': Returns path of file (first occurance)", "open 'app_name': Opens specific application", "search 'topic' on youtube: Searches specific topic on youtube", "google search 'topic': Searches specific topic on google", "generate an image of 'anything': Generates any image", "search an image of 'anyting': Searches for image of specific topic", "send 'file_name': generates qr code for file sharing", "close 'app_name': Closes specific application", "close all: Closes all applications", "'any calculation': Solves it", "close/quit/exit: Closes assistant", "shutdown: Turns off pc", "what is 'anything': Gives a short description"]