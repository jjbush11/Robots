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

        os.system("start /B python3 -W ignore simulate.py " + directOrGui + " "+str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)
        inFile = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(inFile.read())
        inFile.close()

        os.system("del fitness"+str(self.myID)+".txt")
        
    def Create_World(self):
        # while not os.path.exists("world"+str(self.myID)+".sdf"):
        #     print("waiting for world")
        #     time.sleep(0.01)
        pyrosim.Start_SDF("world"+str(self.myID)+".sdf") #tells pyrosim name of file where info about the world should be stored
        
        # pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[c.length,c.width,c.height]) #creates box with initial size and positons 

        pyrosim.End() #closes sdf file

    def Create_Body(self):
        # while not os.path.exists("body.urdf"):
        #     print("waiting for body")
        #     time.sleep(0.01)

        pyrosim.Start_URDF("body"+str(self.myID)+".urdf")
        # pyrosim.Start_URDF("body.urdf")
        # pyrosim.Start_URDF("bodyTwo.urdf")

        # torso and upper leg
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[c.length,2,c.height]) #creates box with initial size and positons 

        # right side bottom leg 
        pyrosim.Send_Joint( name = "Torso_BackRightLeg" , parent= "Torso" , child = "BackRightLeg" , type = "revolute", position = [.5,-1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLeg", pos=[.5,0,0], size=[1,.2,.2]) #creates box with initial size and positons 

        # right side top right leg
        pyrosim.Send_Joint( name = "Torso_FrontRightLeg" , parent= "Torso" , child = "FrontRightLeg" , type = "revolute", position = [.5,1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        

        # left side lower leg 
        pyrosim.Send_Joint( name = "Torso_BackLeftLeg" , parent= "Torso" , child = "BackLeftLeg" , type = "revolute", position = [-.5,-1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # left side top leg 
        pyrosim.Send_Joint( name = "Torso_FrontLeftLeg" , parent= "Torso" , child = "FrontLeftLeg" , type = "revolute", position = [-.5,1,1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower legs right side    
        pyrosim.Send_Joint( name = "BackRightLeg_backRightLowerLeg" , parent= "BackRightLeg" , child = "backRightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="backRightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
     
        pyrosim.Send_Joint( name = "FrontRightLeg_frontRightLowerLeg" , parent= "FrontRightLeg" , child = "frontRightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="frontRightLowerLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # Lower legs left side 
        pyrosim.Send_Joint( name = "BackLeftLeg_backLeftLowerLeg" , parent= "BackLeftLeg" , child = "backLeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="backLeftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.Send_Joint( name = "FrontLeftLeg_frontLeftLowerLeg" , parent= "FrontLeftLeg" , child = "frontLeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="frontLeftLowerLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        pyrosim.End()

        # Middle Left side 
        # pyrosim.Send_Joint( name = "Torso_MiddleLeftLeg" , parent= "Torso" , child = "MiddleLeftLeg" , type = "revolute", position = [-.5,0,1], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="MiddleLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons
        
        # # Middle Right Side (Side closer to camera)
        # pyrosim.Send_Joint( name = "Torso_MiddleRightLeg" , parent= "Torso" , child = "MiddleRightLeg" , type = "revolute", position = [.5,0,1], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="MiddleRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # # Upper Front Leg
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0,.5,1], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        # # Upper Back Leg
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0,-.5,1], jointAxis="0 0 1")
        # pyrosim.Send_Cube(name="BackLeg", pos=[0,-.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        # # Lower Left Side Leg
        # pyrosim.Send_Joint( name = "MiddleLeftLeg_LowerLeftLeg" , parent= "MiddleLeftLeg" , child = "LowerLeftLeg" , type = "revolute", position = [-1,0,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LowerLeftLeg", pos=[-.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # # Lower Right Side Leg 
        # pyrosim.Send_Joint( name = "MiddleRightLeg_LowerRightLeg" , parent= "MiddleRightLeg" , child = "LowerRightLeg" , type = "revolute", position = [1,0,0], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="LowerRightLeg", pos=[.5,0,0] , size=[1,.2,.2]) #creates box with initial size and positons

        # # Lower Front Leg    
        # pyrosim.Send_Joint( name = "FrontLeg_LowerFrontLeg" , parent= "FrontLeg" , child = "LowerFrontLeg" , type = "revolute", position = [0,1,0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="LowerFrontLeg", pos=[0,.5,0] , size=[.2,1,.2]) #creates box with initial size and positons
     
        # # Lower Back Leg
        # pyrosim.Send_Joint( name = "BackLeg_LowerBackLeg" , parent= "BackLeg" , child = "LowerBackLeg" , type = "revolute", position = [0,-1,0], jointAxis="1 0 0")
        # pyrosim.Send_Cube(name="LowerBackLeg", pos=[0,-.5,0] , size=[.2,1,.2]) #creates box with initial size and positons

        # pyrosim.End()   

    def Create_Brain(self):
        # while not os.path.exists("brain"+str(self.myID)+".nndf"):
        #     time.sleep(0.01)
            
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")


        pyrosim.Send_Sensor_Neuron(name=0, linkName = "backRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=1, linkName = "frontRightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName = "backLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName = "frontLeftLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_BackRightLeg")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontRightLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_FrontLeftLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "BackRightLeg_backRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "FrontRightLeg_frontRightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "BackLeftLeg_backLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "FrontLeftLeg_frontLeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Torso_BackLeftLeg")



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



