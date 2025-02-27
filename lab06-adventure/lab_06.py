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
    room= Rooms('Estás en la habitación 0. Ves una puerta mirando al este.',None,None,1,None)
    room_list.append(room)
    room= Rooms('Estás en la habitación 1',5,None,2,None)
    room_list.append(room)
    room= Rooms('Estás en la habitación 2',None,None,None,1)
    room_list.append(room)
    room= Rooms('Estás en la habitación 3',None,None,4,None)
    room_list.append(room)
    room= Rooms('Estás en la habitación 4',None,None,5,4)
    room_list.append(room)
    room= Rooms('Estás en la habitación 5',9,1,6,4)
    room_list.append(room)
    room= Rooms('Estás en la habitación 6',None,None,7,5)
    room_list.append(room)
    room= Rooms('Estás en la habitación 7',None,None,None,6)
    room_list.append(room)
    room= Rooms('Estás en la habitación 8',None,None,9,None)
    room_list.append(room)
    room= Rooms('Estás en la habitación 9',None,5,10,8)
    room_list.append(room)
    room= Rooms('Estás en la habitación 10',None,None,None,9)
    room_list.append(room)

    current_room=0
    done=False
    while(done!=True):

        print(room_list[current_room].description)
        direccion=input("A qué dirección quieres ir?")
        print()
        if(direccion=='n'):
            next_room=room_list[current_room].north
            if(next_room==None):
                print("No puedes ir por ahí")
            else:
                current_room=next_room
        if (direccion == 's'):
            next_room = room_list[current_room].south
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        if (direccion == 'e'):
            next_room = room_list[current_room].east
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        if (direccion == 'w'):
            next_room = room_list[current_room].west
            if (next_room == None):
                print("No puedes ir por ahí")
            else:
                current_room = next_room
        else:
            "No entendí."

print(main())