import pyrosim.pyrosim as pyrosim #makes it so we dont have to say pyrosim.pyrosim.Start... every time
#alters what is in the world
pyrosim.Start_SDF("boxes.sdf") #tells pyrosim name of file where info about the world should be stored
length =1
width=1
height=1
pyrosim.Send_Cube(name="Box", pos=[0,0,.5] , size=[length,width,height]) #creates box with initial size and positons 

for x in range(1,11):
    length = .9*length
    width = .9*width
    height = .9*height
    pyrosim.Send_Cube(name="Box2", pos=[0,0,(x+.5)] , size=[length,width,height]) #creates box with initial size and positons 

pyrosim.End() #closes sdf file