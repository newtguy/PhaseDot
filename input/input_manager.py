# ==========================================================
# Movement helpers - input agnostic
# This module handles smooth acceleration and deceleration for player movement.
# ==========================================================

from input.input_mixer import mix_inputs

class InputManager:
    def __init__(self, inputs):
        """
        inputs: list of input sources, e.g., [KeyboardInput(), ControllerInput()]
        """
        self.inputs = inputs

    def on_key_press(self, key, modifiers):
        for inp in self.inputs:
            if hasattr(inp, "on_key_press"):
                inp.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        for inp in self.inputs:
            if hasattr(inp, "on_key_release"):
                inp.on_key_release(key, modifiers)

    def update(self, delta_time):
        for inp in self.inputs:
            inp.update(delta_time)

    def get_axis(self):
        """
        Mix inputs from all sources into one (x, y) tuple.
        """
        return mix_inputs(self.inputs)
