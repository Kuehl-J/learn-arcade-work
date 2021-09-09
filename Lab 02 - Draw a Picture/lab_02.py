# Athens Parthenon Recreation

import arcade

arcade.open_window(1000, 1000, "Parthenon")

# Background Color
arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

# Ready to Draw
arcade.start_render()

# Ground Base Color
arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 0, arcade.csscolor.OLIVE_DRAB)

# Ground Trail Color
arcade.draw_polygon_filled(((300, 0),
                            (475, 300),
                            (525, 300),
                            (700, 0),
                            ),
                            arcade.csscolor.LIGHT_SLATE_GRAY)

# # Grid Layout
# arcade.draw_line(100, 0, 100, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(200, 0, 200, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(300, 0, 300, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(400, 0, 400, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(500, 0, 500, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(600, 0, 600, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(700, 0, 700, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(800, 0, 800, 1000, arcade.csscolor.BLACK)
# arcade.draw_line(900, 0, 900, 1000, arcade.csscolor.BLACK)
#
# arcade.draw_line(0, 100, 1000, 100, arcade.csscolor.BLACK)
# arcade.draw_line(0, 200, 1000, 200, arcade.csscolor.BLACK)
# arcade.draw_line(0, 300, 1000, 300, arcade.csscolor.BLACK)
# arcade.draw_line(0, 400, 1000, 400, arcade.csscolor.BLACK)
# arcade.draw_line(0, 500, 1000, 500, arcade.csscolor.BLACK)
# arcade.draw_line(0, 600, 1000, 600, arcade.csscolor.BLACK)
# arcade.draw_line(0, 700, 1000, 700, arcade.csscolor.BLACK)
# arcade.draw_line(0, 800, 1000, 800, arcade.csscolor.BLACK)
# arcade.draw_line(0, 900, 1000, 900, arcade.csscolor.BLACK)

# Background Bushes Left
arcade.draw_arc_filled(100, 300, 250, 250, arcade.color.ARMY_GREEN, 0, 180)
arcade.draw_arc_filled(175, 300, 300, 300, arcade.color.DARK_OLIVE_GREEN, 0, 180)
arcade.draw_arc_filled(350, 300, 200, 250, arcade.color.ARMY_GREEN, 0, 180)
arcade.draw_arc_filled(175, 300, 200, 200, arcade.color.DARK_GREEN, 0, 180)
arcade.draw_arc_filled(175, 300, 300, 300, arcade.color.DARK_OLIVE_GREEN, 0, 180)

# Background Bushes Right
arcade.draw_arc_filled(875, 300, 300, 300, arcade.color.DARK_OLIVE_GREEN, 0, 180)
arcade.draw_arc_filled(775, 300, 200, 250, arcade.color.ARMY_GREEN, 0, 180)
arcade.draw_arc_filled(675, 300, 150, 200, arcade.color.DARK_OLIVE_GREEN, 0, 180)

# Clouds
arcade.draw_arc_filled(115, 715, 550, 300, arcade.color.LIGHT_GRAY, 0, 180)
arcade.draw_arc_filled(100, 700, 550, 300, arcade.color.GHOST_WHITE, 0, 180)
arcade.draw_arc_filled(900, 800, 350, 300, arcade.color.LIGHT_GRAY, 0, 180)
arcade.draw_arc_filled(780, 800, 150, 150, arcade.color.GHOST_WHITE, 0, 180)


# Pantheon Backdrop
arcade.draw_lrtb_rectangle_filled(245, 765, 600, 300, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(430, 580, 600, 300, arcade.csscolor.GRAY)
arcade.draw_lrtb_rectangle_filled(470, 540, 450, 300, arcade.csscolor.DARK_SLATE_GRAY)

# Pantheon Stairs
arcade.draw_lrtb_rectangle_filled(200, 810, 300, 290, arcade.csscolor.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(215, 795, 310, 300, arcade.csscolor.GRAY)
arcade.draw_lrtb_rectangle_filled(230, 780, 320, 310, arcade.csscolor.GAINSBORO)

# Pantheon Columns
arcade.draw_lrtb_rectangle_filled(240, 270, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(290, 320, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(340, 370, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(390, 420, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(440, 470, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(540, 570, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(590, 620, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(640, 670, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(690, 720, 600, 320, arcade.color.LEMON_CHIFFON)
arcade.draw_lrtb_rectangle_filled(740, 770, 600, 320, arcade.color.LEMON_CHIFFON)

# Pantheon Roof
arcade.draw_triangle_filled(500, 750, 200, 600, 810, 600, arcade.csscolor.GAINSBORO)
arcade.draw_triangle_filled(500, 720, 280, 615, 730, 615, arcade.csscolor.GRAY)
arcade.draw_triangle_filled(500, 690, 375, 635, 645, 635, arcade.csscolor.DARK_SLATE_GRAY)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()