class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initiator"""
        self.screen_width = 1400
        self.screen_height = 1000
        self.bg_colour = (0, 0, 0)

        # Ship settings
        self.ship_limit = 3

        # Bullet  settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (200, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Powerup settings
        self.pu_height = 10
        self.pu_width = 10
        self.pu_colour = (0, 255, 0)

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How much the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that can change throughout the game"""
        self.ship_speed = 0.6
        self.bullet_speed = 1
        self.alien_speed = 0.5

        # fleet_direction of represents right, -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


