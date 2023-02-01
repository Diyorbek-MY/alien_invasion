class Settings:
    """a class store all settings for alien invasion."""

    def __init__(self):
        """initialize the game's static  settings"""
        #screen settings
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # Bullet setting
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # how fast game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """intialize settings that change throughout the game """
        self.ship_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale



