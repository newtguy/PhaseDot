# ==========================================================
# Initializes Arcade Window
# Launches game
# ==========================================================


import arcade
from views.menu_view import MenuView

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT, 
    SCREEN_TITLE, 
    DEFAULT_FONT_PATH
)

def main():
    window = arcade.Window(
        SCREEN_WIDTH, 
        SCREEN_HEIGHT, 
        SCREEN_TITLE
    )

    # Load font once
    arcade.load_font(DEFAULT_FONT_PATH)

    start_view = MenuView()
    window.show_view(start_view)

    arcade.run()

if __name__ == "__main__":
    main()