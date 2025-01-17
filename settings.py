class Settings():
    """A class to store all settings for Mushroom Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # Ship settings
        self.ship_speed_factor = 1.5
