import random
import numpy as np
import matplotlib.pyplot as plt
random.seed(8)

# Given Data
rT=0.01
rD=0.009
D=60
K=0.15
L=[10,25,4,11,18,3,17,15,9,10]
rL=[0.021,0.022,0.021,0.027,0.025,0.026,0.023,0.021,0.028,0.022]
loss=[0.0002,0.0058,0.0001,0.0003,0.0024,0.0002,0.0058,0.0002,0.001,0.001]

# GA Parameters Initialisation
Pop_Size = 50
max_itr = 800
Pc = 0.8
Pm = 0.006

def Population_Generation():
    
    POP = []
    for i in range(Pop_Size):
        Chromosome = []
        for j in range(10):
            Chromosome.append(random.choice([0,1]))
        POP.append(Chromosome)
    return POP

def Fitness(Solution):
    
    loss_term = 0
    nuval = 0
    omegaval = 0
    loan_size = 0
    for i in range(10):
        if(Solution[i] == 0): continue
        loss_term += loss[i]
        nuval += (rL[i]*L[i]-loss[i])
        omegaval += rT*((1-K)*D-L[i])
        loan_size += L[i]
        
    fitness = nuval+omegaval-rD*D-loss_term
    if(loan_size > (1-K)*D):
        fitness = 0.001

    return fitness

def Crossover(Par1 , Par2):
    
    if(random.random() > Pc):
        return Par1 ,Par2
    temp1 = Par1.copy()
    temp2 = Par2.copy()
    rand_no = np.random.randint(0,10)
    Par1 = temp1[:rand_no] + temp2[rand_no:]
    Par2 = temp2[:rand_no] + temp1[rand_no:]
    
    return Par1 ,Par2

def Mutation(Par):
    
    for i in range(len(Par)):
        if(random.random() > Pm):
            continue
        if(Par[i] == 0): Par[i] = 1
        else : Par[i] = 0
    
    return Par    

def Roulette_Selection(POP):
    
    Fitness_of_Chromosome = []
    Sum_of_Fitness = 0
    
    for i in range(Pop_Size):
        f = Fitness(POP[i])
        Fitness_of_Chromosome.append(f)
        Sum_of_Fitness += f
    for i in range(1,Pop_Size):
        Fitness_of_Chromosome[i] += Fitness_of_Chromosome[i-1]
    for i in range(Pop_Size):
        Fitness_of_Chromosome[i] /= Sum_of_Fitness
        
    New_Generation = []
    Random_Numbers = []
    
    for i in range(Pop_Size):
        Random_Numbers.append(random.random())  # Generating 10 random numbers to do Roulette Selection 10 times to generate new solution
        
    for i in range(Pop_Size):
        rand_no = Random_Numbers[i]
        
        for j in range(Pop_Size):
            if(rand_no < Fitness_of_Chromosome[j]):
                New_Generation.append(POP[j])
                break
    return New_Generation

def Best_Solution(POP):
    
    best_fit = Fitness(POP[0])
    best_sol = POP[0].copy()
    for i in range(1,Pop_Size):
        if(Fitness(POP[i]) > best_fit):
            best_fit = Fitness(POP[i])
            best_sol = POP[i].copy()
    return best_fit,best_sol

def Main_Function():
    Best_Fitness = []
    Best_Sol = []
    Initial_Pop = Population_Generation()
    for i in range(max_itr):
        New_Pop = Roulette_Selection(Initial_Pop)
        for j in range(Pop_Size,2):
            Child1 , Child2 = Crossover(New_Pop[j] , New_Pop[j+1])
            New_Pop[j] = Child1
            New_Pop[j+1] = Child2
            
        for j in range(Pop_Size):
            New_Pop[j] = Mutation(New_Pop[j])
            
        Initial_Pop = New_Pop.copy()
        best_fit , best_sol = Best_Solution(Initial_Pop)
        if(len(Best_Fitness) == 0):
            Best_Fitness.append(best_fit)
            Best_Sol.append(best_sol)
        else:
            if(Best_Fitness[-1] < best_fit):
                Best_Fitness.append(best_fit)
                Best_Sol.append(best_sol)
            else:
                Best_Fitness.append(Best_Fitness[-1])
                Best_Sol.append(Best_Sol[-1])
    return Best_Fitness , Best_Sol

Best_Fitness , Best_Solution = Main_Function()
