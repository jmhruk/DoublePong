#imports
import pygame
from pygame.locals import *
import sys
import random

pygame.init()
#variables
clock = pygame.time.Clock()
window_width = 1280
window_height = 720
window = pygame.display.set_mode((window_width,window_height))
paddle_width = 30
paddle_height = 120
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
orange = (255,128,0)
green = (0, 255, 0)

p1score = 0
p2score = 0

#game objects
paddle1 = pygame.Rect(50,150, paddle_width, paddle_height)
paddle2 = pygame.Rect(window_width - 50 - paddle_width, 150, paddle_width, paddle_height)
paddle3 = pygame.Rect(595,50, paddle_height, paddle_width)
paddle4 = pygame.Rect(595, window_height - paddle_height, paddle_height, paddle_width)
ball = pygame.Rect(window_width // 2 - 10, window_height // 2 - 10, 20, 20)
ballxspeed = 1.5
ballyspeed = -1.5

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
    ball.x += ballxspeed
    ball.y += ballyspeed
    
    #handling collisions
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ballxspeed *= -1
    if ball.colliderect(paddle3) or  ball.colliderect(paddle4):
        ballyspeed *= -1
    
    x1 = random.choice([-1,1])
    y1 = random.choice([-1,1])
    print(str(x1))
    print(str(y1))
    if ball.x < 50 or ball.y < 50:
        p2score += 1
        #center ball not accounting to size
        ballxspeed *= x1
        ball.x = 640
        ball.y = 360
    elif ball.x > 1230 or ball.y > 680:
        p1score += 1
        #center ball not accounting to size
        ballyspeed *= y1
        ball.x = 640
        ball.y = 360
        
    
    
    #screen rendering
    window.fill(blue)
    pygame.draw.rect(window, green, paddle1)
    pygame.draw.rect(window, orange, paddle2)
    pygame.draw.rect(window, green, paddle3)
    pygame.draw.rect(window, orange, paddle4)
    pygame.draw.ellipse(window, black, ball)
    
    pygame.display.update()
    clock.tick(120)
    #print(str(p1score))
    #print(str(p2score))