class TEST:
    def __init__(self):
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.sensors={
            "key1":"jams",
            "key2":"gem"
        }

    def Sense(self):
        # c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") #adds sensor
        for i in self.sensors:
            print(i)
            # SENSOR.Get_Value(self.sensors[i])

test =TEST()
test.Sense()
for x in range(5): 
    print(x)

print(x)