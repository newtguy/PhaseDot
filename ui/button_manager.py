# ==========================================================
# Button manager (selection & input)
# ==========================================================

class ButtonManager:
    def __init__(self):
        self.buttons = []
        self.selected_index = 0

    def add(self, button):
        """ Add a PolygonButton and maintain selection state """
        self.buttons.append(button)
        self._update_selection()

    def clear(self):
        """Remove all buttons from manager"""
        self.buttons = []
        self.selected_index = 0

    def _update_selection(self):
        """ Ensure only the selected button is marked as selected """
        for i, button in enumerate(self.buttons):
            button.selected = (i == self.selected_index)

    def move_selection(self, direction):
        """ Move selection up/down (or left/right) """
        if not self.buttons:
            return
        self.selected_index = (self.selected_index + direction) % len(self.buttons)
        self._update_selection()

    def activate_selected(self):
        """ Activate the currently selected button """
        if self.buttons:
            self.buttons[self.selected_index].activate()

    def update(self, delta_time):
        """ Update all buttons (rotation, animations, etc.) """
        for button in self.buttons:
            button.update(delta_time)

    def draw(self):
        """ Draw all buttons """
        for button in self.buttons:
            button.draw()

    def check_mouse(self, x, y):
        """
        Update selection based on mouse hover.
        Returns the button under the cursor (if any), None otherwise
        """
        for i, button in enumerate(self.buttons):
            if button.hit_test(x, y):
                self.selected_index = i
                self._update_selection()
                return button
        return None
