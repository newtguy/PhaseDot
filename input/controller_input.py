# ==========================================================
# Controller input - uses pyglet to manage controller inputs
# ==========================================================

# input/controller_input.py

import pyglet
from input.base_input import BasePlayerInput

class ControllerInput(BasePlayerInput):
    def __init__(self, deadzone=0.2):
        super().__init__()
        self.deadzone = deadzone
        self.controller = None
        self.detect_controller()

    def detect_controller(self):
        controllers = pyglet.input.get_joysticks()
        if controllers:
            self.controller = controllers[0]
            self.controller.open()
        else:
            self.controller = None

    def update(self, delta_time):
        if self.controller is None:
            self.detect_controller()
        if not self.controller:
            return

        x = self.controller.x
        y = self.controller.y

        if abs(x) < self.deadzone:
            x = 0
        if abs(y) < self.deadzone:
            y = 0

        self.input_x = x
        self.input_y = y
