import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,155,0)

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width,display_height))

    


pygame.display.set_caption('LASA')
icon=pygame.image.load('apple.png')
pygame.display.set_icon(icon)

img=pygame.image.load('snakehead2.png')
appleimg=pygame.image.load('apple.png')

clock = pygame.time.Clock()
AppleThickness = 30

block_size=20
FPS=15

direction="right"

smallfont=pygame.font.SysFont("comicsansms",25)
medfont=pygame.font.SysFont("comicsansms",50)
largefont=pygame.font.SysFont("comicsansms",80)


def pause():
      paused = True
      while paused :
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  pygame.quit()
                  quit()
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_c:
                      paused = False

                  elif event.key == pygame.K_q:
                       pygame.quit()
                       quit()

          gameDisplay.fill(white)  
          message_to_screen("paused",black,-100,size="large") 

          message_to_screen("press C to continue or Q to quit .",black,25)
                              
          pygame.display.update()
          clock.tick(5)

def score(score):
    text = smallfont.render("score: "+str(score),True , black)
    gameDisplay.blit(text,[0,0])

def randApppleGen():
    randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0 

    return randAppleX,randAppleY

randAppleX,randAppleY = randAppleGen()
def game_intro():

    intro = True
    while intro:


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                 pygame.quit()
                 quit()

            if event.tyoe == pygame.KEYDOWN:
                if event.key== pygame.k_c:
                    intro = False

                if event.Key==pygame.k_q:
                     pygame.quit()
                     quit()
                              
                              
        gameDisplay.fill(white)
        message_to_screen("welcome to lasa ",
                           green,
                           -100,
                           "large")

        message_to_screen("the objective of the game is to eat red apple",
                           black,
                           -30)
                              
        message_to_screen("the more apple you eat, the longer you get",
                           black,
                           10)

        message_to_screen("if you run into yourself , or the edges you die !",
                           black,
                           50)

        message_to_screen("press c to play , p to pause or q to quit ",
                           black,
                           180)

        pygame.display.update ()
        clock.tick(15)
                              
def snake(block_size,snakeList):

    if direction =="right":
        head=pygame.transform.rotate(img,270)

    if direction =="left":
        head=pygame.transform.rotate(img,90)

    if direction =="up":
        head=img


    if direction =="down":
        head=pygame.transform.rotate(img,180)
        
    gameDisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
      pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size =="small":
       textSurface = smallfont.render(text,True,color)
    elif size =="medium":
       textSurface = medfont.render(text,True,color)
    elif size =="large":
       textSurface = largefont.render(text,True,color)

                              
    return textSurface,textSurface.get_rect()
    

      
    
def message_to_screen(msg,color,y_displace=0):
    textSurf,textRect = text_objects(msg,color,size)
    #screen_text=font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textRect.center =(display_width/2),(display_height/2)+y_displace
    gameDisplay.blit(textSurf,textRect)

def gameloop():
    global direction 
    gameExit=False
    gameover=False
    
lead_x = display_width/2
lead_y = display_height/2

lead_x_change=10
lead_y_change=0

snakeList = []
snakeLength = 1

randAppleX,randAppleY = randAppleGen()

  
while not gameExit:
    
    while gameover == True:
        gameDisplay.fill(white)
        message_to_screen("game over", red,y_displace=-50,size="large")
        message_to_screen("gameover, press c to play again or Q to quit ",black,50,size="medium")
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                 gameOver = False    
                 gameExit = True
                 
            if event.type==pygame.KEYDOWN:
               if event.key==pygame.K_q :
                  gameExit = True
                  gameOver = False
               if event.key == pygame.K_c :
                  gameLoop()
                     
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    direction ="left"
                    lead_X_change=-block_size
                    lead_y_change=0

                elif event.Key==pygame.K_Right:
                    direction ="right"
                    lead_X_change=block_size
                    lead_y_change=0

                elif event.key== pygame.K_UP:
                    direction ="up"
                    lead_y_change=-block_size
                    lead_x_change=0

                elif event.key == pygame.K_DOWN:
                    direction ="down"
                    lead_y_change=block_size
                    lead_x_change=0

                elif event.key  == pygame.K_p:
                    pause()

                if lead_x>=display_width or lead_x<0 or lead_y >=display_height  or lead_y <0:

                   gameOver=True


lead_x+=lead_x_change
lead_y+=lead_y_change

gameDisplay.Fill(white)
                            
#pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])

gameDisplay.blit(appleimg, (randAppleX , randAppleY ))
                 
snakeHead=[]
snakeHead.append(lead_x)
snakeHead.append(lead_y)
snakeList.append(snakeHead)

if len(snakeList) > snakeLength :
    del snakeList[0]

for eachSegment in snakeList[:-1] :
    if eachSegment == snakeHead:
         gameOver = True  
                                  
snake(block_size,snakeList)
                                  
snake(block_size,snakeList)
                            
score(snakelength-1)
pygame.display.update()

                      ##  if lead_x == randAppleX and lead_y == randAppleY:
                      ##            randAppleX=round(random.randrange(0,display_width-block_size)/10.0)*10.0
                      ##            randAppleY=round(random.randrange(0,display_height-block_size)/10.0)*10.0
                      ##            snakeLength +=1
                      ##           clock.tick(FPS)

 ## if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
 ##if lead_y>= randAppleY and lead_Y<= randAppleY + AppleThickness:
  ##  randAppleX=round(random.randrange(0,display_width-block_size))#/10.0)*10.0
  ##  randAppleY=round(random.randrange(0,display_height-block_size))#/10.0)*10.0
 ##   snakeLength +=1

if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness :
       
         if lead_Y > randAppleY and lead_Y < randAppleY + AppleThickness:
           
           randAppleX,randAppleY = randAppleGen()
           snakeLength +=1 
         elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
           
           randAppleX=round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
           randAppleY=round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0
           snakeLength +=1
           
clock.tick(FPS)

                    

pygame.quit()
quit()

game_intro()
gameLoop()
                                  
                    
                    
                    



    
        

