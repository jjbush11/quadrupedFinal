from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = dict()
        self.nextAvailableID = 0
        
        # os.system("del brain"+str(self.nextAvailableID)+".nndf")
        # os.system("del fitness"+str(self.nextAvailableID)+".txt")

        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
        
        self.fitnessMatrix = np.zeros((c.populationSize, c.numberOfGenerations))
        self.tempPop = 0
        self.tempGen = 0

    def Evolve(self):
        self.Evaluate(self.parents)

        # self.parent.Evaluate("direct")
        for currentGeneration in range(c.numberOfGenerations):
            # if (currentGeneration == 0):
            #     self.Show_Best()
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = dict()
        for x in self.parents:
            self.children[x] = copy.deepcopy(self.parents[x])
            self.children[x].Set_ID(self.nextAvailableID)
            self.nextAvailableID+=1


    def Mutate(self):
        for x in self.children:
            self.children[x].Mutate()

    def Select(self):
        for x in self.parents:
            if (self.parents[x].fitness<self.children[x].fitness):
                self.parents[x] = self.children[x]

    def Print(self):
        self.tempPop = 0
        for x in self.parents:
            print("\nPairs: ",self.parents[x].fitness, " ", self.children[x].fitness,"\n")

            self.fitnessMatrix[self.tempPop][self.tempGen] = self.parents[x].fitness
            self.tempPop+=1
        self.tempGen+=1

        


    # def Show_Initial(self):
    #     os.system("python3 simulate.py gui")

    def Show_Best(self):
        # temp = self.parents[0].fitness
        # min = 0
        # for x in self.parents:
        #     if (self.parents[x].fitness < temp):
        #         temp = self.parents[x].fitness
        #         min = x
        # f = open("data/bestFitness.txt", "a")
        # f.write(str(self.parents[min].fitness)+"\n")
        # f.close()
        # self.parents[min].Start_Simulation("GUI")

        temp = self.parents[0].fitness
        max = 0
        for x in self.parents:
            if (self.parents[x].fitness > temp):
                temp = self.parents[x].fitness
                max = x
        f = open("data/bestFitness.txt", "a")
        f.write(str(self.parents[max].fitness)+"\n")
        f.close()

        np.savetxt("data/fitnessMatrixQUAD.csv", self.fitnessMatrix, delimiter=",")
        np.save("data/fitnessMatrixQUAD.npy", self.fitnessMatrix)

        # Saving the best ones information
        # os.system("ren brain"+str(self.parents[max].myID)+".nndf " "showBestBrain"+str(self.parents[max].myID)+".nndf")
        

        self.parents[max].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for x in range(c.populationSize):
            solutions[x].Start_Simulation("DIRECT")

        for x in range(c.populationSize):
            solutions[x].Wait_For_Simulation_To_End()