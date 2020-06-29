import random
import operator
import csv
import itertools

import Norm
import numpy
import FB
import MainToExe

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

MAX_TREE_DEPTH = 40
POPULATION_SIZE = 1000
CROSSOVER_RATE = 0.75
MUTATION_RATE = 0.1
NUM_OF_GENERATIONS = 100
# How much samples from the data we will take at evaluate function
SAMPLING_SIZE = 1000

def get_data_set(filename):
    with open(filename) as data_file:
        data_reader = csv.reader(data_file)
        # TODO - run on original test set (catch '?' character)
        dataBeforeNorm = list(list(float(elem) for elem in row) for row in data_reader)
        dataNorm = Norm.normalization(dataBeforeNorm)
    return dataNorm

def eval_dataset(individual, filename, check=False):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Randomly sample 400 mails in the spam database
    data = get_data_set(filename)
    # Evaluate the sum of correctly identified mail as spam
    if len(data[0]) == 121:
        result = [bool(func(*mail[1:])) for mail in data]
    elif len(data[0]) == 120:
        result = [bool(func(*mail)) for mail in data]
    else:
        raise(f'enexpected length! {len(data[0])}')

    if check:
        size = len(result)
        correct = sum(result[i] == data[i][0] for i in range(size))
        print(f'got acc of {correct}/{size}')
    else:
        with open('output', 'w') as f:
            for x in result:
                f.write(str(int(x)) + '\n')
    return result

with open("dataset/train.csv") as spambase:
    spamReader = csv.reader(spambase)
    spam = list(list(float(elem) for elem in row) for row in spamReader)

# defined a new primitive set for strongly typed GP
# 120 floats for 4 features * 30 sampels
# TODO - preprocessing the data - currenly it's treated as 120 length vector
pset = gp.PrimitiveSetTyped("MAIN", itertools.repeat(float, 120), bool, "IN")

# boolean operators
pset.addPrimitive(operator.and_, [bool, bool], bool)
pset.addPrimitive(operator.or_, [bool, bool], bool)
pset.addPrimitive(operator.not_, [bool], bool)

# floating point operators
# Define a protected division function
def protectedDiv(left, right):
    try: return left / right
    except ZeroDivisionError: return 1

pset.addPrimitive(operator.add, [float,float], float)
pset.addPrimitive(operator.sub, [float,float], float)
pset.addPrimitive(operator.mul, [float,float], float)
pset.addPrimitive(protectedDiv, [float,float], float)
pset.addPrimitive(operator.neg, 1)
# pset.addPrimitive(numpy.cos, 1)
# pset.addPrimitive(numpy.sin, 1)

# logic operators
# Define a new if-then-else function
def if_then_else(input, output1, output2):
    if input: return output1
    else: return output2

pset.addPrimitive(operator.lt, [float, float], bool)
pset.addPrimitive(operator.eq, [float, float], bool)
pset.addPrimitive(if_then_else, [bool, float, float], float)

# terminals
pset.addEphemeralConstant("rand100", lambda: random.random() * 100, float)
pset.addTerminal(False, bool)
pset.addTerminal(True, bool)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSpambase(individual):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Randomly sample 400 mails in the spam database
    spam_samp = random.sample(spam, SAMPLING_SIZE)
    # Evaluate the sum of correctly identified mail as spam
    result = sum(bool(func(*mail[1:])) is bool(mail[0]) for mail in spam_samp)
    return result,
    
toolbox.register("evaluate", evalSpambase)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_TREE_DEPTH))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_TREE_DEPTH))

def main():
    random.seed(10)
    pop = toolbox.population(n=POPULATION_SIZE)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    
    pop, log = algorithms.eaSimple(pop, toolbox, CROSSOVER_RATE, MUTATION_RATE, NUM_OF_GENERATIONS, stats, halloffame=hof)
    #TODO - increase hof size, and take the best of validation set
    best = hof[0]

    eval_dataset(best, 'dataset/validate.csv', True)
    eval_dataset(best, 'dataset/testNoLabels.csv', False)
    return pop, log, stats, hof

if __name__ == "__main__":
    main()
