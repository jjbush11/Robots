# Evolutionary Robotics
Which robot, a hexapod or quadruped, evolves to move further? To answer this question I used the physics engine PyBullet to build and simulate evolution on quadruped and a hexapod. This evolutionary algorithm gave higher fitness scores to robots that moved far and moved with a constant motion. 

# Evolution
<img width="299" alt="image" src="https://github.com/jjbush11/Robots/assets/112502062/bb538e92-fa6f-4b7e-ba5e-42c11c3d5a19">

This figure shows proof of evolution in the Hexapod and the Quadruped. Each line represents the evolution of the robot as the generation size grows. It’s clear that for both robots, as they move through the generations, their fitness is improving. In both robots, the last generation had a fitness significantly greater than the fitness of the first generation, showing clear proof of evolution.

# Results
<img width="285" alt="image" src="https://github.com/jjbush11/Robots/assets/112502062/19cbf5d7-ed80-4056-8298-b65342f7c9de">

In this figure there are three curves that represent each robot. The Quadruped’s lines are different shades of blue and the Hexapod’s lines are different shades of red.
Based on this graph, I cannot draw conclusions as to which robot evolved to move further. Although the Quadruped has a mean fitness curve greater than the Hexapod, there is an overlap between the Quadruped’s curves and Hexapod’s curves. 



