import pybullet as p
import time
physicsClient = p.connect(p.GUI) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
p.loadSDF("box.sdf") #tells pybullet to read in the world described box.sdf
for x in range(1000):
    p.stepSimulation() #stes the physics inside the world for a small amount of time
    time.sleep(1/60) #sleeps the code for 1/60th of a second each loop iteration
    print(x)
p.disconnect
