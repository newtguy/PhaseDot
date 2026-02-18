# ==========================================================
# Enemy class (behavior)
# ==========================================================

import arcade
import random
import math

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BASE_ENEMY_SPEED,
    BASE_ENEMY_SIZE,
    MIN_SPAWN_DISTANCE,
    THEMES
)


# --------------------
# Speeds
# --------------------

SPEEDS = {
    "basic": BASE_ENEMY_SPEED,
    "intermediate": BASE_ENEMY_SPEED + 2,
    "hard": BASE_ENEMY_SPEED + 4
}

class Enemy(arcade.Sprite):
    """
    Enemy sprite with:
    - Difficulty: basic / intermediate / hard
    - Color from theme
    - Random movement (horizontal/vertical or diagonal for hard)
    - Safe spawn distance away from player
    """
    def __init__(self, difficulty="basic"):
        # Call Sprite __init__ first with a placeholder texture
        # super().__init__() must run before accessing any Sprite properties
        super().__init__(arcade.make_circle_texture(BASE_ENEMY_SIZE, (255, 0, 0)))

        # Now safe to set properties
        self.difficulty = difficulty.lower()
        self.speed = SPEEDS.get(self.difficulty, 3)
        self.color = THEMES["NeonVoid"][f"enemy_{self.difficulty}"]
        self.width = self.height = BASE_ENEMY_SIZE

        # Position and movement initialization
        self.center_x = 0
        self.center_y = 0
        self.change_x = 0
        self.change_y = 0

    def set_movement(self):
        """Set movement based on difficulty."""
        if self.difficulty in ["basic", "intermediate"]:
            # 50/50 horizontal or vertical
            if random.choice([True, False]):
                self.change_x = random.choice([-self.speed, self.speed])
                self.change_y = 0
            else:
                self.change_x = 0
                self.change_y = random.choice([-self.speed, self.speed])
        elif self.difficulty == "hard":
            # Diagonal movement
            self.change_x = random.choice([-self.speed, self.speed])
            self.change_y = random.choice([-self.speed, self.speed])

    def spawn_safe(self, player_sprite):
        """Spawn enemy at a position safely away from the player."""
        while True:
            x = random.randint(50, SCREEN_WIDTH - 50)
            y = random.randint(50, SCREEN_HEIGHT - 50)
            distance_player = math.hypot(player_sprite.center_x - x,
                                         player_sprite.center_y - y)
            if distance_player >= MIN_SPAWN_DISTANCE:
                break

        self.center_x = x
        self.center_y = y
        self.set_movement()

    def update(self, delta_time: float = 0):
        """
            Move enemy and bounce off walls.
            Although delta_time is not used, must be included as param
            arcade.SpriteList.update() automatically passes delta_time to each sprite’s update()
        """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom <= 0 or self.top >= SCREEN_HEIGHT:
            self.change_y *= -1
