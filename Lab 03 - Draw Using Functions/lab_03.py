# Athens Parthenon Recreation

import arcade

screen_width = 1000
screen_height = 1000


def draw_vertical_grid(x, y):
    #Vertical Grid Layout
    arcade.draw_line(x + 100, y, 100, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 200, y, 200, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 300, y, 300, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 400, y, 400, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 500, y, 500, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 600, y, 600, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 700, y, 700, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 800, y, 800, 1000, arcade.csscolor.BLACK)
    arcade.draw_line(x + 900, y, 900, 1000, arcade.csscolor.BLACK)

def draw_horizontal_grid(x, y):
    #Horizontal Grid Layout
    arcade.draw_line(x, y + 100, 1000, 100, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 200, 1000, 200, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 300, 1000, 300, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 400, 1000, 400, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 500, 1000, 500, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 600, 1000, 600, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 700, 1000, 700, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 800, 1000, 800, arcade.csscolor.BLACK)
    arcade.draw_line(x, y + 900, 1000, 900, arcade.csscolor.BLACK)

def draw_bushes(x, y):
    # Background Bushes Left
    arcade.draw_arc_filled(x, y, 250, 250, arcade.color.ARMY_GREEN, 0, 180)
    arcade.draw_arc_filled(x - 50, y, 300, 300, arcade.color.DARK_OLIVE_GREEN, 0, 180)
    arcade.draw_arc_filled(x - 100, y, 200, 250, arcade.color.ARMY_GREEN, 0, 180)
    arcade.draw_arc_filled(x + 100, y, 200, 200, arcade.color.DARK_GREEN, 0, 180)
    arcade.draw_arc_filled(x + 25, y, 300, 300, arcade.color.DARK_OLIVE_GREEN, 0, 180)

def draw_clouds(x, y):
    # Clouds
    arcade.draw_arc_filled(x, y, 350, 300, arcade.color.LIGHT_GRAY, 0, 180)
    arcade.draw_arc_filled(x - 125, y, 150, 150, arcade.color.GHOST_WHITE, 0, 180)

def draw_p_backdrop():
    # Parthenon Backdrop
    arcade.draw_lrtb_rectangle_filled(245, 765, 600, 300, arcade.csscolor.DARK_GRAY)
    arcade.draw_lrtb_rectangle_filled(430, 580, 600, 300, arcade.csscolor.GRAY)
    arcade.draw_lrtb_rectangle_filled(470, 540, 450, 300, arcade.csscolor.DARK_SLATE_GRAY)

def draw_p_stairs():
    # Parthenon Stairs
    arcade.draw_lrtb_rectangle_filled(200, 810, 300, 290, arcade.csscolor.DARK_GRAY)
    arcade.draw_lrtb_rectangle_filled(215, 795, 310, 300, arcade.csscolor.GRAY)
    arcade.draw_lrtb_rectangle_filled(230, 780, 320, 310, arcade.csscolor.GAINSBORO)

def draw_p_column(x):
    # Parthenon Columns
    arcade.draw_lrtb_rectangle_filled(x, x + 30, 600, 320, arcade.color.LEMON_CHIFFON)
    arcade.draw_lrtb_rectangle_filled(x + 50, x + 80, 600, 320, arcade.color.LEMON_CHIFFON)
    arcade.draw_lrtb_rectangle_filled(x + 100, x + 130, 600, 320, arcade.color.LEMON_CHIFFON)
    arcade.draw_lrtb_rectangle_filled(x + 150, x + 180, 600, 320, arcade.color.LEMON_CHIFFON)
    arcade.draw_lrtb_rectangle_filled(x + 200, x + 230, 600, 320, arcade.color.LEMON_CHIFFON)

def draw_p_roof():
    # Parthenon Roof
    arcade.draw_triangle_filled(500, 750, 200, 600, 810, 600, arcade.csscolor.GAINSBORO)
    arcade.draw_triangle_filled(500, 720, 280, 615, 730, 615, arcade.csscolor.GRAY)
    arcade.draw_triangle_filled(500, 690, 375, 635, 645, 635, arcade.csscolor.DARK_SLATE_GRAY)

def main():
    arcade.open_window(screen_width, screen_height, "Parthenon")
    arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)
    arcade.start_render()

    #Grid
    draw_horizontal_grid(0, 0)
    draw_vertical_grid(0, 0)

    # Ground Base Color
    arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 0, arcade.csscolor.OLIVE_DRAB)

    # Ground Trail Color
    arcade.draw_polygon_filled(((300, 0),
                                (475, 300),
                                (525, 300),
                                (700, 0),
                                ),
                               arcade.csscolor.LIGHT_SLATE_GRAY)

    #Bushes
    draw_bushes(200, 300)
    draw_bushes(800, 300)

    #Clouds
    draw_clouds(800, 800)
    draw_clouds(150, 700)
    draw_clouds(980, 500)

    #Parthenon Backdrop
    draw_p_backdrop()

    #Stairway to Heaven
    draw_p_stairs()

    #Columns
    draw_p_column(240)
    draw_p_column(540)

    #Raise the Roof
    draw_p_roof()

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()

main()
