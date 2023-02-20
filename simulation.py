from world import WORLD
from robot import ROBOT
import pybullet_data #allows for use of plane.urdf
import pybullet as p
import pyrosim.pyrosim as pyrosim 
import constants as c
import numpy
import time

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
        p.setAdditionalSearchPath(pybullet_data.getDataPath()) #something to do with floor
        p.setGravity(0,0,c.gravity) #sets gravity 
        self.world = WORLD()
        self.robotID = ROBOT()
    
    def Run(self):
        for x in range(c.loop):
            p.stepSimulation() #sets the physics inside the world for a small amount of time
            self.robotID.Sense(x)
            self.robotID.Act(x)
            time.sleep(1/60)
        
    def __del__(self):
        p.disconnect()



