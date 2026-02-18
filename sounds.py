# ==========================================================
# Preloads music/sounds and plays events
# ==========================================================

import arcade
import os

ASSET_PATH = "assets/sounds/"

SOUNDS = {
    "collect": arcade.load_sound(os.path.join(ASSET_PATH, "collect.wav")),
    "hit": arcade.load_sound(os.path.join(ASSET_PATH, "hit.wav")),
}

def play(sound_name):
    if sound_name in SOUNDS:
        arcade.play_sound(SOUNDS[sound_name])
