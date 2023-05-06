import numpy
import matplotlib.pyplot as mat

backLegSensorValues = numpy.load("data/backLegSensorVal.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorVal.npy")
FLSinArrayValues = numpy.load("data/frontLegSinArrayValues.npy")
BLSinArrayValues = numpy.load("data/backLegSinArrayValues.npy")

# mat.plot(backLegSensorValues, label="Back Leg", linewidth=3)
# mat.plot(frontLegSensorValues, label="Front Leg")
# mat.legend()
# mat.show()

# array value plot
mat.plot(FLSinArrayValues, label="Array Values", linewidth=3)
mat.plot(BLSinArrayValues, label="Array Values", linewidth=1)
mat.legend()
mat.show()

#print(backLegSensorValues)