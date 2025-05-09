import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Game Framework"

PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        arcade.set_background_color(arcade.color.PURPLE_MOUNTAIN_MAJESTY)
        
        self.player = None
        self.wall = None
        
        self.player_list = None
        self.wall_list = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player = arcade.SpriteSolidColor(50, 50, arcade.color.BLUE_SAPPHIRE)
        self.player.center_x = 100
        self.player.center_y = 100
        self.player_list.append(self.player)

        self.wall = arcade.SpriteSolidColor(200, 50, arcade.color.RED)
        self.wall.center_x = 400
        self.wall.center_y = 300
        self.wall_list.append(self.wall)

    def on_draw(self):
        self.clear()

        self.wall_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player.update()

        # Check for collision with wall
        if arcade.check_for_collision_with_list(self.player, self.wall_list):
            # Push the player back if colliding
            if self.player.change_x > 0:  # Moving right
                self.player.right = self.wall.left
            if self.player.change_x < 0:  # Moving left
                self.player.left = self.wall.right
            if self.player.change_y > 0:  # Moving up
                self.player.top = self.wall.bottom
            if self.player.change_y < 0:  # Moving down
                self.player.bottom = self.wall.top

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

def main():
    game = MyGame()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
