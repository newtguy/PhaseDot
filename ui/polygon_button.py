# ==========================================================
# Polygon button (generation, drawing, updates, activation)
# ==========================================================


import arcade
import arcade.geometry
import math

from settings import (
    MENU_FONT_SIZE,
    DEFAULT_FONT_NAME,
    DEFAULT_FONT_PATH,
    THEMES
)

class PolygonButton:
    def __init__(
        self,
        center_x,
        center_y,
        radius,
        sides,
        action,
        label="",
        label_color=THEMES["NeonVoid"]["text_primary"],
        base_color=THEMES["NeonVoid"]["button_base"],
        selected_color=THEMES["NeonVoid"]["button_selected"],
        border_base_color=THEMES["NeonVoid"]["button_border"],
        border_selected_color=THEMES["NeonVoid"]["button_border_selected"]
    ):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.sides = sides
        self.action = action
        self.label = label

        self.label_color = label_color
        self.base_color = base_color
        self.selected_color = selected_color
        self.border_base_color = border_base_color
        self.border_selected_color = border_selected_color
        self.selected = False

        self.rotation = 0
        self.points = self._generate_points()

    def _generate_points(self):
        """ Generates a list of vertices with (x,y) values """
        points = []
        for i in range(self.sides):
            # 2 * math.pi = 360° in radians
            # i / self.sides spreads vertices evenly around circle
            angle = 2 * math.pi * i / self.sides + self.rotation
            # convert polar to Cartesian (2D plane)
            x = self.center_x + self.radius * math.cos(angle)
            y = self.center_y + self.radius * math.sin(angle)
            points.append((x, y))
        return points

    def update(self, delta_time):
        """ subtle rotation when selected """
        if self.selected:
            self.rotation += delta_time * 2  
            self.points = self._generate_points()

    def draw(self):
        """ Draws polygon with border """
        # Color assignment 
        color = self.selected_color if self.selected else self.base_color
        border_color = self.border_selected_color if self.selected else self.border_base_color
        
        # Arcade draw function
        arcade.draw_polygon_filled(self.points, color)
        arcade.draw_polygon_outline(self.points, color=border_color)


        # label for button
        if self.label:
            arcade.draw_text(
                self.label,
                self.center_x,
                self.center_y,
                self.label_color,
                MENU_FONT_SIZE,
                font_name=DEFAULT_FONT_NAME,
                anchor_x="center",
                anchor_y="center"
            )

    def activate(self):
        self.action()

    def hit_test(self, x, y):
        return self.point_in_polygon(x, y, self.points)
    
    # HELPER FUNCTION FROM GEEKSFORGEEKS
    # Checking if a point is inside a polygon
    def point_in_polygon(self, x, y, polygon):
        num_vertices = len(polygon)
        inside = False

        # Store the first point in the polygon and initialize the second point
        p1 = polygon[0]

        # Loop through each edge in the polygon
        for i in range(1, num_vertices + 1):
            # Get the next point in the polygon
            p2 = polygon[i % num_vertices]

            # Check if the point is above the minimum y coordinate of the edge
            if y > min(p1[1], p2[1]):            
                # Check if the point is below the maximum y coordinate of the edge
                if y <= max(p1[1], p2[1]):
                    # Check if the point is to the left of the maximum x coordinate of the edge
                    if x <= max(p1[0], p2[0]):
                        # Calculate the x-intersection of the line connecting the point to the edge
                        x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
                        # Check if the point is on the same line as the edge or to the left of the x-intersection
                        if p1[0] == p2[0] or x <= x_intersection:
                            # Flip the inside flag
                            inside = not inside

            # Store the current point as the first point for the next iteration
            p1 = p2

        # Return the value of the inside flag
        return inside

