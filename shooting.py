import pygame
from classes import *

HEIGHT = 640
WIDTH = 960

def ShootBlue(PortalList, EverythingList, player, mPos):

	mPos = pygame.mouse.get_pos()

	portal = Portal(player.xPos, player.yPos, 8, 8, 1)

	if portal.xPos < mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/12
	elif portal.xPos > mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/12

	if portal.yPos < mPos[1]:
		portal.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/12
	elif portal.yPos > mPos[1]:
		portal.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/12

	PortalList.append(portal)
	EverythingList.append(portal)




def ShootOrange(PortalList, EverythingList, player, mPos):

	portal = Portal(player.xPos, player.yPos, 8, 8, 2)

	if portal.xPos < mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/12
	elif portal.xPos > mPos[0]:
		portal.xVel = (mPos[0]-player.xPos)/12

	if portal.yPos < mPos[1]:
		portal.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/12
	elif portal.yPos > mPos[1]:
		portal.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/12

	PortalList.append(portal)
	EverythingList.append(portal)