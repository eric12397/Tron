import pygame

class Scoreboard():
	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (255,255,255) #black
		self.font = pygame.font.SysFont(None, 96)

		self.player_1_score = 0
		self.player_2_score = 0
		self.score_limit = 5

	def display_text(self, text):
		self.score_image = self.font.render(text, True, self.text_color, (0,0,0))
		self.score_rect = self.score_image.get_rect()
		self.score_rect.center = self.screen_rect.center
		self.screen.blit(self.score_image, self.score_rect)
		pygame.display.flip()

	def update_score(self):
		text = str(self.player_1_score) + ' - ' + str(self.player_2_score)
		self.display_text(text)

	def reset_score(self, screen):
		self.player_1_score = 0
		self.player_2_score = 0
		screen.fill((0,0,0))

	def play_again(self):
		text = "Rematch?"
		self.display_text(text)