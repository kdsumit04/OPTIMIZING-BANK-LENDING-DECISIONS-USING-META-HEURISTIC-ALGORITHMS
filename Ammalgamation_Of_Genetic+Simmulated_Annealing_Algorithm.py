from functions import *
from constants import *
import matplotlib.pyplot as plt
random.seed(2)

pop = []
for i in range(pop_size):
	temp = []
	for j in range(len(L)):
		rand_no = 1 if random.random() > 0.5 else 0
		temp.append(rand_no)
	pop.append(temp)
  
pop_old = pop
arr1, arr2 =[], []

for i in range(no_of_generation):
	if i==5: cool = 10
	pop_new = [best(pop_old)]*2
	while(len(pop_new)!= pop_size):	
		parent1,parent2 = roulette_selection(pop)
		if random.random()<pc:
			child1,child2 = crossover(parent1,parent2)
		else:
			child1,child2 = parent1,parent2
		child1 = mutation(child1)
		child2 = mutation(child2)
		tmp = SA(parent1, child1)
		pop_new.append(tmp)
		tmp = SA(parent2, child2)
		pop_new.append(tmp)

	pop_old = pop_new
	x = best(pop_new)
	arr1.append(x)
	if(len(arr2)==0): arr2.append(fitness(x))
	else : arr2.append(max(fitness(x),arr2[-1]))
	ini_temp = ini_temp - cool
	if ini_temp == fin_tmp: 
		cool = 0
