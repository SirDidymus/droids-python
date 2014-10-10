#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
import random

class AI(BaseAI):
    """The class implementing gameplay logic."""
    @staticmethod
    def username():
        return "SirDidymus"

    @staticmethod
    def password():
        return "password"

    CLAW, ARCHER, REPAIRER, HACKER, TURRET, WALL, TERMINATOR, HANGAR = range(8)

    def spawn_units(self):
        if self.playerID == 0:
            x = 0
            y = random.randint(0, self.mapHeight - 1)
            variant = random.randint(0,7)
            self.players[self.playerID].orbitalDrop(x, y, variant)

        elif self.playerID == 1:  
            x = self.mapWidth - 1
            y = random.randint(0, self.mapHeight - 1)
            variant = random.randint(0,7)
            self.players[self.playerID].orbitalDrop(x, y, variant)
            
        return

    def move_units(self):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for droid in self.droids:
            # Attempt to move
            for _ in range(droid.maxMovement):
                movement = random.choice(direction)
                droid.move(droid.x + movement[0] , droid.y + movement[1])

        # if self.playerID == 0:
        # for droid in self.droids:
            # droid.move(droid.x + 1, droid.y)
            # print("Moved droid to ({}, {}).".format(droid.x, droid.y))

        # elif self.playerID == 1:
            # for droid in self.droids:
                # droid.move(droid.x - 1, droid.y)
                # print("Moved droid to ({}, {}).".format(droid.x, droid.y))
        
        return

    ##This function is called once, before your first turn
    def init(self):
        pass

    ##This function is called once, before your first turn
    def end(self):
        pass
    
    ##This function is called each time it is your turn
    ##Return true to end your turn, return false to ask the server for updated information
    def run(self):
            self.spawn_units()
            self.move_units()
            return 1

    def __init__(self, conn):
        BaseAI.__init__(self, conn)
