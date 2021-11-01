from constants import *
import random
random.seed(2)

def fitness(individual, flag=0):
	v = 0
	omega = 0
	beta = 0
	total_sum_loan=0
	s_l = 0
	for i in range(len(L)):
		if individual[i]==1:
			v+= (rL[i]*L[i]-lamda[i])
			omega+= (Rt*((1-k)*d-L[i]))
			total_sum_loan+= L[i]
			s_l += lamda[i]
		else:
			continue

	fitness_value = v+omega-Rd*d-s_l

	if total_sum_loan > (1-k)*d:
		fitness_value -= 5

	if flag==1:
		print(v, omega, beta, s_l, penalty)
	return fitness_value

def roulette_selection(population):
	fitness_population=[]
	for i in range(len(population)):
		fitness_population.append(fitness(population[i]))

	for i in range(1,len(fitness_population)):
		fitness_population[i]=fitness_population[i]+fitness_population[i-1]
	sum_fitness = fitness_population[-1]
	for i in range(len(fitness_population)):
		fitness_population[i] = fitness_population[i]/sum_fitness
	rand1= random.random()
	rand2= random.random()
	p1=-1
	p2=-1
	for i in range(len(fitness_population)):
		if rand1<fitness_population[i] and p1 is -1:
			p1=population[i]
		if rand2<fitness_population[i] and p2 is -1:
			p2=population[i]

	return p1,p2

def crossover(parent1,parent2):
	rand_int = random.randint(1,len(parent1)-2)
	child1 = []
	child2 = []
	child1 += parent1[0:rand_int]
	child1 += parent2[rand_int:]
	child2 += parent2[0:rand_int]
	child2 += parent1[rand_int:]

	return child1,child2

def mutation(parent):
	for i in range(len(parent)):
		if random.random() < pm:
			if parent[i] == 1:
				parent[i] = 0
			else:
				parent[i] = 1 
	return parent

def best(pop):
	best = pop[0]
	for i in range(len(pop)):
		if fitness(best) < fitness(pop[i]):
			best = pop[i]
	return best
