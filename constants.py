import numpy

length =1
width=1
height=1

frontLegAmplitude = numpy.pi/4.
frontLegFrequency = 10
frontLegPhaseOffset = 0

amplitude = numpy.pi/4.
frequency = 10
offset = 0

backLegAmplitude = numpy.pi/4.
backLegFrequency = 40
backLegPhaseOffset = numpy.pi/4

loop=500
gravity=-9.8
motorForce=40

frontLegSinValues = numpy.linspace(0, 360, loop)*numpy.pi/180.
backLegSinValues = numpy.linspace(0, 360, loop)*numpy.pi/180.

numberOfGenerations = 10

populationSize = 10

numSensorNeurons = 6
numMotorNeurons = 11

motorJointRange = .2