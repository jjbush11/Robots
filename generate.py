import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
pyrosim.Start_SDF("box.sdf") #tells pyrosim name of file where info about the world should be stored
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1]) #creates box with initial size and positons 
pyrosim.End() #closes sdf file