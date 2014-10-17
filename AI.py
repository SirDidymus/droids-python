#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
import random
import cache

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
            variant = random.randint(0,1)
            self.players[self.playerID].orbitalDrop(x, y, variant)

        elif self.playerID == 1:  
            x = self.mapWidth - 1
            y = random.randint(0, self.mapHeight - 1)
            variant = random.randint(0,1)
            self.players[self.playerID].orbitalDrop(x, y, variant)
            
        return

    def move_units(self):
        kill_this = self.findEnemyHanger()
        
        for droid in self.droids:
            if droid.owner == self.playerID:
                moveTo(droid, kill_this.x, kill_this.y)
                droid.operate(self, kill_this.x, kill_this.y)
        
        return
    
    def findEnemyHangar(self):
        for droid in self.droids:
            if droid.playerID == self.playerID^1 and droid.variant == self.HANGAR:
                return droid
        return None
                
    
    def moveRight(droid):
        droid.move(droid.x + 1, droid.y)
        
    def moveLeft(droid):
        droid.move(droid.x - 1, droid.y)
        
    def moveUp(droid):
        droid.move(droid.x, droid.y - 1)

    def moveDown(droid):
        droid.move(droid.x, droid.y + 1)

    def moveTo(self, droid, x, y):  
        for _ in range(droid.maxMovement):
            if droid.x < x:
                moveRight(droid)
            elif droid.x > x:
                moveLeft(droid)
            elif droid.y < y:
                moveDown(droid)
            elif droid.y > y:
                moveUp(droid)
                                    
    
    ##This function is called once, before your first turn
    def init(self):
        self.Cache = cache.cache
        pass

    ##This function is called once, before your first turn
    def end(self):
        pass
    
    ##This function is called each time it is your turn
    ##Return true to end your turn, return false to ask the server for updated information
    def run(self):
        self.Cache.update_droids()
        self.spawn_units()
        self.move_units()

        return 1

    def __init__(self, conn):
        BaseAI.__init__(self, conn)
