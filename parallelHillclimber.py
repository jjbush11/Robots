from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        self.parents = dict()
        self.nextAvailableID = 0
        for x in range(c.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID+=1
        # self.parent = SOLUTION()

    def Evolve(self):
        for x in range(c.populationSize):
            self.parents[x].Evaluate("GUI")
        # self.parent.Evaluate("direct")
        # for currentGeneration in range(c.numberOfGenerations):
        #     if (currentGeneration == 0):
        #         self.Show_Best()
        #     self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("direct")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID+=1

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if (self.parent.fitness<self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("Pairs: ",self.parent.fitness, " ", self.child.fitness)

    # def Show_Initial(self):
    #     os.system("python3 simulate.py gui")

    def Show_Best(self):
        pass
        # os.system("python3 simulate.py gui")