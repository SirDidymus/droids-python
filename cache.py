class cache:    
    enemy_hangars = []
    enemy_droids = []
    my_droids = []
    
    ai = None
    
    def __init__(self, ai):
        self.ai = ai
        self.clean_droids()
        
    def clean_droids(self):
        self.my_droids = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]
        self.enemy_droids = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]
        self.enemy_hangars = [[None for _ in range(self.ai.mapHeight)] for _ in range(self.ai.mapWidth)]

    def update_droids(self):
        self.clean_droids()
        
        for droid in self.ai.droids:
            if droid.owner == self.ai.playerID:
                self.my_droids[droid.x][droid.y] = droid
            elif droid.owner == self.ai.playerID^1:
                self.enemy_droids[droid.x][droid.y] = droid
                
                if droid.variant == self.ai.HANGAR:
                    self.enemy_hangars[droid.x][droid.y] = droid
                    
            else:
                print("You should never see this statement!")