import pygame

from settings import Settings

class Ship():

    def __init__(self, ai_settings: Settings, screen: pygame.Surface) -> None:
        """Initialize the ship and set its starting position."""
        self.screen: pygame.surface = screen
        self.ai_settings: Settings = ai_settings

        # Load the ship image and get its rect.
        self.image: pygame.Surface = pygame.image.load('images/icons/ffffff/transparent/1x1/lorc/deathcab.png').convert()
        self.original_rect: pygame.Rect = self.image.get_rect()

        # Calculate new dimensions for the image (half size)
        self.new_width = self.original_rect.width //2
        self.new_height = self.original_rect.height //2

        # Scale the image to the new dimension
        self.image = pygame.transform.scale(self.image, (self.new_width, self.new_height))
        self.rect: pygame.Rect = self.image.get_rect()
        self.screen_rect: pygame.Rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal values for ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right: bool = False
        self.moving_left: bool = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        # Note: continuing movement to the edge could move the level to not visible parts, move camera
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
