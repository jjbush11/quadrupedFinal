import numpy
import constants as c
import pyrosim.pyrosim as pyrosim 

class SENSOR:
    def __init__(self, linkname):
        self.linkname = linkname
        self.values = numpy.zeros(c.loop)   #creates vector of size loop of all zeros

    def Get_Value(self,x):
        self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname) #adds sensor

    def Save_Values(self):
        numpy.save("data/sensorVal.npy", self.values) 
        print("Saved")