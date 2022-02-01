from string import ascii_letters
from random import choice, random
 
target  = list()
target.append(list("METHINKS"))
target.append(list("IT"))
target.append(list("IS"))
target.append(list("LIKE"))
target.append(list("A"))
target.append(list("WEASEL"))

charset = ascii_letters
parent = list()
for i in range(len(target)):
    parent.append([choice(charset) for _ in range(len(target[i]))])

crossover_rate = 0.7
num_children = 100  # number children that generate each time
 
def attach(arr):
    sum_arr = []
    for word in arr:
        sum_arr += word
    return sum_arr
def attach_display(arr):
    sum_arr = []
    for word in arr:
        sum_arr += word
        sum_arr += [' ']
    return sum_arr

perfectfitness = float(len(attach(target)))

def fitness(trial):
    'Sum of matching chars by position'
    return sum(t==h for t,h in zip(attach(trial), attach(target)))
 
def mutateRate(): # find mutation rate
    return (perfectfitness - fitness(parent)) / perfectfitness * 0.1
 
def mutate(parent, rate):
    'Less mutation the closer the fit of the parent'
    sum_arr = list()
    for word in parent:
        sum_arr.append([(ch if random() > rate else choice(charset)) for ch in word])
    return sum_arr
 
def display_state():
    print ("#%-4i, fitness: %4.1f%%, '%s'" %
           (iterations, fitness(parent)*100./perfectfitness, ''.join(attach_display(parent))))


def crossover(a, b):
    place = 0
    word_index = 0
    if random() < crossover_rate:
        word_index = choice(range(len(target)))
        place = choice(range(len(target[word_index])))
    else:
        return a, b
 
    return a, b, a[word_index][:place] + b[word_index][place:], b[word_index][:place] + a[word_index][place:]
 
iterations = 0
center = int(num_children/2)
while parent != target:
    rate = mutateRate() # get mutation rate
    iterations += 1
    if iterations % 100 == 0: display_state()
    children = [ mutate(parent, rate) for _ in range(num_children) ]  + [parent]
    parent1 = max(children[:center], key=fitness)
    parent2 = max(children[center:], key=fitness)
    parent = max(crossover(parent1, parent2), key=fitness)
display_state()