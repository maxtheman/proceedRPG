#startup pygame
import pygame
pygame.init()

#Define numbers, colors, ect.
gravity = 1
pi=3.141592653
black =[0,0,0]
white = [255,255,255]
blue = [0,0,255]
green = [0,255,0]
red = [255,0,0]
#det = 0

#size of screen
size=[400,400]

#class remembering which tiles are where
#class tileSheet():
    
    #def __init__(self,det,xList,yList):
        #fill pos lists, x and y respectively
       # while det <= size[0]:
         #   det += 1
         #   det*40
         #   xList.append(r)

       # while det <= size[1]:
        #    det += 1
        #    det*40
        #    r*40
        #    xList.append(r)
    #xList = []
    #yList = []

#tileSheet(det,xList,yList)
#print(tileSheet.xList)
#print(tileSheet.yList)

#player attributes
playerSpeedX = 0
playerSpeedY = 0
playerPosX = 160
playerPosY = 200

#List Defining Ground
groundList = []

#Define images
player_image = pygame.image.load("player_image.png")
grass_image = pygame.image.load("grass_image.png")
sky_image = pygame.image.load("sky_image.png")
player_image.set_colorkey(white)

#functions
#tile spawner
def tileSpawn(image,x,y):
    screen.blit(image,[x,y])
    


#open a screen
screen=pygame.display.set_mode(size)
pygame.display.set_caption("proceedRPG")

#loop until user closes program
done = False

#create a timer for screen updating
clock = pygame.time.Clock()


#--------------------Main Program Loop-------------------------------
while done == False:
    #keep ref. rate at 10 fps
    clock.tick(50)

    for event in pygame.event.get():#user did something
        if event.type == pygame.QUIT: #If user clicked close
            done=True #Flags that we can end loop
        
        #player controls
        #pressing down a key
        if event.type == pygame.KEYDOWN:
            #Key movement
            if event.key == pygame.K_LEFT:
                playerSpeedX = -3
            if event.key == pygame.K_RIGHT:
                playerSpeedX = 3
            if event.key == pygame.K_UP:
                playerSpeedY = -10 
            #debug--print player pos
            if event.key == pygame.K_q:
                print([playerPosX,playerPosY])
                      
        #release said key
        if event.type == pygame.KEYUP:
            #unkey movement
            if event.key == pygame.K_LEFT:
                playerSpeedX = 0
            if event.key == pygame.K_RIGHT:
                playerSpeedX = 0
            if event.key == pygame.K_UP:
                playerSpeedY = 0    
    #All drawing code happens after the for loop and inside the
    #main while done==False loop
                
    #clear screen and set BG
    screen.fill(white)

    #Generate Sky
    for s in range(10):
        #line by line
        for i in range(10):
            x = i*40
            y = s*40
            tileSpawn(sky_image,x,y)

    #Generate Ground, put in groundList
    for i in range(10):
        x = i*40
        y = 360
        blitPos = [x,y]
        groundList.append(blitPos)
        tileSpawn(grass_image,x,y)

    #draw the player    
    screen.blit(player_image,[playerPosX,playerPosY])

    #move the player
    playerPosX += playerSpeedX
    playerPosY += playerSpeedY

    #gravity
    playerSpeedY += gravity
  
    #player ground detection
    if playerPosY == 320:
        playerSpeedY = 0
    elif playerPosY > 320:
        playerPosY = 320



    #update screen
    pygame.display.flip()



#be IDLE friendly
pygame.quit ()
