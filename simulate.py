import pybullet_data #allows for use of plane.urdf
import pybullet as p
import time
#alters how a world is simulated 
physicsClient = p.connect(p.GUI) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #something to do with floor
p.setGravity(0,0,-9.8) #sets gravity 
planeId = p.loadURDF("plane.urdf") #sets floor
robotID = p.loadURDF("body.urdf") #sets floor 
p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
for x in range(1000):
    p.stepSimulation() #stes the physics inside the world for a small amount of time
    time.sleep(1/60) #sleeps the code for 1/60th of a second each loop iteration
    print(x)
p.disconnect
