# ==========================================================
# Keyboard Input 
# ==========================================================

import arcade
from input.base_input import BasePlayerInput

class KeyboardInput(BasePlayerInput):
    def on_key_press(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.UP):
            self.input_y = 1
        elif key in (arcade.key.S, arcade.key.DOWN):
            self.input_y = -1
        elif key in (arcade.key.A, arcade.key.LEFT):
            self.input_x = -1
        elif key in (arcade.key.D, arcade.key.RIGHT):
            self.input_x = 1

    def on_key_release(self, key, modifiers):
        if key in (arcade.key.W, arcade.key.S, arcade.key.UP, arcade.key.DOWN):
            self.input_y = 0
        elif key in (arcade.key.A, arcade.key.D, arcade.key.LEFT, arcade.key.RIGHT):
            self.input_x = 0

    def update(self, delta_time):
        pass
