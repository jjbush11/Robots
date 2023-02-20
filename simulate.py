from simulation import SIMULATION 

simulation = SIMULATION()
simulation.Run()

# import constants as c
# import pybullet_data #allows for use of plane.urdf
# import pybullet as p
# import pyrosim.pyrosim as pyrosim 
# import time
# import numpy

# # alters how a world is simulated 
# physicsClient = p.connect(p.GUI) #creates object which handles the phyiscs and draws results to GUI (graphical user interface)
# p.setAdditionalSearchPath(pybullet_data.getDataPath()) #something to do with floor
# p.setGravity(0,0,c.gravity) #sets gravity 
# planeId = p.loadURDF("plane.urdf") #sets floor
# robotID = p.loadURDF("body.urdf") #sets floor 
# p.loadSDF("world.sdf") #tells pybullet to read in the world described box.sdf
# pyrosim.Prepare_To_Simulate(robotID) #does more setting up

# backLegSensorValues = numpy.zeros(c.loop)
# frontLegSensorValues = numpy.zeros(c.loop)

# frontLegSinValues = numpy.linspace(0, 360, c.loop)*numpy.pi/180.
# backLegSinValues = numpy.linspace(0, 360, c.loop)*numpy.pi/180.

# # numpy.save("data/frontLegSinArrayValues.npy", c.frontLegAmplitude*numpy.sin(frontLegSinValues*c.frontLegFrequency+c.frontLegPhaseOffset))
# # numpy.save("data/backLegSinArrayValues.npy", c.backLegAmplitude*numpy.sin(backLegSinValues*c.backLegFrequency+c.backLegPhaseOffset))

# # exit()
# for x in range(c.loop):
#     p.stepSimulation() #sets the physics inside the world for a small amount of time
#     c.backLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg") #adds sensor 
#     c.frontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") #adds sensor

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotID, #simlaute a motor in robot named robot
#     jointName = b'Torso_BackLeg', #motors are always attached to joints
#     controlMode = p.POSITION_CONTROL, #mains ones are position or velocity
#     targetPosition = c.backLegAmplitude*numpy.sin(backLegSensorValues[x]*c.backLegFrequency+c.backLegPhaseOffset),
#     maxForce = c.motorForce)

#     pyrosim.Set_Motor_For_Joint(
#     bodyIndex = robotID, #simlaute a motor in robot named robot
#     jointName = b'Torso_FrontLeg', #motors are always attached to joints
#     controlMode = p.POSITION_CONTROL, #mains ones are position or velocity
#     targetPosition = c.frontLegAmplitude*numpy.sin(frontLegSinValues[x]*c.frontLegFrequency+c.frontLegPhaseOffset),
#     maxForce = c.motorForce)

#     time.sleep(1/60) #sleeps the code for 1/60th of a second each loop iteration

# print(frontLegSensorValues)
# numpy.save("data/backLegSensorVal.npy", backLegSensorValues)
# numpy.save("data/frontLegSensorVal.npy", frontLegSensorValues)
# p.disconnect
