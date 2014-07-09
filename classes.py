class Character(object):

	def __init__(self, xPos, yPos, width, height):

		self.xPos = xPos
		self.yPos = yPos

		self.width = width
		self.height = height

	def render(self, screen):

		pygame.draw.rect(screen, (0,0,0), (self.xPos, self.yPos, self.width, self.height))


class Tile(object):

	def __init__(self, xPos, yPos, width, height):

		pass