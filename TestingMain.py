import os.path
import random
import sys
from threading import Thread

import pygame

import CaesarTool
import IntroductionText
import Level1Cipher
import Level1Text
import Level2Cipher
import Level2Text
import Level3Cipher
import Level3Text
import Level4Cipher
import Level4Text
import MissionText
import MorseTool
import PolyCipherTool
import VignereTool


class Settings(object):
    menu = {"root":["Introduction","Briefing", "Activity Log","Frequency Configuration","Capture Sizing", "Credits", "Resign"],

            "Introduction":["Welcome Letter"],

            "Briefing":["Operation Briefing"],

            "Activity Log":["Below 60","Above 90"],

            "Frequency Configuration":["Reset Frequency", "Amplitude Adjustment", "Serial Config","Custom Frequency"],

            "Capture Sizing":[ "Change screen size"],
            "Change screen size":["640x400", "800x500", "1000x1000"],

            "Credits":["Zhiyuan Huang"],

            #"Enter":["Continue"],
            }
        
def destroy(self):
    # Destroy the window
    self.root.destroy()

class Menu(object):
    """ each menu item name must be unique"""
    def __init__(self, menu={"root":["Enter","Help","Quit"]}):
        self.menudict = menu
        self.menuname="root"
        self.oldnames = []
        self.oldnumbers = []
        self.items=self.menudict[self.menuname]
        self.active_itemnumber=0
    
    def nextitem(self):
        if self.active_itemnumber==len(self.items)-1:
            self.active_itemnumber=0
        else:
            self.active_itemnumber+=1
        return self.active_itemnumber
        
    def previousitem(self):
        if self.active_itemnumber==0:
            self.active_itemnumber=len(self.items)-1
        else:
            self.active_itemnumber-=1
        return self.active_itemnumber 
        
    def get_text(self):
        """ change into submenu?"""
        try:
            text = self.items[self.active_itemnumber]
        except:
           print("exception!")
           text = "root"
        if text in self.menudict:
            self.oldnames.append(self.menuname)
            self.oldnumbers.append(self.active_itemnumber)
            self.menuname = text
            self.items = self.menudict[text]
            # necessary to add "back to previous menu"?
            if self.menuname != "root":
                self.items.append("back")
            self.active_itemnumber = 0
            return None
        elif text == "back":
            #self.menuname = self.menuname_old[-1]
            #remove last item from old
            self.menuname =  self.oldnames.pop(-1)
            self.active_itemnumber= self.oldnumbers.pop(-1)
            print("back ergibt:", self.menuname)
            self.items = self.menudict[self.menuname]
            return None
            
        return self.items[self.active_itemnumber] 
        
        
        
            

class PygView(object):
    width = 640
    height = 400
    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
           default arguments 
        """
        
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        pygame.display.set_caption("Press ESC to quit")
        PygView.width = width
        PygView.height = height
        self.set_resolution()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)
        
    def set_resolution(self):
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((0,0,0)) # fill background white

    def paint(self):
        menu_distance = 50 # distance between title and menu
        title_center = (self.width // 2, 40)
        title_font = pygame.font.SysFont("mono", 43)
        title_text = title_font.render("PsycommuVer1", True, (255, 255, 255))
        title_rect = title_text.get_rect(center=title_center)
        self.screen.blit(title_text, title_rect)

        # calculate menu position
        menu_height = len(m.items) * 30 # assuming each menu item has height 30
        menu_top = title_center[1] + menu_distance
        menu_left = title_center[0] - (menu_height // 2)
        menu_center = (menu_left, menu_top)

        for i in m.items:
            n = m.items.index(i)
            if n == m.active_itemnumber:
                self.draw_text("[#]", menu_center[0] - 50, menu_center[1] + m.items.index(i)*30, (0,0,255))
                self.draw_text(i, menu_center[0], menu_center[1] + m.items.index(i)*30, (0,0,255))
            else:
                self.draw_text(i, menu_center[0], menu_center[1] + m.items.index(i)*30)

    def get_input(self):
        pygame.display.set_caption("Enter a string")
        input_box = pygame.Rect(100, 100, 140, 32)
        text = ''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return text
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            
            self.screen.fill((0, 0, 0))
            pygame.draw.rect(self.screen, (255, 255, 255), input_box, 2)
            font = pygame.font.Font(None, 32)
            input_text = font.render(text, True, (255, 255, 255))
            self.screen.blit(input_text, (input_box.x + 5, input_box.y + 5))
            pygame.display.flip()


    def run(self):
        """The mainloop
        """
        #self.paint()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key==pygame.K_DOWN or event.key == pygame.K_KP2:
                        m.nextitem()
                        print(m.active_itemnumber)
                    if event.key==pygame.K_UP or event.key == pygame.K_KP8:
                        m.previousitem()
                    if event.key==pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        result = m.get_text()
                        print(result)
                        if result is None:
                            break
                        elif "x" in result:
                            # change screen resolution, menu text is something like "800x600"
                            left = result.split("x")[0]
                            right = result.split("x")[1]
                            if str(int(left))==left and str(int(right))== right:
                                PygView.width = int(left)
                                PygView.height = int(right)
                                self.set_resolution()
                        elif result == "Zhiyuan Huang":
                            text="Programmer of this game. "
                        

                            
                            
                            
                            #Level2Text.Level2Command()
                            #Scoreboard.ScoreboardCOmmand() 

                        elif result == "Welcome Letter":
                            IntroductionText.IntroductionTextCommand()
                        elif result == "Operation Briefing":
                            MissionText.MissionCommand()
                        elif result == "Below 60":
                            Level1Text.Level1Command()
                            Level1Cipher.TombCommand()
                        elif result == "Above 90":
                            Level2Text.Level2Command()
                            Level2Cipher.SystemCommand()
                        elif result == "Mission 3":
                            Level3Text.Level3Command()
                            Level3Cipher.TwoCommand()
                        elif result == "Mission 4":
                            Level4Text.Level4Command()
                            Level4Cipher.SignalCommand()

                        elif result =="Serial Cipher":
                            PolyCipherTool.PolyCipherCommand()
                        elif result == "Morse Code":
                            MorseTool.MorseCommand()
                        elif result == "Caesar Cipher":
                            CaesarTool.CaesarCommand()
                        elif result == "Vignere Cipher":
                            VignereTool.VignereCommand()




                        elif result=="Resign":
                            print("Goodbye")
                            pygame.quit()
                            sys.exit()
                                            

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: {:6.3}".format(
                            self.clock.get_fps()), color=(30, 120 ,18))
            #pygame.draw.line(self.screen,(random.randint(0,255),random.randint(0,255), random.randint(0,255)),(50,self.height - 80),(self.width -50,self.height - 80) ,3)             
            self.paint()
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            
        pygame.quit()


    def draw_text(self, text ,x=50 , y=0,color=(27,135,177)):
        if y==0:
            y= self.height - 50
        
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, color)
        self.screen.blit(surface, (x,y))

    
####

if __name__ == '__main__':

    # call with width of window and fps
    m=Menu(Settings.menu)
    PygView().run()
