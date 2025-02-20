import arcade
import random
arcade.open_window(800, 700, "Drawing Example")

arcade.set_background_color(arcade.color.DARK_BLUE)


arcade.start_render()
#ARBOL:
def arbol(x,y):
    arcade.draw_rectangle_filled(x,y,50,300,arcade.color.ROSEWOOD)
    #arcade.draw_triangle_filled(300,250,500,250,400,500,arcade.color.DARK_GREEN)
    #arcade.draw_triangle_filled(325,350,475,350,400,600,arcade.color.DARK_GREEN)
    #arcade.draw_triangle_filled(340,450,460,450,400,700,arcade.color.DARK_GREEN)

    arcade.draw_triangle_filled(x-100,y,x+100,y,x,y+250,arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x-75,y+100,x+75,y+100,x,y+350,arcade.color.DARK_GREEN)
    arcade.draw_triangle_filled(x-60,y+200,x+60,y+200,x,y+450,arcade.color.DARK_GREEN)

def flor(x_f,y_f):
    arcade.draw_rectangle_filled(x_f,y_f,5,15,arcade.color.GUPPIE_GREEN)
    arcade.draw_circle_filled(x_f-4,y_f+10,5,arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f,y_f+14,5,arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f,y_f+6,5,arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f+4,y_f+10,5,arcade.color.PINK_LACE)
    arcade.draw_circle_filled(x_f,y_f+10,5,arcade.color.YELLOW_ROSE)





#Estrellas:
def estrellas(numero_estrellas):
    for i in range(numero_estrellas):
        x =random.randrange(800)
        y =random.randrange(700)
        x1=random.randrange(3,7)
        brillo=random.randrange(100,255)
        color=(brillo,brillo,brillo)
        arcade.draw_rectangle_filled(x,y,x1,x1,color,45)

estrellas(65)

#LUNA:
arcade.draw_circle_filled(200,550,100,arcade.color.GHOST_WHITE)
arcade.draw_circle_filled(250,600,100,arcade.color.DARK_BLUE)


#COLINA:
arcade.draw_circle_filled(400,-350,500,arcade.color.GREEN_YELLOW)

arbol(400,250)

#FLORES
for i in range (25):
    x_flor=random.randrange(200,600)
    y_flor=random.randrange(0,90)
    flor(x_flor,y_flor)








#BICICLETA:
#ruedas
arcade.draw_circle_outline(650,400,15,arcade.color.BLACK)
arcade.draw_circle_outline(700,400,15,arcade.color.BLACK)
#lineas en ruedas
arcade.draw_line(685, 400,715,400,arcade.color.BLACK )
arcade.draw_line(700, 385,700,415,arcade.color.BLACK )
arcade.draw_line(700, 385,700,425,arcade.color.BLACK )

arcade.draw_line(635, 400,665,400,arcade.color.BLACK )
arcade.draw_line(650, 415,650,385,arcade.color.BLACK )
arcade.draw_line(650, 425,650,385,arcade.color.BLACK )
#manillar etc.
arcade.draw_triangle_outline(650,425 ,700, 425, 675 , 400 ,arcade.color.BLACK)
arcade.draw_line(650, 425,640,435,arcade.color.BLACK )
arcade.draw_line(630, 435,650,435,arcade.color.BLACK )
arcade.draw_line(700, 385,700,430,arcade.color.BLACK )
arcade.draw_ellipse_filled(700,430,15,5,arcade.color.BLACK)


#ET el extraterrestre del dedo mas feo que un recien nacido arrugado
texture = arcade.load_texture("ET1.png")
arcade.draw_texture_rectangle(700,450,75,75,texture)




arcade.finish_render()

arcade.run()

