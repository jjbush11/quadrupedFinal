from world import WORLD
from robot import ROBOT
from sensor import SENSOR
import pybullet_data #allows for use of plane.urdf
import pybullet as p
import pyrosim.pyrosim as pyrosim 
import constants as c
import numpy
import time

class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        self.directOrGui = directOrGui
        if (directOrGui == "direct" or directOrGui == "DIRECT"):
            self.physicsClient = p.connect(p.DIRECT) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) #something to do with floor
        p.setGravity(0,0,c.gravity) #sets gravity 
        self.world = WORLD(solutionID)
        self.robotID = ROBOT(solutionID)
    
    def Run(self):
        for x in range(c.loop):
            p.stepSimulation() #sets the physics inside the world for a small amount of time
            self.robotID.Sense(x)
            self.robotID.Think()
            self.robotID.Act(x)
            if (self.directOrGui == "GUI" or self.directOrGui == "gui"):
                time.sleep(1/5000)
    
    def Get_Fitness(self):
        self.robotID.Get_Fitness()
        
    def __del__(self):
        p.disconnect()




