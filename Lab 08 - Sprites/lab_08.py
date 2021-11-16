import random
import arcade


MOVEMENT_SPEED = 4
SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_STAR = 0.8
SPRITE_SCALING_METEOR = 0.7
METEOR_COUNT = 15
STAR_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Star(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()

class Meteor(arcade.Sprite):

    def __init__(self, filename, sprite_scaling, position_x, position_y, change_x, change_y, radius, color):

        super().__init__(filename, sprite_scaling)

        # self.change_x = 0
        # self.change_y = 0

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def update(self):


        self.center_x += self.change_x
        self.center_y += self.change_y


        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")


        self.set_mouse_visible(False)

        self.player_list = None
        self.star_list = None
        self.meteor_list = None

        self.player_sprite = None
        self.score = 0

        self.ff_sound = arcade.load_sound("force_field_1.ogg")
        self.impact_sound = arcade.load_sound("impact_1.ogg")

        arcade.set_background_color((77, 0, 77))

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.star_list = arcade.SpriteList()
        self.meteor_list = arcade.SpriteList()

        self.score = 0


        # self.position_y += self.change_y
        # self.position_x += self.change_x

        self.player_sprite = arcade.Sprite("xwing.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(STAR_COUNT):
            star = arcade.Sprite("star_small.png", SPRITE_SCALING_STAR)

            star = Star("star_small.png", SPRITE_SCALING_STAR)

            star.center_x = random.randrange(SCREEN_WIDTH)
            star.center_y = random.randrange(SCREEN_HEIGHT)

            self.star_list.append(star)


        for i in range(METEOR_COUNT):
            meteor = arcade.Sprite("meteor_one.png", SPRITE_SCALING_METEOR)

            meteor = Meteor("meteor_one.png", SPRITE_SCALING_METEOR, 5, 7, -3, -1, 0.5, arcade.color.ORANGE)

            meteor.center_x = random.randrange(SCREEN_WIDTH)
            meteor.center_y = random.randrange(SCREEN_HEIGHT)
            meteor.change_x = random.randrange(-3, 4)

            meteor.change_y = random.randrange(-3, 4)

            self.meteor_list.append(meteor)

    def on_draw(self):

        arcade.start_render()
        self.star_list.draw()
        self.meteor_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.star_list) == 0:
            arcade.draw_text("Game Over", 300, 400, arcade.color.WHITE, 75)

    def update(self, delta_time):

        if len(self.star_list) > 0:

            self.star_list.update()
            self.meteor_list.update()
            self.player_sprite.update()

        if self.player_sprite.left < 0:
            self.player_sprite.left = 0

        if self.player_sprite.right > SCREEN_WIDTH:
            self.player_sprite.right = SCREEN_WIDTH

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0

        if self.player_sprite.top > SCREEN_HEIGHT:
            self.player_sprite.top = SCREEN_HEIGHT


        star_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.star_list)

        meteor_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                             self.meteor_list)

        for star in star_hit_list:
            star.remove_from_sprite_lists()
            self.score += 1

            arcade.play_sound(self.ff_sound)

        for meteor in meteor_hit_list:
            meteor.remove_from_sprite_lists()
            self.score -= 1

            arcade.play_sound(self.impact_sound)

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