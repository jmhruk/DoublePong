#imports
import pygame
from pygame.locals import *
import sys
import random
from math import *
import time


CON = 0

pygame.init()
#variables
p1score = 0
p2score = 0
clock = pygame.time.Clock()
#display window related
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Double Pong")

#object related
paddle_width = 30
paddle_height = 120
#colour related
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
orange = (255,128,0)
green = (0, 255, 0)



#game objects
paddle1 = pygame.Rect(50,150, paddle_width, paddle_height)
paddle2 = pygame.Rect(window_width - 50 - paddle_width, 150, paddle_width, paddle_height)
paddle3 = pygame.Rect(595,50, paddle_height, paddle_width)
paddle4 = pygame.Rect(595, window_height - paddle_height, paddle_height, paddle_width)
ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)
ballxspeed = 1
ballyspeed = 1


while CON < 1:
    event = pygame.event.wait()
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            CON += 1
    
    window.fill(blue)
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render("Please Click Space to start the game!", True, green, blue)
    textRect = text.get_rect()
    textRect.center = (window_width / 2, window_height / 2)
    window.blit(text, textRect)
    text = font.render("Double Pong", True, orange, blue)
    textRect = text.get_rect()
    textRect.center = (window_width / 2, (window_height / 2) - 200)
    window.blit(text, textRect)
    font1 = pygame.font.Font('freesansbold.ttf', 25)
    text = font1.render("Made by JMHRUK", True, green, blue)
    textRect = text.get_rect()
    textRect.center = (window_width / 2, (window_height / 2) - 160)
    window.blit(text, textRect)
    
    pygame.display.update()
            
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    
    #user input keys (paddles)
    keys = pygame.key.get_pressed()
    #up/down
    if keys[K_w] and paddle1.y > 0:
        paddle1.y -= 5
    if keys[K_s] and paddle1.y < window_height - paddle_height:
        paddle1.y += 5
    if keys[K_UP] and paddle2.y > 0:
        paddle2.y -= 5 
    if keys[K_DOWN] and paddle2.y < window_height - paddle_height:
        paddle2.y += 5
    #left/right
    if keys[K_a] and paddle3.x > 0:
        paddle3.x -= 5
    if keys[K_d] and paddle3.x < window_width - paddle_height:
        paddle3.x += 5
    if keys[K_LEFT] and paddle4.x > 0:
        paddle4.x -= 5
    if keys[K_RIGHT] and paddle4.x < window_width - paddle_height:
        paddle4.x += 5
        
    #ball movement
    
    
    #handling collisions
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ballxspeed *= -1
        ballyspeed *= -1

        ball.x += ballxspeed
    elif ball.colliderect(paddle3) or  ball.colliderect(paddle4):
        ballyspeed *= -1

        ball.y += ballyspeed
    
    #ball movement
    ball.x += ballxspeed
    ball.y += ballyspeed
    #randomly choose bounce directions
    x1 = random.choice([-1,1])
    y1 = random.choice([-1,1])
    #print(str(x1))
    #print(str(y1))
    if ball.x < 10 or ball.y < 10:
        p2score += 1
        #center ball not accounting to size
        ballxspeed *= x1
        ball.x = 640
        ball.y = 360
    elif ball.x > 1280 or ball.y > 720:
        p1score += 1
        #center ball not accounting to size
        ballyspeed *= y1
        ball.x = 640
        ball.y = 360
    
    #print("x" + str(ballxspeed))
    #print("y" + str(ballyspeed))
    # testing purposes time.sleep(0.1)
    #screen rendering
    window.fill(blue)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('P1 Score: ' + str(p1score) + " P2 Score:" + str(p2score), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (window_width - 1000, window_height - 15)
    window.blit(text, textRect)
    pygame.draw.ellipse(window, black, ball)

    pygame.draw.rect(window, green, paddle1)
    pygame.draw.rect(window, white, paddle2)
    pygame.draw.rect(window, green, paddle3)
    pygame.draw.rect(window, white, paddle4)
    
    pygame.display.update()
    clock.tick(120)
    #print(str(p1score))
    #print(str(p2score))