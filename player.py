# ==========================================================
# Player class, movement, upgrades
# ==========================================================

import arcade
from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SKINS
)

class Player(arcade.SpriteCircle):
    """Player sprite with position, skins, and speed."""

    def __init__(self, skin_index=0):
        skin = PLAYER_SKINS[skin_index]

        # SpriteCircle automatically handles texture, radius, and color
        super().__init__(
            radius=skin["size"], 
            color=skin["color"], 
            center_x=SCREEN_WIDTH // 2, 
            center_y=SCREEN_HEIGHT // 2
        )

        # Movement
        self.change_x = 0
        self.change_y = 0
        self.speed = skin["speed"] # max speed
        self.acceleration = 2000   # px/sec^2
        self.friction = 2000       # px/sec^2

        # Skin index
        self.skin_index = skin_index

    def update(self, delta_time: float = 0):
        # SpriteCircle uses change_x/change_y automatically
        super().update()  

        # Keep inside screen bounds
        if self.left < 0:
            self.left = 0
            self.change_x = 0
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
            self.change_x = 0
        if self.bottom < 0:
            self.bottom = 0
            self.change_y = 0
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
            self.change_y = 0
