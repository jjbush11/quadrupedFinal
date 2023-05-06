import pybullet as p

class WORLD:
    def __init__(self, solutionID):
        self.myID = solutionID
        self.planeId = p.loadURDF("plane.urdf") #sets floor
        # try:
        #     p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
        # except: 
        #     p.loadSDF("defaultWorld.sdf")
        
        p.loadSDF("world"+str(self.myID)+".sdf") #tells pybullet to read in the world described box.sdf

        