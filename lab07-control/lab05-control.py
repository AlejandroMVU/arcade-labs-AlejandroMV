""" Lab 7 - User Control """
import random
import arcade
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

class ovni:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    def draw(self):
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 150, 75, arcade.color.GRAY)
        arcade.draw_ellipse_filled(self.position_x, self.position_y + 30, 75, 35, arcade.color.ANDROID_GREEN)
        arcade.draw_circle_filled(self.position_x, self.position_y - 10, 5, arcade.color.BLUE)
        arcade.draw_circle_filled(self.position_x - 25, self.position_y - 10, 5, arcade.color.RED)
        arcade.draw_circle_filled(self.position_x + 25, self.position_y - 10, 5, arcade.color.YELLOW)
        arcade.draw_circle_filled(self.position_x + 45, self.position_y - 3, 5, arcade.color.PURPLE)
        arcade.draw_circle_filled(self.position_x - 45, self.position_y - 3, 5, arcade.color.GO_GREEN)

class vaca:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.vaca = arcade.load_texture('lab08-sprites/Vaca.png')
    def draw(self):

        arcade.draw_texture_rectangle(self.position_x, self.position_y, 50, 50, self.vaca )


def arbol(x, y):
    arcade.draw_rectangle_filled(x, y, 50, 300, arcade.color.ROSEWOOD)
    # arcade.draw_triangle_filled(300,250,500,250,400,500,arcade.color.DARK_GREEN)
    # arcade.draw_triangle_filled(325,350,475,350,400,600,arcade.color.DARK_GREEN)
    # arcade.draw_triangle_filled(340,450,460,450,400,700,arcade.color.DARK_GREEN)

    arcade.draw_triangle_filled(x - 100, y, x + 100, y, x, y + 250, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 75, y + 100, x + 75, y + 100, x, y + 350, arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x - 60, y + 200, x + 60, y + 200, x, y + 450, arcade.color.DARK_GREEN)


def flor(x_f, y_f):
    arcade.draw_rectangle_filled(x_f, y_f, 5, 15, arcade.color.GUPPIE_GREEN)
    arcade.draw_circle_filled(x_f - 4, y_f + 10, 5, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f, y_f + 14, 5, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f, y_f + 6, 5, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f + 4, y_f + 10, 5, arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f, y_f + 10, 5, arcade.color.YELLOW_ROSE)





# Estrellas:
def estrellas(numero_estrellas):
    for i in range(numero_estrellas):
        x = random.randrange(800)
        y = random.randrange(700)
        x1 = random.randrange(3, 7)
        brillo = random.randrange(100, 255)
        color = (brillo, brillo, brillo)
        arcade.draw_rectangle_filled(x, y, x1, x1, color, 45)

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        self.ovni=ovni(300,300)
        self.vaca=vaca(300,300)

    def on_draw(self):
        arcade.set_background_color(arcade.color.DARK_BLUE)

        estrellas(65)

        # LUNA:
        arcade.draw_circle_filled(200, 550, 100, arcade.color.GHOST_WHITE)
        arcade.draw_circle_filled(250, 600, 100, arcade.color.DARK_BLUE)

        # COLINA:

        arcade.draw_circle_filled(100, -225, 400, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(700, -225, 400, arcade.color.DARK_GREEN)
        arcade.draw_circle_filled(400, -350, 500, arcade.color.GREEN_YELLOW)

        arbol(400, 250)

        # FLORES
        #for i in range(25):
        #    x_flor = random.randrange(200, 600)
        #    y_flor = random.randrange(0, 90)
        #    flor(x_flor, y_flor)
        self.vaca.draw()
        self.ovni.draw()
        arcade.finish_render()
        self.clear()

    def on_mouse_motion(self, x, y, dx, dy):
        self.ovni.position_x= x
        self.ovni.position_y= y

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.LEFT:
            self.vaca.position_x-=1
        if symbol == arcade.key.RIGHT:
            self.vaca.position_x+=1
        if symbol == arcade.key.UP:
            self.vaca.position_y+=1
        if symbol == arcade.key.DOWN:
            self.vaca.position_y-=1
def main():
    window = MyGame()
    arcade.run()


main()