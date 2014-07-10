import pygame, sys

def Interaction():

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:

				pygame.quit()
				sys.exit()

			elif event.key == pygame.K_UP:

				return("up")

			elif event.key == pygame.K_DOWN:

				return("down")

			elif event.key == pygame.K_LEFT:

				return("left")

			elif event.key == pygame.K_RIGHT:

				return("right")

			elif event.key == pygame.K_SPACE:

				return("space")

		elif event.type == pygame.KEYUP:

			pass


def SpaceInteraction(CanShootBullet):

	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_SPACE:

				if CanShootBullet == 'True':

					CanShootBullet = 'False'
				
					return "False"


		elif event.type == pygame.KEYUP:

			if event.key == pygame.K_SPACE:

				if CanShootBullet == 'False':

					CanShootBullet = 'True'

					return "True"



