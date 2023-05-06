import pybullet as p
import pyrosim.pyrosim as pyrosim 
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:
    def __init__(self, solutionID):
        self.myID = solutionID
        self.robotID = p.loadURDF("body"+str(self.myID)+".urdf") #sets floor
        # try:
        #    self.robotID = p.loadURDF("body"+str(self.myID)+".urdf") #sets floor  
        # except:
        #     print("\n nooooooooo \n")
        #     self.robotID=p.loadURDF("bodyTwo.urdf")
            # self.robotID=p.loadURDF("defaultBody.urdf")
        # self.robotID = p.loadURDF("body.urdf") #sets floor  
        pyrosim.Prepare_To_Simulate(self.robotID) #does more setting up
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(self.myID)+".nndf")

        os.system("del brain"+str(self.myID)+".nndf")
        os.system("del body"+str(self.myID)+".urdf")
        os.system("del world"+str(self.myID)+".sdf")

    def Prepare_To_Sense(self):
        self.sensors=dict()
        for linkName in pyrosim.linkNamesToIndices:
             #returns instance of sensor, stored in in dictoionary 
            self.sensors[linkName] = SENSOR(linkName) 

    
    def Sense(self,x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)
        
    def Prepare_To_Act(self):
        self.motors=dict()
        for jointName in pyrosim.jointNamesToIndices:
            #returns instance of motor, stored in in dictoionary 
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,x):
    #p.setCollisionFilterGroupMask(self.robotID, -1, 0, 0)
    # p.setCollisionFilterPair(self.robotID, self.robotID, 1, 1)
    # p.changeDynamics(self.robotID, -1, lateralFriction=0.5, restitution=0.0)

        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = bytes(self.nn.Get_Motor_Neurons_Joint(neuronName), 'utf-8')
                # jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName].Set_Value(self.robotID, desiredAngle)
                
    
    def Think(self):
        self.nn.Update()
        
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID,0)
        robotVelocity = p.getBaseVelocity(self.robotID)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        velocityOfX = robotVelocity[0][0]

        fitnessFunc = xCoordinateOfLinkZero*c.weightOfDistance + velocityOfX*c.weightOfDistance

        inFile = open("tmp"+str(self.myID)+".txt", "w")
        inFile.write(str(fitnessFunc))
        # os.rename("tmp"+str(self.myID)+".txt" , "fitness"+str(self.myID)+".txt")
        # inFile = open("fitness"+str(self.myID)+".txt", "w")
        inFile.close()
        os.system("ren tmp"+str(self.myID)+".txt " "fitness"+str(self.myID)+".txt")
        # os.chmod("fitness"+str(self.myID)+".txt", stat.S_IRWXO)
        # os.rename("tmp"+str(self.myID)+".txt" , "fitness"+str(self.myID)+".txt")
        
        
            