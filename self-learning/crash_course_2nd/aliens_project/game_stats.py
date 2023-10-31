class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset
        self.high_score = 0

        # Start alien invastion in an active state
        self.game_active = False

    def reset_stats(self):
        """initialize stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
