import sys

import pygame

from settings import Settings
from ship import Ship

def check_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings: Settings , screen: pygame.surface, ship: Ship):
    """Update images on the screen and flip to the new screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
