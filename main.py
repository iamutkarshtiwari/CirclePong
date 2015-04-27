#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Circle Pong Challenge
# Copyright (C) 2015  Utkarsh Tiwari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Utkarsh Tiwari    iamutkarshtiwari@gmail.com



import os
import gtk
import pickle
import pygame
import sys
import math






class game:
    
    def make(self):
        
        
        
        pygame.init()
        sound=True
        
        try:
            pygame.mixer.init()
        except Exception, err:
            sound=False
            print 'error with sound', err
            
        black=(0,0,0)
        white=(255,255,255)
        clock=pygame.time.Clock()
        timer=pygame.time.Clock()
            
        crashed=False   
        disp_width = 600
        disp_height = 600
            
        press=0    
        
        info=pygame.display.Info()
        gameDisplay=pygame.display.get_surface()
        
        
        if not(gameDisplay):
            
            gameDisplay = pygame.display.set_mode((info.current_w,info.current_h))
            
            pygame.display.set_caption("Make Them Fall")
            #gameicon=pygame.image.load('data/images/icon.png')
            #pygame.display.set_icon(gameicon)
            
            
        angle=0                                                        # Loading assets
        ball=pygame.image.load("data/images/ball.png")
        ball=pygame.transform.scale(ball,(10,10))
        
        pygame.draw.circle(gameDisplay,white,(100,100),10,0)
        
        
        pad2=pad=pygame.image.load("data/images/ball.png")           # pad transform
        pad2=pad=pygame.transform.scale(pad,(120,20))
        pad=pygame.transform.rotate(pad,angle)
        
        
        
        color=(255,255,255)
        
        
        font_path = "fonts/arial.ttf"
        font_size = 18
        font1= pygame.font.Font(font_path, font_size)
        font1.set_bold(True)
        i=0
        j=0
        
        xcolor=0
        ycolor=210
        zcolor=0
        
        xcf=ycf=zcf=0
        f1=f2=0
        
        xrightflag=-1
        upperhalf=False
        xcor=625
        ycor=384
        
        padangle=0
        
        while not crashed:
        #Gtk events
            
            while gtk.events_pending():
                gtk.main_iteration()
            event=pygame.event.poll()
            #totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                crashed=True
                
            
            mos_x,mos_y=pygame.mouse.get_pos() 
            
            #print event
            
                
            gameDisplay.fill(black)
            
            #print(event)
            
                                            ## Color control begins ##
            if(xcf==0):
                xcolor+=2
            else:
                xcolor-=3
            
            if(ycf==0):
                ycolor-=1
            else:
                ycolor+=3
                
            if(zcf==0):    
                zcolor+=2
            else:
                zcolor-=1
            
            if(xcolor>=240):
                xcf=1
            if(xcolor<=25):
                xcf=0    
                
                
            if(ycolor<=25):
                ycf=1
            if(ycolor>=240):
                ycf=0    
                
                
            if(zcolor>=240):
                zcf=1
            if(zcolor<=25):
                zcf=0
            
            
            
            
            
            
            
            color=(xcolor,ycolor,zcolor)
                
            pygame.draw.rect(gameDisplay, color,(40,40,100,20), 0) 
            #pygame.draw.circle(gameDisplay,white,(683,384),180,0)
            pygame.draw.circle(gameDisplay,color,(683,384),180,0)                           # Center big circle control
            
            pygame.draw.circle(gameDisplay,white,(683,384),5,0)
            
            
            newxcor=xcor
            
            if(xcor<683):
                newxcor=683+(683-xcor)
            
           
            if(upperhalf==True):
                ycor=384+(int)(math.sqrt(abs((180**2)-(newxcor-683)**2)))
                
            if(upperhalf==False):
                ycor=384-(int)(math.sqrt(abs((180**2)-(newxcor-683)**2)))
            
            
            
            #ycor=(int)(math.sqrt(abs((180**2)-(xcor**2))))
            #print ycor
            #print (math.sqrt(abs((180**2)-(xcor**2))))
            
            
            #pad=pygame.transform.rotate(pad2, angle)
            
            #print (int)(math.sqrt(abs((180**2)-(newxcor-683)**2)))
            gameDisplay.blit(ball,(683,ycor))
            gameDisplay.blit(ball,(xcor,384))
            print xcor
            
            '''
            if(angle>=359 and f1==1):
                angle=0
                
            if(angle<=1 and f2==1):gg
                angle=360
                
            if(angle>=(-1) and f1==1):
                angle=-360
                
            if(angle<=(-359) and f2==1):
                angle=-1
            '''
            
            '''
            if event.type==pygame.KEYDOWN and event.key==275 and f1==0:
                
                f1=1
                
                xrightflag=1
                
            if event.type==pygame.KEYDOWN and event.key==276 and f2==0:
                
                f2=1
                
                xrightflag=0
                
                      #start moving
            '''          
                      
                      
            if(xcor>=863 and xrightflag!=-1 ):
                #xrightflag=0
                upperhalf=not(upperhalf)
                
            
                
                
            if(xcor<=503 and xrightflag!=-1 ):
                #xrightflag=1
                upperhalf=not(upperhalf)
                
            
                
                
            if(upperhalf==False):               # Down Case
                if(xrightflag==1):
                    xcor+=1
                if(xrightflag==0):
                    xcor-=1
            if(upperhalf==True):               # Upper Case
                if(xrightflag==1):
                    xcor-=1
                if(xrightflag==0):
                    xcor+=1
                
                
            '''    
           
            if(f1==1 and f2==0):
                angle+=1
            
            if(f2==1 and f1==0):
                angle-=1
            '''
                  
                
            '''    
            if event.type==pygame.KEYUP and event.key==276 and f1==1:
                
                f1=0
                xrightflag=-1
                
                
            if event.type==pygame.KEYUP and event.key==275 and f2==1:
                
                f2=0
                xrightflag=-1
            '''
            
            
            press=pygame.key.get_pressed()
            
            #print press
            if(press[len(press)-47]):               #left key press check
                #print "left" 
                xrightflag=0
                f1=1
                f2=0
            
             
             
            if(press[len(press)-48]):               #right key press check
                #print "right"  
                xrightflag=1
                f1=0
                f2=1
            
                
                
            if(press[len(press)-47]==0 and press[len(press)-48]==0 ):
                
                xrightflag=-1
             
            
            
            #gameDisplay.blit(circle)
            #gameDisplay.blit(background,(350,0))
            
            
            '''
            
            if pane2.get_rect(center=(390+80+120,150+50)).collidepoint(mos_x,mos_y):            # 2 pane game
                gameDisplay.blit(pygame.transform.scale(pane2,(420,90)),(385,150))
                if(pygame.mouse.get_pressed())[0]==1 and press==0:
                    #print 'yes'
                    press=1
                    while f==1:
                        
                        a=pane2window()
                        a=a.run(gameDisplay,info)
                    
                        f=scorewindow()
                        f=f.run(gameDisplay,a,1)
                        
                        
                        
                     
                        
                    
                
                
                
            else:
                gameDisplay.blit(pane6,(390,350))  # 6pane
                
            
            
            
            
            gameDisplay.blit(maxnormal,(540,200))
            gameDisplay.blit(maxnightmare,(410,300))
            gameDisplay.blit(maxfear,(560,300))
            gameDisplay.blit(maxinferno,(700,300))
            gameDisplay.blit(maximpossible,(560,410))
            gameDisplay.blit(maxcardiac,(560,510))
            
            
            
            
            if os.path.getsize("score.pkl") >0:
            
                with open('score.pkl', 'rb') as input:    #REading
                    maxscore = pickle.load(input)
            
            maxnormal=maxscore[0]
            maxnightmare=maxscore[1]
            maxfear=maxscore[2]
            maxinferno=maxscore[3]
            maximpossible=maxscore[4]
            maxcardiac=maxscore[5]
            
                
            '''   
            
            
            
            f=1
            #press=0
            pygame.display.update()
            clock.tick(120)
     
            if crashed==True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()
     
     
     
     
        # Just a window exception check condition

        event1=pygame.event.get()                                 
        if event1.type == pygame.QUIT:
            crashed=True
   
        if crashed==True:
            pygame.quit()
            sys.exit()
            

if __name__ == "__main__":
    g = game()
    g.make()         
