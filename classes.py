import pygame

class Character(object):

	def __init__(self, xPos, yPos, width, height):

		self.xPos = xPos
		self.yPos = yPos

		self.width = width
		self.height = height

		self.xVel = 0
		self.yVel = 0

	def render(self, screen):

		pygame.draw.rect(screen, (255,255,255), (self.xPos, self.yPos, self.width, self.height))


class Tile(object):

	def __init__(self, xPos, yPos, width, height, color):

		self.xPos = xPos
		self.yPos = yPos

		self.width = width
		self.height = height

		self.color = color

		self.xVel = 0
		self.yVel = 0

	def render(self, screen):

		pygame.draw.rect(screen, (self.color), (self.xPos, self.yPos, self.width, self.height))

class Portal(Tile):

	def __init__(self, xPos, yPos, width, height, number):		# Number should be 1 for a blue portal and 2 for an orange one

		self.number = number

		if self.number == 1:
			self.color = (0, 186, 255)

		elif self.number == 2:
			self.color = (255, 139, 13)

		self.xVel = 0
		self.yVel = 0

		Tile.__init__(self, xPos, yPos, width, height, self.color)


