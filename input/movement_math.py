# ==========================================================
# Movement helpers - input agnostic
# This module handles smooth acceleration and deceleration for player movement.
# ==========================================================

import math

import math

def approach(current, target, delta):
    if current < target:
        return min(current + delta, target)
    elif current > target:
        return max(current - delta, target)
    return target


def apply_acceleration(player, input_x, input_y, delta_time):
    """
    Apply acceleration and friction to any Arcade SpriteCircle
    using the built-in `change_x` and `change_y` as velocity.
    """

    length = math.hypot(input_x, input_y)

    if length > 0:
        # Normalize input for diagonal movement
        input_x /= length
        input_y /= length

        # Target velocity
        target_vx = input_x * player.speed
        target_vy = input_y * player.speed

        # Accelerate toward target using SpriteCircle's built-in velocity
        player.change_x = approach(player.change_x, target_vx, player.acceleration * delta_time)
        player.change_y = approach(player.change_y, target_vy, player.acceleration * delta_time)
    else:
        # No input: apply friction
        player.change_x = approach(player.change_x, 0, player.friction * delta_time)
        player.change_y = approach(player.change_y, 0, player.friction * delta_time)

