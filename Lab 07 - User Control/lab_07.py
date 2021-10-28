import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5

def draw_trees(x, y):
    arcade.draw_lrtb_rectangle_filled(x, x + 35, y + 50, y, arcade.color.BISTRE)
    arcade.draw_triangle_filled(x - 40, y + 50,
                                x + 75, y + 50,
                                x + 17, y + 200, arcade.color.FOREST_GREEN)


class Fairy:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.radius = radius
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        arcade.draw_triangle_filled(self.position_x + 10, self.position_y + 5,
                                    self.position_x + 30, self.position_y + 40,
                                    self.position_x + 30, self.position_y + 10, arcade.color.BEAU_BLUE)
        arcade.draw_triangle_filled(self.position_x + 10, self.position_y,
                                    self.position_x + 27, self.position_y - 3,
                                    self.position_x + 27, self.position_y - 23, arcade.color.BEAU_BLUE)
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y + 5,
                                    self.position_x - 30, self.position_y + 40,
                                    self.position_x - 30, self.position_y + 10, arcade.color.BEAU_BLUE)
        arcade.draw_triangle_filled(self.position_x - 10, self.position_y,
                                    self.position_x - 27, self.position_y - 3,
                                    self.position_x - 27, self.position_y - 23, arcade.color.BEAU_BLUE)
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

class Bird:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.radius = radius
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y

        self.wall_bump = arcade.load_sound("fall1.wav")
        self.fall1_sound_player = None

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, arcade.color.CARDINAL)
        arcade.draw_triangle_filled(self.position_x + 40, self.position_y + 45,
                                    self.position_x + 60, self.position_y + 20,
                                    self.position_x + 40, self.position_y + 15, arcade.color.BANANA_MANIA)
        arcade.draw_circle_filled(self.position_x + 30, self.position_y + 30, 20, arcade.color.CARDINAL)
        arcade.draw_circle_filled(self.position_x + 35, self.position_y + 35, 6, arcade.color.WHITE)
        arcade.draw_circle_filled(self.position_x + 36, self.position_y + 34, 3, arcade.color.BLACK)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < self.radius:
            self.position_x = self.radius
            arcade.play_sound(self.wall_bump)

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            arcade.play_sound(self.wall_bump)

        if self.position_y < self.radius:
            self.position_y = self.radius
            arcade.play_sound(self.wall_bump)

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            arcade.play_sound(self.wall_bump)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        self.mouse_click_sound = arcade.load_sound("explosion1.flac")
        self.explosion1_sound_player = None
        arcade.set_background_color(arcade.color.HUNTER_GREEN)

        self.fairy = Fairy(400, 300, 0, 0, 15, arcade.color.BABY_BLUE_EYES)
        self.bird = Bird(50, 50, 0, 0, 30, arcade.color.BANANA_MANIA)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.mouse_click_sound)

    def on_mouse_motion(self, x, y, dx, dy):
        self.fairy.position_x = x
        self.fairy.position_y = y

    def update(self, delta_time):
        self.bird.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.bird.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.bird.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP or key == arcade.key.W:
            self.bird.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.bird.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT or key == arcade.key.A or key == arcade.key.D:
            self.bird.change_x = 0
        if key == arcade.key.UP or key == arcade.key.DOWN or key == arcade.key.W or key == arcade.key.S:
            self.bird.change_y = 0


    def on_draw(self):
        arcade.start_render()

        draw_trees(100, 100)
        draw_trees(650, 75)
        draw_trees(480, 30)
        draw_trees(240, 430)
        draw_trees(700, 370)
        draw_trees(50, 330)

        self.fairy.draw()

        self.bird.draw()

def main():
    window = MyGame()
    arcade.run()


main()