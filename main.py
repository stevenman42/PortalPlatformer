import pygame, sys

from interaction import *
from classes import *
from shooting import *

pygame.init()

WIDTH =  960
HEIGHT = 640

screen = pygame.display.set_mode((960,640))

pygame.display.set_caption("Portal 3")

clock = pygame.time.Clock()

player = Character(WIDTH/2, HEIGHT-16, 16, 16)

# Colors #

RED = (255, 38, 33)
BLUE = (0, 186, 255)

# Variables and whatnot #

CanShoot = True

# Lists of things #

PortalList = []		# I don't think there should ever be any more than two values in this list [blue_portal, orange_portal], either 0 or 1 (ex: [0,0] if neither have been fired.)
EverythingList = []	# Pretty much everything



while True:

	interaction = Interaction()

	if interaction == 'up':
		player.yVel = -5

	elif interaction == 'down':
		player.yVel = 5

	elif interaction == 'left':
		player.xVel = -5

	elif interaction == 'right':
		player.xVel = 5


	mPos = pygame.mouse.get_pos()

	# Game Logic or totes whatevs #

	mospressed = pygame.mouse.get_pressed()
	clict = mospressed[0]
	right_clict = mospressed[2]

	if clict == 1:

		if CanShoot:
			print('blue')
			ShootBlue(PortalList, EverythingList, player, mPos)
			CanShoot = False
		else:
			pass
		CanShoot = False

	CanShoot = False
		
		

	if clict == 0:

		CanShoot = True

	if right_clict == 1:

		if CanShootOrange:
			print('orange')
			ShootOrange(PortalList, EverythingList, player, mPos)
			CanShootOrange = False
		else:
			pass
		CanShootOrange = False
		

	if right_clict == 0:

		CanShootOrange = True




	player.xPos += player.xVel
	player.yPos += player.yVel

	for thing in EverythingList:

		thing.xPos += thing.xVel
		thing.yPos += thing.yVel

		



	# Drawing #

	screen.fill((0,0,0))

	player.render(screen)

	for thing in EverythingList:
		thing.render(screen)


	# End Drawing


	clock.tick(60)
	pygame.display.flip()