# ==========================================================
# Input Mixer - Allows for simultaneous inputs (keyboard & controller)
# ==========================================================

import math

def mix_inputs(inputs):
    """
    Combine multiple (x, y) input vectors into one.
    """
    x = sum(i.input_x for i in inputs)
    y = sum(i.input_y for i in inputs)

    length = math.hypot(x, y)
    if length > 1:
        x /= length
        y /= length

    return x, y