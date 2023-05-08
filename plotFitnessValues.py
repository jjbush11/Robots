import numpy
import matplotlib.pyplot as mat
import constants as c

fitnessMatrixHex = numpy.load("data/fitnessMatrixHEX.npy")
fitnessMatrixQuad = numpy.load("../quad/QUADRUPED/data/fitnessMatrixQUAD.npy")

# mat.plot(backLegSensorValues, label="Back Leg", linewidth=3)
# mat.plot(frontLegSensorValues, label="Front Leg")
# mat.legend()
# mat.show()

# Mean
vectorHex = numpy.mean(fitnessMatrixHex, axis=0)
vectorQuad = numpy.mean(fitnessMatrixQuad, axis=0)

# Standard deviation
stdHex = numpy.std(fitnessMatrixHex, axis=0)
stdQuad = numpy.std(fitnessMatrixQuad, axis=0)

# plots 
# for x in range(c.populationSize):
#     mat.plot(fitnessMatrixHex[x,:], label="Hexapod Pop "+str(x+1), linewidth=3)
#     mat.plot(fitnessMatrixQuad[x,:], label="Quadruped Pop "+str(x+1), linewidth=3)\

# plots of means
# mat.plot(vectorHex, label="Hexapod Avg. Fit. ", linewidth=3)
# mat.plot(vectorQuad, label="Quadruped Avg. Fit. ", linewidth=3)

# plots of means + std
# hex m+s m m-s
mat.plot(vectorHex+stdHex, label="Hexapod Avg+Std", linewidth=3)
mat.plot(vectorHex, label="Hexapod Avg", linewidth=3)
mat.plot(vectorHex-stdHex, label="Hexapod Avg-Std", linewidth=3)
# quad m+s m m-s
mat.plot(vectorQuad+stdQuad, label="Quad Avg+Std", linewidth=3)
mat.plot(vectorQuad, label="Quad Avg", linewidth=3)
mat.plot(vectorQuad-stdQuad, label="Quad Avg-Std", linewidth=3)

mat.legend()
mat.show()
