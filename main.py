import pygame, sys

from interaction import *

pygame.init()

screen = pygame.display.set_mode((960,640))

pygame.display.set_caption("Portal 3")

clock = pygame.time.Clock()

player = Player









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

	clict = pygame.mouse.get_pressed()[0]

	projectile = Projectile(player.xPos, player.yPos, 8, 8)

	if projectile.xPos < mPos[0]:
		projectile.xVel = (mPos[0]-player.xPos)/(uniform(10.5,11.5))
	elif projectile.xPos > mPos[0]:
		projectile.xVel = (mPos[0]-player.xPos)/(uniform(10.5,11.5))

	if projectile.yPos < mPos[1]:
		projectile.yVel = ((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/(uniform(10.5,11.5))
	elif projectile.yPos > mPos[1]:
		projectile.yVel = -((HEIGHT-(HEIGHT-player.yPos)) - mPos[1])/(uniform(10.5,11.5))

	projectileList.append(projectile)
	EverythingList.append(projectile)

	

	right_clict = pygame.mouse.get_pressed()[1]

	player.xPos += player.xVel
	player.yPos += player.yVel


	# Drawing #

	screen.fill((0,0,0))


	# End Drawing


	clock.tick(60)
	pygame.display.flip()