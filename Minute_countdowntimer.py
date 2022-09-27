import pygame
import time
pygame.init()

window=pygame.display.set_mode((200,200))
pygame.display.set_caption("countdown timer")

base_font=pygame.font.SysFont('constantia',20)
num_font=pygame.font.SysFont('oswald',20)

totaltime=60
resumeclicked = False
flag = True
flag1=0

image=pygame.Rect(50,80,30,20)
color = (255,0,0)
class resumebutton():
    width=65
    height=30

    def __init__(self,x,y,text1,text2):
        self.x=x
        self.y=y
        self.text1=text1
        self.text2=text2

    def Draw(self):
        global resumeclicked 
        flag1=0

        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
  
        if resumeclicked ==False:
            pygame.draw.rect(window,color,button_rect)
            text_img = base_font.render(self.text1,True,(0,0,0))
            text_len = text_img.get_width()
            window.blit(text_img,(self.x+int(self.width/2)-int(text_len/2),self.y+5))
        else:
            pygame.draw.rect(window,(0,255,0),button_rect)
            text_img = base_font.render(self.text2,True,(0,0,0))
            text_len = text_img.get_width()
            window.blit(text_img,(self.x+int(self.width/2)-int(text_len/2),self.y+5))

    def draw(self):
        global resumeclicked
        pos=pygame.mouse.get_pos()

        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)

        if button_rect.collidepoint(pos):
            if resumeclicked==False:
                resumeclicked = True
            else:
                resumeclicked=False
            
class resetbutton():
    width=65
    height=30

    def __init__(self,x,y,text):
        self.x=x
        self.y=y
        self.text=text
    
    def draw(self):
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(window,(0,0,255),button_rect)
        text_img = base_font.render(self.text,True,(0,0,0))
        text_len = text_img.get_width()
        window.blit(text_img,(self.x+int(self.width/2)-int(text_len/2),self.y+5))

    def Draw(self):
        pos=pygame.mouse.get_pos()
        global resumeclicked
        global totaltime

        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        bit=0
        if button_rect.collidepoint(pos):
            totaltime=60
            resumeclicked=False
            bit=bit+1
        return bit
        
class stopbutton:
    width=65
    height=30
    def __init__(self,x,y,text):
        self.x=x
        self.y=y
        self.text=text
    def draw(self):
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(window,(0,0,255),button_rect)
        text_img = base_font.render(self.text,True,(0,0,0))
        text_len = text_img.get_width()
        window.blit(text_img,(self.x+int(self.width/2)-int(text_len/2),self.y+5))

    def Draw(self):
        pos=pygame.mouse.get_pos()
        button_rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if button_rect.collidepoint(pos):
            pygame.quit()
          
resume=resumebutton(117.5,35,'resume','pause')
reset=resetbutton(117.5,135,'reset')
stop=stopbutton(17.5,135,'stop')


while flag:
    window.fill((255,255,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False
            break
        if event.type==pygame.MOUSEBUTTONDOWN:
            stop.Draw()
            flag1=reset.Draw()
            if flag1==0:
                resume.draw()
    stop.draw()
    resume.Draw()
    reset.draw()
    if resumeclicked==True and totaltime>0:
        totaltime=totaltime-0.5
        time.sleep(0.5)
    if totaltime==0:
        resumeclicked=False
        resume.Draw()
    pygame.draw.rect(window,color,image)
    countdownsurface=num_font.render("{0}".format(totaltime), True, (10, 10, 10))
    text_len=countdownsurface.get_width()
    window.blit(countdownsurface,(image.x+int(image.width/2)-int(text_len/2),image.y+5))
    
    pygame.display.update()
pygame.quit()
