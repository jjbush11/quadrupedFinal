# Evolutionary Robotics

Which robot, a hexapod or quadruped, evolves to move further? To answer this question, I used PyBullet physics engine to compare the evolution of a Quadruped and Hexapod robot over the same evolutionary algorithm. This algorithm gives higher fitness scores to robots that moved far and in regular motion.

# Evolution 
<img width="299" alt="image" src="https://github.com/jjbush11/quadrupedFinal/assets/112502062/a9b997b2-fb0f-4ec2-81a2-927331ec2aaa">

This figure shows proof of evolution in the Hexapod and the Quadruped. Each line represents the evolution of the robot as the generation size grows. It’s clear that for both robots, as they move through the generations, their fitness is improving. In both robots, the last generation had a fitness significantly greater than the fitness of the first generation, showing clear proof of evolution.


# Results
<img width="285" alt="image" src="https://github.com/jjbush11/quadrupedFinal/assets/112502062/6337eaed-b08a-4a57-8f10-af014860b9d8">
In this figure, there are three curves that represent each robot. The Quadruped’s lines are different shades of blue and the Hexapod’s lines are different shades of red.
Based on this graph, I cannot draw conclusions as to which robot evolved to move further. Although the Quadruped has a mean fitness curve greater than the Hexapod, there is an overlap between the Quadruped’s curves and the Hexapod’s curves. 




