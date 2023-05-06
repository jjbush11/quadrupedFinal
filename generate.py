import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
#alters what is in the world
import random
#pos (x,y,z)
length =1
width=1
height=1

def Create_World():
    pyrosim.Start_SDF("world.sdf") #tells pyrosim name of file where info about the world should be stored
    # pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[length,width,height]) #creates box with initial size and positons 
    pyrosim.End() #closes sdf file

# def Create_Robot():
#     pass

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[length,width,height]) #creates box with initial size and positons 
    pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-.5,0,-.5] , size=[length,width,height]) #creates box with initial size and positons 
    pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height]) #creates box with initial size and positons

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName = "BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName = "FrontLeg")

    pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
    pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

    # pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 2.0 )
    # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 2.0 ) #connects sensors 1 to motor 3 
    # pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 2.0 ) 
    # pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 2.0 ) 

    for senseName in range (3):
        for motorName in range(3,5):
            pyrosim.Send_Synapse( sourceNeuronName = senseName , targetNeuronName = motorName , weight = random.randrange(-1,1))



    pyrosim.End()



Create_World()
Generate_Body()
Generate_Brain()
# Create_Robot()

    # pyrosim.Send_Cube(name="Link0", pos=[0,0,.5] , size=[length,width,height]) #creates box with initial size and positons 
    # pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link1", pos=[0,0,.5] , size=[length,width,height]) #creates box with initial size and positons 

    # pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    # pyrosim.Send_Cube(name="Link2", pos=[0,0,.5] , size=[length,width,height]) #creates box with initial size and positons 

    # pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,.5,.5])
    # pyrosim.Send_Cube(name="Link3", pos=[0,.5,0] , size=[length,width,height]) #creates box with initial size and positons

    # pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0,1,0])
    # pyrosim.Send_Cube(name="Link4", pos=[0,.5,0] , size=[length,width,height]) #creates box with initial size and positons

    # pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [0,.5,-.5])
    # pyrosim.Send_Cube(name="Link5", pos=[0,0,-.5] , size=[length,width,height]) #creates box with initial size and positons

    # pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [0,0,-1])
    # pyrosim.Send_Cube(name="Link6", pos=[0,0,-.5] , size=[length,width,height]) #creates box with initial size and positons

