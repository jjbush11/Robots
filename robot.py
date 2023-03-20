import pybullet as p
import pyrosim.pyrosim as pyrosim 
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.myID = solutionID
        self.robotID = p.loadURDF("body.urdf") #sets floor 
        pyrosim.Prepare_To_Simulate(self.robotID) #does more setting up
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(self.myID)+".nndf")
        os.system("del brain"+str(self.myID)+".nndf")

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
            #returns instance of motor, stored in in dictoionary 
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,x):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = bytes(self.nn.Get_Motor_Neurons_Joint(neuronName), 'utf-8')
                # jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robotID, desiredAngle)
                # for i in self.motors:
                #     self.motors[i].Set_Value(self.robotID, desiredAngle)
    
    def Think(self):
        self.nn.Update()
        # self.nn.Print()
    
    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotID,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        inFile = open("tmp"+str(self.myID)+".txt", "w")
        inFile.write(str(xCoordinateOfLinkZero))
        # os.system("rename tmp"+str(self.myID)+".txt" "fitness"+str(self.myID)+".txt")        
        os.rename("tmp"+str(self.myID)+".txt" , "fitness"+str(self.myID)+".txt")
        inFile.close()
        
        
            