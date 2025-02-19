import arcade
import random
arcade.open_window(800, 700, "Drawing Example")

arcade.set_background_color(arcade.color.DARK_BLUE)


arcade.start_render()

#Estrellas:
arcade.draw_rectangle_filled(300,300,5,5,arcade.color.WHITE_SMOKE,45)
for i in range(50):
    x =random.randrange(800)
    y =random.randrange(700)
    x1=random.randrange(3,7)

    arcade.draw_rectangle_filled(x,y,x1,x1,arcade.color.WHITE_SMOKE,45)

#COLINA:
arcade.draw_circle_filled(400,-350,500,arcade.color.GREEN_YELLOW)

#ARBOL:
arcade.draw_rectangle_filled(400,250,50,300,arcade.color.ROSEWOOD)
arcade.draw_triangle_filled(300,250,500,250,400,500,arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(325,350,475,350,400,600,arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(340,450,460,450,400,700,arcade.color.DARK_GREEN)

#LUNA:
arcade.draw_circle_filled(200,550,100,arcade.color.GHOST_WHITE)
arcade.draw_circle_filled(250,600,100,arcade.color.DARK_BLUE)
# Keep the window up until someone closes it.

#BICICLETA:
arcade.draw_circle_outline(650,400,15,arcade.color.BLACK)
arcade.draw_circle_outline(700,400,15,arcade.color.BLACK)

arcade.draw_line(685, 400,715,400,arcade.color.BLACK )
arcade.draw_line(700, 385,700,415,arcade.color.BLACK )
arcade.draw_line(700, 385,700,425,arcade.color.BLACK )

arcade.draw_line(635, 400,665,400,arcade.color.BLACK )
arcade.draw_line(650, 415,650,385,arcade.color.BLACK )
arcade.draw_line(650, 425,650,385,arcade.color.BLACK )

arcade.draw_triangle_outline(650,425 ,700, 425, 675 , 400 ,arcade.color.BLACK)
arcade.draw_line(650, 425,640,435,arcade.color.BLACK )
arcade.draw_line(630, 435,650,435,arcade.color.BLACK )
arcade.draw_line(700, 385,700,430,arcade.color.BLACK )
arcade.draw_ellipse_filled(700,430,15,5,arcade.color.BLACK)

arcade.finish_render()

arcade.run()

