import pybullet as p
import os
import time

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf") #sets floor
        while not os.path.exists("world.sdf"):
            print("World does not exist")
            time.sleep(0.01)
        p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
        