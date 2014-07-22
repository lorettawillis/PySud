__author__ = 'loretta'

import random


# Room of requirements.
class Room:
    # Constants
    FRONT_DOOR = 'front'
    RIGHT_DOOR = 'right'
    LEFT_DOOR  = 'left'
    BACK_DOOR  = 'back'
    DOORS      = (FRONT_DOOR, RIGHT_DOOR, LEFT_DOOR)

    # Class fields
    id = 0

    # Create a room and what is in it.
    def __init__(self):
        Room.id += 1
        # Object fields
        self.name = 'Room-' + str(Room.id)
        self.door_list = random.sample(Room.DOORS, random.randint(1, 3))
        self.door_list.append(Room.BACK_DOOR)

    # Enter room, describe it, ask for a user action, validate action, do action.
    def enter(self):
        which_door = raw_input('In ' + self.name + ', pick one of the following doors: ' +
                               ', '.join(self.door_list) + '. -> ')

        which_door_len = len(which_door)
        if which_door_len >= 1: which_door = which_door.strip()
        if which_door_len >= 1: which_door = which_door.lower()

        while which_door not in self.door_list:
            which_door = raw_input('Invalid choice, try again -> ')

        if which_door == self.BACK_DOOR:
            print 'Leaving ' + self.name + '.\n'
        else:
            print 'Going through', which_door, 'door.\n'
            room = Room()
            room.enter()
            self.enter()


#----------------------------------------------------------------------------------------------------------------------#
def main():
    room = Room()
    room.enter()
    print '\nBye!\n'

if __name__ == "__main__":
    main()
