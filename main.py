import pygame, sys

pygame.init()

screen = pygame.display.set_mode((960,640))

pygame.display.set_caption("Portal 3")

clock = pygame.time.Clock()









while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:

			if event.key == pygame.K_ESCAPE:

				pygame.quit()
				sys.exit()

			elif event.key == pygame.K_UP:

				print("up")

			elif event.key == pygame.K_DOWN:

				print("down")

			elif event.key == pygame.K_LEFT:

				print("left")

			elif event.key == pygame.K_RIGHT:

				print("right")





	# Drawing #

	screen.fill((0,0,0))


	# End Drawing


	clock.tick(60)
	pygame.display.flip()