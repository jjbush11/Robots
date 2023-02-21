import numpy
import constants as c
import pybullet as p
import pyrosim.pyrosim as pyrosim 

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.motorsVect = numpy.linspace(0, 360, c.loop)*numpy.pi/180.   #creates vector of size loop of all zeros
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude 
        self.frequency = c.frequency
        self.offset = c.offset
        if (self.jointName == b'Torso_BackLeg'):
            self.frequency = 10
        self.motorVals = self.amplitude*numpy.sin(self.motorsVect*self.frequency+self.offset) 

    def Set_Value(self, robotID,x):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotID, #simlaute a motor in robot named robot
            jointName = self.jointName, #motors are always attached to joints
            controlMode = p.POSITION_CONTROL, #mains ones are position or velocity
            targetPosition = self.amplitude*numpy.sin(self.motorsVect[x]*self.frequency+self.offset),
            maxForce = c.motorForce)
    
    def Save_Values(self):
        numpy.save("data/moterSinArrayValues.npy", self.motorVals)
      
