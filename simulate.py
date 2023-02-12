import pybullet_data #allows for use of plane.urdf
import pybullet as p
import pyrosim.pyrosim as pyrosim 
import time
import numpy

#alters how a world is simulated 
physicsClient = p.connect(p.GUI) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #something to do with floor
p.setGravity(0,0,-9.8) #sets gravity 
planeId = p.loadURDF("plane.urdf") #sets floor
robotID = p.loadURDF("body.urdf") #sets floor 
p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
pyrosim.Prepare_To_Simulate(robotID) #does more setting up

backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
for x in range(1000):
    p.stepSimulation() #sets the physics inside the world for a small amount of time
    backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #adds sensor 
    frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") #adds sensor

    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotID, #simlaute a motor in robot named robot
    jointName = b'Torso_BackLeg', #motors are always attached to joints
    controlMode = p.POSITION_CONTROL, #mains ones are position or velocity
    targetPosition = 0.0,
    maxForce = 500)

    time.sleep(1/60) #sleeps the code for 1/60th of a second each loop iteration

print(frontLegSensorValues)
numpy.save("data/backLegSensorVal.npy", backLegSensorValues)
numpy.save("data/frontLegSensorVal.npy", frontLegSensorValues)
p.disconnect
