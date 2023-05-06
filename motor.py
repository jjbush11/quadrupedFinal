import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim 

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorsVect = numpy.linspace(0, 360, c.loop)*numpy.pi/180.   #creates vector of size loop of all zeros

    def Set_Value(self, robotID, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, #simlaute a motor in robot named robot
            jointName = self.jointName, #motors are always attached to joints
            controlMode = p.POSITION_CONTROL, #mains ones are position or velocity
            targetPosition = c.amplitude*numpy.sin(desiredAngle*c.frequency+c.offset),
            maxForce = c.motorForce)
    
      
