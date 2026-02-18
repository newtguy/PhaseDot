# ==========================================================
# Base Input Interface
# ==========================================================

import arcade
import math

class BasePlayerInput:
    def __init__(self):
        self.input_x = 0
        self.input_y = 0

    def on_key_press(self, key, modifiers): pass
    def on_key_release(self, key, modifiers): pass
    def update(self, delta_time): pass

