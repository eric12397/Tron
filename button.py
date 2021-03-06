import pygame

class Button():
    def __init__ (self, screen, x, y, msg):
        """Set the dimensions and properties of the button."""
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30
        self.button_color = (14,24,41) # black
        self.text_color = (255, 255, 255) # white
        self.msg = msg # whatever text the button shows
        self.font = pygame.font.SysFont(None, 42) #style of font, font size
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) # rect of button
        self.prep_msg()

    def prep_msg(self):
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)