import pygame,sys,time
from pygame.locals import *
import math
WINDOWWIDTH=640
WINDOWHEIGHT=480
BACKGROUNDCOLOR=(0,0,0)
BALL_COLOR = (0,0,225)
BALL_SIZE = 4

GAME_STATE_INIT=0
GAME_STATE_RUN=1
GAME_STATE_SHUTDOWN=2
GAME_STATE_EXIT=3

game_state = GAME_STATE_INIT

pygame.init()
mainClock = pygame.time.Clock()

windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('开炮')

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()

	if game_state == GAME_STATE_INIT:
		timestep=0.1
		ball_x = 10
		ball_y = 10
		velocity=10
		angle=0
		sinx=math.sin(angle*math.pi/180)
		cosx=math.cos(angle*math.pi/180)
		vx=velocity*cosx
		vy=velocity*sinx
		pygame.draw.circle(windowSurface, BALL_COLOR,(ball_x,ball_y),BALL_SIZE,0)

		if event.key == pygame.K_UP:
			angle+=15

		if event.key == pygame.K_UP:
			angle-=15

		if event.key == pygame.K_SPACE:
			sinx=math.sin(angle*math.pi/180)
			cosx=math.cos(angle*math.pi/180)
			vx=velocity*cosx
			vy=velocity*sinx
			game_state = GAME_STATE_RUN
	
	elif game_state == GAME_STATE_RUN:
			ball_y+=vy*timestep
			ball_x+=vx*timestep
			vy-=timestep*9.8
			pygame.draw.circle(windowSurface, BALL_COLOR,(ball_x,ball_y),BALL_SIZE,0)

	elif game_state == GAME_STATE_SHUTDOWN:
			game_state = GAME_STATE_EXIT



	windowSurface.fill(BACKGROUNDCOLOR)

	pygame.display.update()
	mainClock.tick(30)