import pygame, sys

from interaction import *

pygame.init()

screen = pygame.display.set_mode((960,640))

pygame.display.set_caption("Portal 3")

clock = pygame.time.Clock()









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






	# Game Logic or totes whatevs #

	player.xPos += player.xVel
	player.yPos += player.yVel


	# Drawing #

	screen.fill((0,0,0))


	# End Drawing


	clock.tick(60)
	pygame.display.flip()