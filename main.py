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
									#  [player, player] is just a placeholder in these three thingies
CanShoot = True					#	  /
CanShootBullet = 'True'
gravity = 1
								#	 /
# Lists of things #				#	/

PortalList = [player, player]		# I don't think there should ever be any more than two values in this list [blue_portal, orange_portal], either 0 or 1 (ex: [0,0] if neither have been fired.)
EverythingList = [player, player]	# Pretty much everything
OtherPortalList = []				# The first portal list is to detect whether or not the portals have been fired or stopped or neither
BulletList = []						# The second is for collisions and suchlike

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

	elif interaction == 'space':

		space_interaction = SpaceInteraction(CanShootBullet)

		if space_interaction == 'True':

			print('pew')

		else:

			Bullet = ShootBullet(player, mPos)
			EverythingList.append(Bullet)
			BulletList.append(Bullet)

	mPos = pygame.mouse.get_pos()

	# Game Logic or totes whatevs #

	mospressed = pygame.mouse.get_pressed()
	clict = mospressed[0]
	right_clict = mospressed[2]

	if clict == 1:

		if CanShoot:
			if PortalList[0] == 'moving':
				BluePortal.xVel = 0
				BluePortal.yVel = 0
				PortalList[0] = 'stopped'
			else:
				if PortalList[0] == 'stopped':
					EverythingList.remove(BluePortal)
					OtherPortalList.remove(BluePortal)
				ShootBlue(player, mPos)
				BluePortal = ShootBlue(player, mPos)
				PortalList[0] = 'moving'
				EverythingList.append(BluePortal)
				OtherPortalList.append(BluePortal)
				CanShoot = False
		else:
			pass
		CanShoot = False

	CanShoot = False
		
		

	if clict == 0:

		CanShoot = True

	if right_clict == 1:

		if CanShootOrange:
			if PortalList[1] == 'moving':
				OrangePortal.xVel = 0
				OrangePortal.yVel = 0
				PortalList[1] = 'stopped'
			else:
				if PortalList[1] == 'stopped':
					EverythingList.remove(OrangePortal)
					OtherPortalList.remove(OrangePortal)
				ShootOrange(player, mPos)
				OrangePortal = ShootOrange(player, mPos)
				PortalList[1] = 'moving'
				EverythingList.append(OrangePortal)
				OtherPortalList.append(OrangePortal)
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

	for portal in OtherPortalList:

		for bullet in BulletList:

			portal.rect = pygame.Rect(portal.xPos, portal.yPos, portal.width, portal.height)
			bullet.rect = pygame.Rect(bullet.xPos, bullet.yPos, bullet.width, bullet.height)

			if portal.rect.contains(bullet.rect):

				if portal.number == 1:

					bullet.xPos = OrangePortal.xPos + 8
					bullet.yPos = OrangePortal.yPos + 8

				elif portal.number == 2:

					bullet.xPos = BluePortal.xPos + 8
					bullet.yPos = BluePortal.yPos + 8

			bullet.yVel += gravity

		

	# Drawing #

	screen.fill((0,0,0))

	player.render(screen)

	for thing in EverythingList:
		thing.render(screen)


	# End Drawing


	clock.tick(60)
	pygame.display.flip()