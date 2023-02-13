import numpy
import matplotlib.pyplot as mat

backLegSensorValues = numpy.load("data/backLegSensorVal.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorVal.npy")
sinArrayValues = numpy.load("data/sinArrayValues.npy")

# mat.plot(backLegSensorValues, label="Back Leg", linewidth=3)
# mat.plot(frontLegSensorValues, label="Front Leg")
# mat.legend()
# mat.show()

# array value plot
mat.plot(sinArrayValues, label="Array Values", linewidth=3)
mat.legend()
mat.show()

#print(backLegSensorValues)