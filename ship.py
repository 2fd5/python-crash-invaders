import pygame

class Ship():

    def __init__(self, screen: pygame.Surface) -> None:
        """Initialize the ship and set its starting position."""
        self.screen: pygame.surface = screen

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

        # Movement flag
        self.moving_right: bool = False
        self.moving_left: bool = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
