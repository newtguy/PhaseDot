# ==========================================================
# Collectible - Handles a single collectible
# ==========================================================

import arcade
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, THEMES

class Collectible(arcade.Sprite):
    """A single collectible on the screen."""

    def __init__(self, theme_name="NeonVoid"):
        color = THEMES[theme_name]["collectible"]
        super().__init__(arcade.make_circle_texture(15, color))
        self.theme_name = theme_name
        self.respawn()

    def respawn(self):
        """Place collectible at a random position on the screen."""
        self.center_x = random.randint(20, SCREEN_WIDTH - 20)
        self.center_y = random.randint(20, SCREEN_HEIGHT - 20)
