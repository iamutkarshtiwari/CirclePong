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
from pygame.sprite import Sprite






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
            
            pygame.display.set_caption("Circle Pong")
            
            
            
        angle=0                                                        # Loading assets
        ball=pygame.image.load("data/images/ball.png")
        ball=pygame.transform.scale(ball,(10,10))
        
        pygame.draw.circle(gameDisplay,white,(100,100),10,0)
        
        
        pad2=pad=pygame.image.load("data/images/backcircle.png")           # pad transform
        pad2=pad=pygame.transform.scale(pad,(375,379))
        pad=pygame.transform.rotate(pad,angle)
        pad_rect=pad.get_rect()
        pad_rect.center=(625,384)
        
        
        
        fakepad=pygame.image.load("data/images/pad.png")
        fakepad=pygame.transform.scale(fakepad,(130,24))
        fakepad_rect=fakepad.get_rect()
        fakepad_rect.center=(683,384)
        
        
        
        
        
        
        
        
        #image_rect = pad.get_rect(center=(625,384))
        
        
        
        
        
        
        
        
        color=(255,255,255)
        yellow=(255,255,0)
        
        
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
        x=683               #Fixed coordinates for for color changing circle
        y=384
        
        
        xcor=683
        ycor=564
        
        fakex=683   # Fixed coordinates for rotatiing disk
        fakey=384
        
        
        
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
                
            #pygame.draw.rect(gameDisplay, color,(40,40,100,20), 0) 
            #pygame.draw.circle(gameDisplay,white,(683,384),180,0)
            pygame.draw.circle(gameDisplay,color,(683,384),180,0)       # Big circle                           # Center big circle control
            
            pygame.draw.circle(gameDisplay,yellow,(xcor,ycor),5,0)  # Small dot
            
            
            newxcor=xcor
            
            
            if(upperhalf==True):
                ycor=384-(int)(math.sqrt(abs((180**2)-(newxcor-683)**2)))
                
            if(upperhalf==False):
                ycor=384+(int)(math.sqrt(abs((180**2)-(newxcor-683)**2)))
            
            
            
            
            
            # For original game padd rotation
            new_pad = pygame.transform.rotate(pad, angle)
            
            new_pad_rect = new_pad.get_rect()
            new_pad_rect.center=(fakex,fakey)
            
            # For fake pad rotation
            
            
            
            
            
            
            
            
            gameDisplay.blit(new_pad,new_pad_rect)
                   
                      
                      
            if(xcor>=863 and xrightflag!=-1 ):
                #xrightflag=0
                upperhalf=not(upperhalf)
                
            
                
                
            if(xcor<=503 and xrightflag!=-1 ):
                #xrightflag=1
                upperhalf=not(upperhalf)
                
            
                
                
            if(upperhalf==False):               # Down Case
                if(xrightflag==1):
                    xcor+=4
                    #if(xcor%2==0):
                    angle+=2
                if(xrightflag==0):
                    xcor-=4
                    #if(xcor%2==0):
                    angle-=2
            if(upperhalf==True):               # Upper Case
                if(xrightflag==1):
                    xcor-=4
                    #if(xcor%2==0):
                    angle+=2
                if(xrightflag==0):
                    xcor+=4
                    #if(xcor%2==0):
                    angle-=2
               
                
           
            
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
                
            if(press[len(press)-48] and press[len(press)-47]):
                f1=f2=0
            
                
                
            if(press[len(press)-47]==0 and press[len(press)-48]==0 ):
                
                xrightflag=-1
             
            
            
           
            
            f=1
            #press=0
            pygame.display.update()
            clock.tick(60)
     
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
