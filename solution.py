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
        while not os.path.exists("world.sdf"):
            print("waiting for world")
            time.sleep(0.01)
        pyrosim.Start_SDF("world.sdf") #tells pyrosim name of file where info about the world should be stored
        
        pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[c.length,c.width,c.height]) #creates box with initial size and positons 

        pyrosim.End() #closes sdf file

    def Create_Body(self):
        # while not os.path.exists("body.urdf"):
        #     print("waiting for body")
        #     time.sleep(0.01)
        pyrosim.Start_URDF("body.urdf")

        # torso and upper leg
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[1,2,c.height]) #creates box with initial size and positons 

        # right side bottom leg 
        pyrosim.Send_Joint( name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , type = "revolute", position = [.5,-1,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[.5,0,0], size=[1,.2,.2]) #creates box with initial size and positons 

        # right side top right leg
        pyrosim.Send_Joint( name = "Torso_FrontRightLeg" , parent= "Torso" , child = "FrontRightLeg" , type = "revolute", position = [.5,1,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # Middle Left side 
        pyrosim.Send_Joint( name = "Torso_MiddleLeftLeg" , parent= "Torso" , child = "MiddleLeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # Middle Right Side (Side closer to camera)
        pyrosim.Send_Joint( name = "Torso_MiddleRightLeg" , parent= "Torso" , child = "MiddleRightLeg" , type = "revolute", position = [.5,0,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="MiddleRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # left side lower leg 
        pyrosim.Send_Joint( name = "Torso_BackLeftLeg" , parent= "Torso" , child = "BackLeftLeg" , type = "revolute", position = [-.5,-1,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # left side top leg 
        pyrosim.Send_Joint( name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , type = "revolute", position = [-.5,1,1], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower legs right side    
        pyrosim.Send_Joint( name = "BackRightLeg_backRightLowerLeg" , parent= "BackRightLeg" , child = "backRightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="backRightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
     
        pyrosim.Send_Joint( name = "MiddleRightLeg_middleRightLowerLeg" , parent= "MiddleRightLeg" , child = "middleRightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="middleRightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "FrontRightLeg_frontRightLowerLeg" , parent= "FrontRightLeg" , child = "frontRightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="frontRightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower legs left side 
        pyrosim.Send_Joint( name = "MiddleLeftLeg_middleLeftLowerLeg" , parent= "MiddleLeftLeg" , child = "middleLeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="middleLeftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "BackLeftLeg_backLeftLowerLeg" , parent= "BackLeftLeg" , child = "backLeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="backLeftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "FrontLeftLeg_frontLeftLowerLeg" , parent= "FrontLeftLeg" , child = "frontLeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="frontLeftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.End()   

    def Create_Brain(self):
        # while not os.path.exists("brain"+str(self.myID)+".nndf"):
        #     time.sleep(0.01)
            
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        # pyrosim.Send_Sensor_Neuron(name=0, linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name=1, linkName = "BackRightLeg")
        # pyrosim.Send_Sensor_Neuron(name=2, linkName = "FrontRightLeg")
        # pyrosim.Send_Sensor_Neuron(name=3, linkName = "MiddleLeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=4, linkName = "MiddleRightLeg")
        # pyrosim.Send_Sensor_Neuron(name=5, linkName = "FrontLeftLeg")
        # pyrosim.Send_Sensor_Neuron(name=6, linkName = "BackLeftLeg")

        pyrosim.Send_Sensor_Neuron(name=0, linkName = "backRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "middleRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName = "frontRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName = "middleLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName = "backLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName = "frontLeftLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_MiddleRightLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "BackRightLeg_backRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 12 , jointName = "MiddleRightLeg_middleRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 13 , jointName = "FrontRightLeg_frontRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 14 , jointName = "MiddleLeftLeg_middleLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 15 , jointName = "BackLeftLeg_backLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 16 , jointName = "FrontLeftLeg_frontLeftLowerLeg")

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



