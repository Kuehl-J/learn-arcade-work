import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    def __init__(self, position_x,
                 position_y,
                 change_x,
                 change_y,
                 radius,
                 color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.ball_x = 50
        self.ball_y = 50


    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.ball_x, self.ball_y, 15, arcade.color.AUBURN)

    def on_update(self, delta_time):
        self.ball_x += 1

def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing example")
    arcade.run()



main()