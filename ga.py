from string import ascii_letters
from random import choice, random
 
target  = list("METHINKS IT IS LIKE A WEASEL")
charset = ascii_letters + ' '
parent  = [choice(charset) for _ in range(len(target))]
crossover_rate = 0.7
num_children = 100  # number children that generate each time
 
perfectfitness = float(len(target))
 
def fitness(trial):
    'Sum of matching chars by position'
    return sum(t==h for t,h in zip(trial, target))
 
def mutaterate():
    return 1-((perfectfitness - fitness(parent)) / perfectfitness * 0.1)
 
def mutate(parent, rate):
    'Less mutation the closer the fit of the parent'
    return [(ch if random() <= rate else choice(charset)) for ch in parent]
 
def display_state():
    print ("#%-4i, fitness: %4.1f%%, '%s'" %
           (iterations, fitness(parent)*100./perfectfitness, ''.join(parent)))
 
def crossover(a, b):
    place = 0
    if random() < crossover_rate:
        place = choice(range(len(target)))
    else:
        return a, b
 
    return a, b, a[:place] + b[place:], b[:place] + a[place:]
 
iterations = 0
center = int(num_children/2)
while parent != target:
    rate = mutaterate() # get mutation rate
    iterations += 1
    if iterations % 100 == 0: display_state()
    children = [ mutate(parent, rate) for _ in range(num_children) ]  + [parent]
    parent1 = max(children[:center], key=fitness)
    parent2 = max(children[center:], key=fitness)
    parent = max(crossover(parent1, parent2), key=fitness)
display_state()