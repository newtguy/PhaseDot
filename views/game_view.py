# ==========================================================
# Game View (level difficulty, hud, player & enemy sprite instances)
# ==========================================================

import arcade
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from collectible import Collectible
from enemy import Enemy

# input imports
from input.base_input import BasePlayerInput
from input.keyboard_input import KeyboardInput
from input.controller_input import ControllerInput
from input.movement_math import apply_acceleration
from input.input_manager import InputManager

class GameView(arcade.View):
    def __init__(self, level_difficulty="basic"):
        super().__init__()
        self.level_difficulty = level_difficulty  # "basic", "intermediate", "hard"

        # SpriteLists
        self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.collectible_list = arcade.SpriteList()

        # HUD
        self.collected_count = 0

        # Countdown
        self.countdown = 3.0
        self.countdown_active = True

        # Input 
        self.controller_check_timer = 0
        self.controller_check_interval = 1.0  # seconds

    def setup(self):
        """Initialize or reset the game."""
        

        # -------------------------
        # Player
        # -------------------------
        self.player_list = arcade.SpriteList()
        player_sprite = Player(skin_index=0)
        self.player_list.append(player_sprite)

        # Input Types
        # Input
        self.keyboard_input = KeyboardInput()
        self.controller_input = ControllerInput()
        self.input_manager = InputManager([self.keyboard_input, self.controller_input])

        # -------------------------
        # Enemy list
        # -------------------------
        self.enemy_list = arcade.SpriteList()
        first_enemy_type = self.get_enemy_type()
        first_enemy = Enemy(first_enemy_type)
        first_enemy.spawn_safe(player_sprite)
        self.enemy_list.append(first_enemy)

        # -------------------------
        # Collectible
        # -------------------------
        self.collectible_list = arcade.SpriteList()
        collectible_sprite = Collectible(theme_name="NeonVoid")
        self.collectible_list.append(collectible_sprite)

        # -------------------------
        # Reset HUD & countdown
        # -------------------------
        self.collected_count = 0
        self.countdown = 3.0
        self.countdown_active = True

    # -----------------------------
    # Determine enemy type based on level
    # -----------------------------
    def get_enemy_type(self):
        if self.level_difficulty == "basic":
            return "basic"
        elif self.level_difficulty == "intermediate":
            return random.choice(["basic", "intermediate"])
        elif self.level_difficulty == "hard":
            return random.choice(["basic", "intermediate", "hard"])
        return "basic"

    # -----------------------------
    # Update game state
    # -----------------------------
    def on_key_press(self, key, modifiers):
        self.input_manager.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.input_manager.on_key_release(key, modifiers)

    def on_update(self, delta_time: float):
        # Countdown before game starts
        if self.countdown_active:
            self.countdown -= delta_time
            if self.countdown <= 0:
                self.countdown_active = False
            return  # skip updates until countdown finishes

        # -------------------------
        # Update sprites
        # -------------------------

        # Update all inputs
        self.input_manager.update(delta_time)

        # Get combined x/y input
        x, y = self.input_manager.get_axis()

        # Apply movement
        apply_acceleration(self.player_list[0], x, y, delta_time)

        self.player_list.update(delta_time)
        self.enemy_list.update(delta_time)
        self.collectible_list.update()

        # -------------------------
        # Player & collectible collision
        # -------------------------
        player_sprite = self.player_list[0]  # only one player
        collectible_sprite = self.collectible_list[0]  # only one collectible

        if arcade.check_for_collision(player_sprite, collectible_sprite):
            collectible_sprite.respawn()
            self.collected_count += 1

            # Spawn new enemy
            new_enemy_type = self.get_enemy_type()
            new_enemy = Enemy(new_enemy_type)
            new_enemy.spawn_safe(player_sprite)
            self.enemy_list.append(new_enemy)

        # -------------------------
        # Enemy collision -> Game Over
        # -------------------------
        if arcade.check_for_collision_with_list(player_sprite, self.enemy_list):
            print("Player hit! Game over.")

            # Update high score
            from save_system import update_score
            update_score(self.collected_count)

            from views.menu_view import MenuView
            self.window.show_view(MenuView())

    # -----------------------------
    # Draw HUD & game objects
    # -----------------------------
    def on_draw(self):
        self.clear()

        from save_system import load_save

        # At the start of on_draw
        save_data = load_save()
        high_score = save_data.get("high_score", 0)

        # Draw high score
        arcade.draw_text(
            f"High Score: {high_score}",
            SCREEN_WIDTH - 10, SCREEN_HEIGHT - 20,
            arcade.color.GOLD, 16,
            anchor_x="right"
        )

        # Draw all sprite lists
        self.player_list.draw()
        self.enemy_list.draw()
        self.collectible_list.draw()

        # Draw HUD (collected count)
        arcade.draw_text(
            f"Collected: {self.collected_count}",
            10, SCREEN_HEIGHT - 20,
            arcade.color.WHITE, 16
        )

        # Draw countdown if active
        if self.countdown_active:
            arcade.draw_text(
                f"{int(self.countdown) + 1}",
                SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                arcade.color.YELLOW, 48,
                anchor_x="center", anchor_y="center"
            )
