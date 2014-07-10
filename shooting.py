import pygame
from classes import *
from math import sqrt

HEIGHT = 640
WIDTH = 960

def ShootBlue(player, mPos):

	mPos = pygame.mouse.get_pos()

	portal = Portal(player.xPos, player.yPos, 32, 32, 1)

	if portal.xPos < mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/20
	elif portal.xPos > mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/20

	if portal.yPos < mPos[1]:
		portal.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20
	elif portal.yPos > mPos[1]:
		portal.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20

	return portal

def ShootOrange(player, mPos):

	portal = Portal(player.xPos, player.yPos, 32,32, 2)

	if portal.xPos < mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/20
	elif portal.xPos > mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/20

	if portal.yPos < mPos[1]:
		portal.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20
	elif portal.yPos > mPos[1]:
		portal.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20

	return portal

def ShootBullet(player, mPos):

	bullet = Tile(player.xPos, player.yPos, 16, 16, (255,255,255))

	if bullet.xPos < mPos[0]:
		bullet.xVel = (mPos[0]-player.xPos)/20
	elif bullet.xPos > mPos[0]:
		bullet.xVel = (mPos[0]-player.xPos)/20

	if bullet.yPos < mPos[1]:
		bullet.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20
	elif bullet.yPos > mPos[1]:
		bullet.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/20

	return bullet