import os
# from hillclimber import HILL_CLIMBER
from parallelHillclimber import PARALLEL_HILL_CLIMBER



# for x in range(5): 
#     os.system("python3 generate.py")
#     os.system("python3 simulate.py")

# hc = HILL_CLIMBER()
# # hc.Show_Initial()
# hc.Evolve()
# hc.Show_Best()
os.system("del brain*.nndf")
os.system("del fitness*.txt")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()



