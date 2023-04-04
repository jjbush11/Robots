import numpy
import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
import constants as c
import os
import random
import time


class SOLUTION: 
    def __init__(self, nextAvailableID):
        self.myID = nextAvailableID
        self.weights = numpy.random.rand(c.numSensorNeurons,c.numMotorNeurons) 
        self.weights = self.weights * 2 -1

    # def Evaluate(self, directOrGui):
    #     self.Create_World()
    #     self.Create_Body()
    #     self.Create_Brain()

    #     os.system("start /B python3 simulate.py " + directOrGui + " "+str(self.myID))

    #     while not os.path.exists("fitness"+str(self.myID)+".txt"):
    #         time.sleep(0.01)
    #     inFile = open("fitness"+str(self.myID)+".txt", "r")
    #     self.fitness = float(inFile.read())
    #     print(self.fitness)
    #     inFile.close()

    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system("start /B python3 simulate.py " + directOrGui + " "+str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        inFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(inFile.read())
        inFile.close()

        os.system("del fitness"+str(self.myID)+".txt")
        
    def Create_World(self):
        # while not os.path.exists("world.sdf"):
        #     time.sleep(0.01)
        pyrosim.Start_SDF("world.sdf") #tells pyrosim name of file where info about the world should be stored
        
        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[c.length,c.width,c.height]) #creates box with initial size and positons 

        pyrosim.End() #closes sdf file

    def Create_Body(self):
        # while not os.path.exists("body.urdf"):
        #     time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")

        # torso and upper leg
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,2,c.height]) #creates box with initial size and positons 

        # right side bottom leg 
        pyrosim.Send_Joint( name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , type = "revolute", position = [.5,-1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[.5,0,0], size=[1,.2,.2]) #creates box with initial size and positons 

        # right side top right leg
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [.5,1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # Middle Left side 
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # Middle Right Side (Side closer to camera)
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [.5,0,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # left side lower leg 
        pyrosim.Send_Joint( name = "Torso_LowerLeft" , parent= "Torso" , child = "LowerLeft" , type = "revolute", position = [-.5,-1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LowerLeft", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # left side top leg 
        pyrosim.Send_Joint( name = "Torso_TopLeft" , parent= "Torso" , child = "TopLeft" , type = "revolute", position = [-.5,1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="TopLeft", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower leg     
        pyrosim.Send_Joint( name = "BackLeg_backLowerLeg" , parent= "BackLeg" , child = "backLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="backLowerLeg", pos=[0,-.5,0] , size=[.2,1,.2]) #creates box with initial size and positons
     
        pyrosim.Send_Joint( name = "FrontLeg_frontLowerLeg" , parent= "FrontLeg" , child = "frontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="frontLowerLeg", pos=[0,.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "LeftLeg_leftLowerLeg" , parent= "LeftLeg" , child = "leftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="leftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "RightLeg_rightLowerLeg" , parent= "RightLeg" , child = "rightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="rightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.End()   

    def Create_Brain(self):
        # while not os.path.exists("brain"+str(self.myID)+".nndf"):
        #     time.sleep(0.01)
            
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "BackRightLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName = "backLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName = "frontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName = "leftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName = "rightLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "BackLeg_backLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "FrontLeg_frontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "LeftLeg_leftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "RightLeg_rightLowerLeg")

        for currentRow in range (c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomColumn = random.randint(0,c.numMotorNeurons-1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1

    def Set_ID(self, nextAvailableID):
        self.myID = nextAvailableID



