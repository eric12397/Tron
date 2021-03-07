import pygame

class Player():
	def __init__(self, screen, x, y, width, height, dx, dy, color):
		"""Create player's tron bike."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.x = x
		self.y = y
		self.width = width 
		self.height = height 
		self.dx = dx # velocity in x-direction
		self.dy = dy # velocity in y-direction
		self.tron_path = []
		self.color = color
		# Player rect
		self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

	def update_position(self):
		self.rect[0] += self.dx # changes rect's x-coordinate
		self.rect[1] += self.dy # changes rect's y-coordinate
		self.tron_path.append(self.rect.copy())

	def draw_player(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

	def reset_tron_path(self):
		self.tron_path = [];