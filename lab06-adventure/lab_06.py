from ftplib import print_line


class Rooms:
    def __init__(self,description,north,south,east,west):
        self.description = description
        self.north = north
        self.south= south
        self.east=  east
        self.west=  west

def main():
    room_list=[]
    room= Rooms('Estás en un dormitorio. Ves una puerta mirando al este.',None,None,1,None)
    room_list.append(room)
    room= Rooms('Estás en una habitación que se se conecta en forma de pasillo en dirección norte. Ves una puerta hacia el este.',5,None,2,None)
    room_list.append(room)
    room= Rooms('Estás en un baño. Ves una puerta hacia el oeste.',None,None,None,1)
    room_list.append(room)
    room= Rooms('Estás en un balcón, puedes ver la calle. Ves el regreso al interior hacia el este.',None,None,4,None)
    room_list.append(room)
    room= Rooms('Estás en un dormitorio. Ves una entrada hacia el balcón al oeste y una puerta al este.',None,None,5,4)
    room_list.append(room)
    room= Rooms('Estás en una habitación que se conecta en forma de pasillo hacia el norte y hacia el sur. Ves 2 puertas, en el este y el oeste',9,1,6,4)
    room_list.append(room)
    room= Rooms('Estás en la cocina. Ves una puerta hacia el oeste y una entrada al jardín al este.',None,None,7,5)
    room_list.append(room)
    room= Rooms('Estás en un jardín interior. Ves una puerta hacia el oeste.',None,None,None,6)
    room_list.append(room)
    room= Rooms('Estás en un dormitorio. Ves una puerta hacia el este',None,None,9,None)
    room_list.append(room)
    room= Rooms('Estás en una habitación que se conecta en forma de pasillo hacia el sur. Ves 2 puertas, hacia el este y el oeste.',None,5,10,8)
    room_list.append(room)
    room= Rooms('Estás en un comedor. Ves una puerta hacia el oeste.',None,None,None,9)
    room_list.append(room)

    current_room=0
    done=False
    while(done!=True):

        print(room_list[current_room].description)
        direccion=input("En qué dirección quieres ir? \n")

        if(direccion.lower()=='n' or direccion.lower()=='north' or direccion.lower()=='norte'):
            next_room=room_list[current_room].north
            if(next_room==None):
                print("No puedes ir por ahí")
            else:
                current_room=next_room
        elif (direccion.lower() == 's' or direccion.lower()=='south' or direccion.lower()=='sur'):
            next_room = room_list[current_room].south
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        elif (direccion.lower() == 'e' or direccion.lower()=='east' or direccion.lower()=='este'):
            next_room = room_list[current_room].east
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        elif (direccion.lower() == 'w' or direccion.lower()=='west' or direccion.lower()=='oeste'):
            next_room = room_list[current_room].west
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        else:
            "No entendí."

print(main())