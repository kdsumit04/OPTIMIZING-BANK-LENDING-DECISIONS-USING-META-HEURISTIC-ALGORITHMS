import random
import numpy as np
import matplotlib.pyplot as plt
random.seed(6)

# SA Parameters Initialisation
max_itr = 800
ini_temp = 200
final_temp = 50
cool = 10
e=2.71

Best_Fitness = []
Best_Solution = []

# Given Data
rT=0.01
rD=0.009
D=60
K=0.15
L=[10,25,4,11,18,3,17,15,9,10]
rL=[0.021,0.022,0.021,0.027,0.025,0.026,0.023,0.021,0.028,0.022]
loss=[0.0002,0.0058,0.0001,0.0003,0.0024,0.0002,0.0058,0.0002,0.001,0.001]

def Fitness(solution):
    loss_term = 0
    nuval = 0
    omegaval = 0
    loan_size = 0
    for i in range(10):
        if(solution[i] == 0): continue
        loss_term += loss[i]
        nuval += (rL[i]*L[i]-loss[i])
        omegaval += rT*((1-K)*D-L[i])
        loan_size += L[i]
        
    fitness = nuval+omegaval-rD*D-loss_term
    if(loan_size > (1-K)*D):
        fitness = -1

    return fitness
  
  def INITIAL_SOL_FORMATION() :
    Initial_sol = []
    for i in range(10):
        Initial_sol.append(random.choice([0,1])) # Formulated an array of size 10 because number of customers are 10
    return Initial_sol
  
  Initial_sol = INITIAL_SOL_FORMATION() 
Best_sol = Initial_sol.copy()


for i in range(max_itr):
    rand_no = np.random.randint(0,10) # Selection of any index between [0,9] so that we can change it and form new solution
    New_sol = Initial_sol.copy()
    if(New_sol[rand_no] == 0):
        New_sol[rand_no] = 1
    else : 
        New_sol[rand_no] = 0
        
    if(Fitness(New_sol) == -1):
        Initial_sol = INITIAL_SOL_FORMATION()  # As the constraint was violated we form new Initial Solution
        i -= 1
        continue;
    if(Fitness(New_sol) > Fitness(Initial_sol)):
        Initial_sol = New_sol.copy()           # As new sol is better therefore we are copying new solution to initial solution
    else :
        Prob_of_Acceptance = np.power(e,((Fitness(New_sol)-Fitness(Initial_sol))/ini_temp))
        if(Prob_of_Acceptance >= random.random() and cool > 0):
            Initial_sol = New_sol.copy()
    
    if(Fitness(Initial_sol) >= Fitness(Best_sol)):
        Best_sol = Initial_sol.copy()
        
    # Appending Best Solution and Best Fitness so far    
    Best_Fitness.append(Fitness(Best_sol))
    Best_Solution.append(Best_sol)
    
    if(ini_temp == final_temp):
        cool = 0
    ini_temp -= cool
    
    
