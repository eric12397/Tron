import pygame
import sys
import time
from player import Player
from scoreboard import Scoreboard
from button import Button

# All functions
def reset_tron_paths():
	global tron_path_1, tron_path_2
	tron_path_1 = [] # empty tron path lists
	tron_path_2 = [] 

def new_game():
	time.sleep(1.5)
	screen.fill((0,0,0)) # black
	player_1 = Player(screen, x=200, y=300, width=5, height=5, dx=5, 
						dy=0, tron_path=tron_path_1, color=PINK) # player 1
	player_2 = Player(screen, x=800, y=300, width=5, height=5, dx=-5, 
						dy=0, tron_path=tron_path_2, color=WHITE) # player 2
	return player_1, player_2

def check_for_winner(scoreboard):
	if scoreboard.player_1_score == scoreboard.score_limit:
		text = "Player 1 is the winner !!"
		scoreboard.display_text(text)
		screen.fill((0,0,0))
		time.sleep(1.5)
		return False # returns game_active as False

	elif scoreboard.player_2_score == scoreboard.score_limit:
		text = "Player 2 is the winner !!"
		scoreboard.display_text(text)
		screen.fill((0,0,0))
		time.sleep(1.5)
		return False
	else:
		return True # if no winner, returns game_active as True

def ask_to_play_again(screen, scoreboard, yes_button, no_button):
	scoreboard.play_again()
	yes_button.draw_button()
	no_button.draw_button()

def check_click_events(yes_button, no_button, mouse_x, mouse_y, screen):
	yes_button_clicked = yes_button.rect.collidepoint(mouse_x, mouse_y)
	no_button_clicked = no_button.rect.collidepoint(mouse_x, mouse_y)
	if yes_button_clicked:
		scoreboard.reset_score(screen)
		global game_active
		game_active = True

	if no_button_clicked:
		global playing
		playing = False
###################################################################################################################################

# Initialize pygame settings.
pygame.init()
screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Tron")

# Initialize Player settings
PINK = ((219,62,177)) 
WHITE = ((255,255,255)) 

tron_path_1 = [] # List to keep track of rectangles for each player
tron_path_2 = []

player_1 = Player(screen, x=200, y=300, width=5, height=5, dx=5, dy=0, 
					tron_path=tron_path_1, color=PINK) # player 1
player_2 = Player(screen, x=800, y=300, width=5, height=5, dx=-5, dy=0, 
					tron_path=tron_path_2, color=WHITE) # player 2

# Walls
walls = [pygame.Rect(0, 0, 30, 700), pygame.Rect(0, 0, 1000, 30), 
		pygame.Rect(970, 0, 30, 700), pygame.Rect(0, 670, 1000, 30)]

# Scoreboard
scoreboard = Scoreboard(screen)

# Buttons
yes_button = Button(screen, x=400, y=400, msg="Yes")
no_button = Button(screen, x=525, y=400, msg="No")

# Main loop
playing = True
game_active = True
while playing:
	clockobject = pygame.time.Clock()
	clockobject.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_click_events(yes_button, no_button, mouse_x, mouse_y, screen)

		elif event.type == pygame.KEYDOWN:
			# Player 1 controls
			if event.key == pygame.K_w:
				player_1.dx = 0
				player_1.dy = -5
			elif event.key == pygame.K_s:
				player_1.dx = 0
				player_1.dy = 5
			elif event.key == pygame.K_d:
				player_1.dx = 5
				player_1.dy = 0
			elif event.key == pygame.K_a:
				player_1.dx = -5
				player_1.dy = 0
			# Player 2 controls
			if event.key == pygame.K_UP:
				player_2.dx = 0
				player_2.dy = -5
			elif event.key == pygame.K_DOWN:
				player_2.dx = 0
				player_2.dy = 5
			elif event.key == pygame.K_RIGHT:
				player_2.dx = 5
				player_2.dy = 0
			elif event.key == pygame.K_LEFT:
				player_2.dx = -5
				player_2.dy = 0

	if game_active:
		for wall in walls: # draw game boundaries
			pygame.draw.rect(screen, (14,24,41), wall)

		player_1.update_position() # move each player
		player_2.update_position()
		player_1.draw_player() # draw each player
		player_2.draw_player()

		# if player 1 crashes into boundary, own path, or other player's path >> player 2 wins round
		if player_1.rect.collidelist(walls) != -1 or player_1.rect.collidelist(tron_path_1[:-2]) != -1 \
		or player_1.rect.collidelist(tron_path_2[:-2])!= -1:

			scoreboard.player_2_score += 1
			scoreboard.update_score()
			reset_tron_paths()
			player_1, player_2 = new_game()

		# if player 2 crashes into walls, own path, or other player's path >> player 1 wins round
		if player_2.rect.collidelist(walls) != -1 or player_2.rect.collidelist(tron_path_2[:-1]) != -1 \
		or player_2.rect.collidelist(tron_path_1[:-1])!= -1:

			scoreboard.player_1_score += 1
			scoreboard.update_score()
			reset_tron_paths()
			player_1, player_2 = new_game()

		# check which player won
		game_active = check_for_winner(scoreboard)

	if not game_active:
		ask_to_play_again(screen, scoreboard, yes_button, no_button)

	pygame.display.flip()


