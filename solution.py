import numpy
import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
import constants as c
import os
import random
import time


class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) 
        self.weights = self.weights * 2 -1

    # def Evaluate(self, directOrGui):
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()

    #     os.system("start /B python3 simulate.py " + directOrGui + " "+str(self.myID))

    #     while not os.path.exists("fitness"+str(self.myID)+".txt"):
    #         time.sleep(0.01)
    #     inFile = open("fitness"+str(self.myID)+".txt", "r")
    #     self.fitness = float(inFile.read())
    #     print(self.fitness)
    #     inFile.close()

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("start /B python3 simulate.py " + directOrGui + " "+str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        inFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(inFile.read())
        inFile.close()

        os.system("del fitness"+str(self.myID)+".txt")
        
    def Create_World(self):
        # while not os.path.exists("world"+str(self.myID)+".sdf"):
        #     print("waiting for world")
        #     time.sleep(0.01)
        pyrosim.Start_SDF("world"+str(self.myID)+".sdf") #tells pyrosim name of file where info about the world should be stored
        
        # pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[c.length,c.width,c.height]) #creates box with initial size and positons 

        pyrosim.End() #closes sdf file

    def Create_Body(self):
        # while not os.path.exists("body.urdf"):
        #     print("waiting for body")
        #     time.sleep(0.01)

        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        # pyrosim.Start_URDF("body.urdf")
        # pyrosim.Start_URDF("bodyTwo.urdf")

        # torso and upper leg
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length,2,c.height]) #creates box with initial size and positons 

        # Middle Left side 
        pyrosim.Send_Joint( name = "Torso_MiddleLeftLeg" , parent= "Torso" , child = "MiddleLeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # Middle Right Side (Side closer to camera)
        pyrosim.Send_Joint( name = "Torso_MiddleRightLeg" , parent= "Torso" , child = "MiddleRightLeg" , type = "revolute", position = [.5,0,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="MiddleRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Upper Front Leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        # Upper Back Leg
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        # Lower Left Side Leg
        pyrosim.Send_Joint( name = "MiddleLeftLeg_LowerLeftLeg" , parent= "MiddleLeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower Right Side Leg 
        pyrosim.Send_Joint( name = "MiddleRightLeg_LowerRightLeg" , parent= "MiddleRightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower Front Leg    
        pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,.5,0] , size=[.2,1,.2]) #creates box with initial size and positons
     
        # Lower Back Leg
        pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,-.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        pyrosim.End()   

    def Create_Brain(self):
        # while not os.path.exists("brain"+str(self.myID)+".nndf"):
        #     time.sleep(0.01)
            
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")


        pyrosim.Send_Sensor_Neuron(name=0 , linkName = "LowerLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=1 , linkName = "LowerRightLeg")
        pyrosim.Send_Sensor_Neuron(name=2 , linkName = "LowerFrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3 , linkName = "LowerBackLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_MiddleRightLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "MiddleLeftLeg_LowerLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "MiddleRightLeg_LowerRightLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "FrontLeg_LowerFrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "BackLeg_LowerBackLeg")

        # pyrosim.Send_Motor_Neuron( name = 14 , jointName = "MiddleLeftLeg_middleLeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 15 , jointName = "BackLeftLeg_backLeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = 16 , jointName = "FrontLeftLeg_frontLeftLowerLeg")

        for currentRow in range (c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID



