import pygame
import time
import random

pygame.init()

#Setting up the game window
display_width = 800
display_height = 600

#Defining colors with RGB
black = (0,0,0)
white = (255,255,255)
red = (220,0,0)
green = (0,207,0)
lime = (0,255,0)
blue = (0,0,255)
darker_blue = (0,0,207)
yellow = (255,255,0)
purple = (128,0,128)
lighter_purple = (150,0,150)

#Defining text format
smallText = pygame.font.SysFont("bahaus93",20)
mediumText = pygame.font.SysFont("bauhaus93",30)
largeText = pygame.font.SysFont("bauhaus93",60)
block_color = (25,175,235)

#Defining size of the Ship and the enemy ship
ship_width = 58
dodgedObj_width = 100
dodgedObj_height = 61

#Further developing the game window
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Star Dodge')
clock = pygame.time.Clock() #Game clock

#Loading all the images of the various objects and the background into the game screen
shipImg = pygame.image.load('Spaceship.png')
dodgeObj = pygame.image.load('Dodged_object.png')
screenBack = pygame.image.load('spacebackground.png')

def things(thing_startx,thing_starty):
    gameDisplay.blit(dodgeObj,(thing_startx, thing_starty))

#Making a scoring system    
def things_dodged(count):
    font = smallText
    text = font.render("Dodged: " + str(count), True, yellow)
    gameDisplay.blit(text,(0,0))
 
def ship(x,y):
    gameDisplay.blit(shipImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, yellow)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface2 = font.render(text, True, red)
    return textSurface2, textSurface2.get_rect()

def message_display(text):
    TextSurf, TextRect = text_objects(text, mediumText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('Oh No! You Lost!')  

#Start screen buttons
def game_button(x,y,w,h,ia,act,msg,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,act,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()

                
    else:
        pygame.draw.rect(gameDisplay,ia,(x,y,w,h))

        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w/2)), (y + (h/2)))
        gameDisplay.blit(textSurf, textRect)


def quit_game():
    pygame.quit()
    quit()
#Part of pause screen/button
def unpause():
    global pause
    pause = True
#Part of pause screen/button   
def paused():

    gameDisplay.blit(screenBack, [0,0])
    TextSurf, TextRect = text_objects("|Paused|", largeText)
    TextRect.center = ((display_width/2),(display_height/3))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        game_button(210,350,150,50,darker_blue,blue,"Resume","unpause")
        game_button(437,350,150,50,purple,lighter_purple,"Quit",quit_game)
        

        pygame.display.update()
        clock.tick(15)
        
#Making and defining a start screen for the game    
def game_start():

    start = True 
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(screenBack, [0,0])
        TextSurf, TextRect = text_objects("SPACE DODGE!", largeText)
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf, TextRect)

        game_button(210,350,150,50,darker_blue,blue,"Start",game_loop)
        game_button(437,350,150,50,purple,lighter_purple,"Quit",quit_game)
        

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    #Ship position in screen
    x = (display_width * 0.45)
    y = (display_height * 0.89)

    #Game loops and logic
    change_x = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 2
    thing_width = 100
    thing_height = 61

    Score = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            #Movement in game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x += -5
                if event.key == pygame.K_RIGHT:
                    change_x += 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    change_x = 0
                
        x += change_x
        gameDisplay.blit(screenBack, [0,0])


        
        things(thing_startx,thing_starty)
        thing_starty += thing_speed
        ship(x,y)
        things_dodged(Score)

        if x > display_width - ship_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            Score += 1
            if Score % 10 == 0:
                thing_speed += 1

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + ship_width > thing_startx and x + ship_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        
        
        pygame.display.update()
        clock.tick(60)

game_start()
game_loop()
pygame.quit()
quit()
