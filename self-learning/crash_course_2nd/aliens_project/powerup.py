import pygame
from pygame.sprite import Sprite
from random import randint


class Powerup(Sprite):
    """Class used to draw and manage powerup abilities"""

    def __init__(self, ai_game):
        """Create a powerup which the player can use at a set interval"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = self.settings.pu_colour

        # Create a rect and place the powerup at a random location at the bottom of the screen
        placement = randint(2, self.settings.screen_width - 2)
        self.rect = pygame.Rect(placement, self.settings.screen_height - 50, self.settings.pu_width, self.settings.pu_height)

    def draw_powerup(self):
        """Draw powerup on the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)