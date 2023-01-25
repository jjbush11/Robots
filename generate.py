import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
#alters what is in the world

length =1
width=1
height=1

def Create_World():
    pyrosim.Start_SDF("world.sdf") #tells pyrosim name of file where info about the world should be stored
    pyrosim.Send_Cube(name="Box", pos=[-2,2,.5] , size=[length,width,height]) #creates box with initial size and positons 
    pyrosim.End() #closes sdf file

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0,0,.5] , size=[length,width,height]) #creates box with initial size and positons 
    pyrosim.End()

Create_World()
Create_Robot()

