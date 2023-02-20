import pybullet as p
import pyrosim.pyrosim as pyrosim 
from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robotID = p.loadURDF("body.urdf") #sets floor 
        pyrosim.Prepare_To_Simulate(self.robotID) #does more setting up
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors=dict()
        for linkName in pyrosim.linkNamesToIndices:
             #returns instance of sensor, stored in in dictoionary 
            self.sensors[linkName] = SENSOR(linkName) 
    
    def Sense(self,x):
        for i in self.sensors:
            self.sensors[i].Get_Value(x)
        
    def Prepare_To_Act(self):
        self.motors=dict()
        for jointName in pyrosim.jointNamesToIndices:
            #returns instance of sensor, stored in in dictoionary 
            self.motors[jointName] = MOTOR(jointName)
            print(jointName)

    def Act(self,x):
        for i in self.motors:
            self.motors[i].Set_Value(self.robotID,x)
            