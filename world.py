import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf") #sets floor
        try:
            p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
        except: 
            p.loadSDF("defaultWorld.sdf")
        
        # p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf

        