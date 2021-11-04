import random
import arcade

MOVEMENT_SPEED = 4
SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_STAR = 0.8
STAR_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

        self.set_mouse_visible(False)

        self.player_list = None
        self.star_list = None

        self.player_sprite = None
        self.score = 0

        arcade.set_background_color((77, 0, 77))

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()

        self.score = 0

        self.position_y += self.change_y
        self.position_x += self.change_x

        self.player_sprite = arcade.Sprite("xwing.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(STAR_COUNT):
            star = arcade.Sprite("star_small.png", SPRITE_SCALING_STAR)

            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)

            self.star_list.append(star)

    def on_draw(self):

        arcade.start_render()
        self.star_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):

        self.star_list.update()
        self.player_sprite.update()

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.star_list)

        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()