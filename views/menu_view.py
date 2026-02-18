# ==========================================================
# Main Menu View (render
# ==========================================================

import arcade
from settings import (
    SCREEN_WIDTH, 
    SCREEN_HEIGHT, 
    THEMES, 
    TITLE_FONT_SIZE, 
    DEFAULT_FONT_NAME
)
from ui.polygon_button import PolygonButton
from ui.button_manager import ButtonManager

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        self.title_text = None
        self.manager = ButtonManager()
        self.theme_name = "NeonVoid"
        self.theme = THEMES[self.theme_name]

    def on_show_view(self):
        arcade.set_background_color(self.theme["background"])

        self.manager.clear()

        # Title
        self.title_text = arcade.Text(
            "PHASEDOT",
            SCREEN_WIDTH // 2, 
            SCREEN_HEIGHT * 0.75,
            self.theme["text_primary"],
            font_size=TITLE_FONT_SIZE,
            font_name=DEFAULT_FONT_NAME,
            anchor_x="center"
        )

        # -----------------------------
        # Create Polygon Buttons
        # -----------------------------
        self.manager.add(
            PolygonButton(
                center_x=SCREEN_WIDTH // 2 - 130,
                center_y=SCREEN_HEIGHT // 2 -20,
                radius=110,
                sides=3, # triangle
                label="START",
                action=self.start_game,
                base_color=self.theme["button_base"],
                selected_color=self.theme["button_selected"],
                border_base_color=self.theme["button_border"],
                border_selected_color=self.theme["button_border_selected"],
                label_color=self.theme["text_primary"]
            )
        )

        self.manager.add(
            PolygonButton(
                center_x=SCREEN_WIDTH // 2 + 130,
                center_y=SCREEN_HEIGHT // 2 - 20,
                radius=110,
                sides=4, # square
                label="DOTS",
                action=self.character_select,
                base_color=self.theme["button_base"],
                selected_color=self.theme["button_selected"],
                border_base_color=self.theme["button_border"],
                border_selected_color=self.theme["button_border_selected"],
                label_color=self.theme["text_primary"]
            )
        )

    # -----------------------------
    # Button Actions
    # -----------------------------
    def start_game(self):
        from views.game_view import GameView
        game_view = GameView(level_difficulty="basic")
        game_view.setup()
        self.window.show_view(game_view)

    def character_select(self):
        from views.dot_select_view import DotSelectView
        self.window.show_view(DotSelectView())

    # -----------------------------
    # Arcade Draw & Update
    # -----------------------------
    def on_draw(self):
        self.clear()

        # Title
        if self.title_text:
            self.title_text.draw()
        # Buttons
        self.manager.draw()

        


    def on_update(self, delta_time: float):
        self.manager.update(delta_time)

    # -----------------------------
    # Input Handling
    # -----------------------------
    def on_key_press(self, key, modifiers):
        if key in (arcade.key.UP, arcade.key.W):
            self.manager.move_selection(-1)
        elif key in (arcade.key.DOWN, arcade.key.S):
            self.manager.move_selection(1)
        elif key in (arcade.key.ENTER, arcade.key.SPACE):
            self.manager.activate_selected()

    def on_mouse_motion(self, x, y, dx, dy):
        self.manager.check_mouse(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        hit = self.manager.check_mouse(x, y)
        if hit:
            hit.activate()
