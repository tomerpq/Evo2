import random
import operator
import csv
import itertools
import math
import Norm
import numpy
import MainToExe

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from deap import gp

TRAIN_ROWS = 1000

MAX_TREE_DEPTH = 40
POPULATION_SIZE = 1000
CROSSOVER_RATE = 0.75
MUTATION_RATE = 0.1
NUM_OF_GENERATIONS = 2
SAMPLING_SIZE = 1000 # How much samples from the data we will take at evaluate function

#work on the MainToExe file so it contains func saved in data
#and GP can update the func there alone + activate Exe for
#prediction file output, and Exe will only output prediction file
#with his func by getting input of file name
#and output filename given TODO



def get_data_set(filename, deepnessRows):
    with open(filename) as data_file:
        data_reader = csv.reader(data_file)
        dataBeforeNorm = []
        for i in range(deepnessRows):F
            row = data_reader.__next__()
            if (filename == "test.csv"):
                row[0] = 2
            dataBeforeNorm.append(list(float(elem) for elem in row))
        if(filename == 'dataset/train.csv'):
            with open('dataset/trainNormal.csv', mode='w', newline='\n') as new_file:
                employee_writer = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                z = 0
                tmp = []
                while (1):
                    if (z == 700000):
                        break
                    for i in range(z,z+25000):
                        if(i % 25000 == 0):
                            print(f'firsti = {i}')
                        tmp.append(dataBeforeNorm[i])
                    dataNorm = Norm.normalization2(tmp, deepnessRows)
                    tmp = []
                    employee_writer.writerows(dataNorm)
                    z = z + 25000
            return
        elif(filename != 'dataset/trainNormal.csv'):
            dataNorm = Norm.normalization(dataBeforeNorm, deepnessRows)
        else:
            dataNorm = dataBeforeNorm
    return dataNorm

def eval_dataset_ValidateOrTest(individual, filename, deepnessRows, check=False):
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    data = get_data_set(filename, deepnessRows)
    # Evaluate labels
    if len(data[0]) == 121:
        result = [bool(func(*mail[1:])) for mail in data]
    else:
        raise(f'enexpected length! {len(data[0])}')

    size = len(result)
    if check: #Prediction by validate - data
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for i in range(size):
            resI = result[i]
            valI = data[i][0]
            if(resI == True and valI == 1):
                TP += 1
            if(resI == False and valI == 0):
                TN += 1
            if(resI == True and valI == 0):
                FP += 1
            if(resI == False and valI == 1):
                FN += 1
        print(f'TP = {TP} FP = {FP} TN = {TN} FN = {FN}')
        accuracy = (TP + TN)/(TP + FP + TN + FN)
        precision = (TP)/(TP + FP)
        recall = (TP)/(TP + FN)
        beta = 0.25
        betaPowed = math.pow(beta,2)
        fb = (1 + betaPowed)*((precision * recall)/((betaPowed * precision) + recall))
        print(f'Accuracy = {accuracy}\nPrecision = {precision}\n'
              f'Recall = {recall}\n'
              f'F0.25 = {fb}')
    else: #Prediction file
        with open('dataset/output.txt','w') as f:
            for i in range(size):
                resI = result[i]
                f.write(str(int(resI)))
                if(i != (size -1)):
                    f.write('\n')
    return result

def evalSpambase(individual):
    spam = get_data_set('dataset/trainNormal.csv', TRAIN_ROWS)
    # Transform the tree expression in a callable function
    func = toolbox.compile(expr=individual)
    # Randomly sample SAMPLING_SIZE mails in the spam database
    spam_samp = random.sample(spam, SAMPLING_SIZE)
    # Evaluate the sum of correctly identified mail as spam
    result = sum(bool(func(*mail[1:])) is bool(mail[0]) for mail in spam_samp)
    return result,

# Define a protected division function
def protectedDiv(left, right):
    try: return left / right
    except ZeroDivisionError: return 1

# Define a new if-then-else function
def if_then_else(input, output1, output2):
    if input: return output1
    else: return output2

######################### GENETIC PROGRAMMING #####################################

# defined a new primitive set for strongly typed GP
# 120 floats for 4 features * 30 sampels
# TODO - preprocessing the data - currenly it's treated as 120 length vector
pset = gp.PrimitiveSetTyped("MAIN", itertools.repeat(float, 120), bool, "IN")

# boolean operators
pset.addPrimitive(operator.and_, [bool, bool], bool)
pset.addPrimitive(operator.or_, [bool, bool], bool)
pset.addPrimitive(operator.not_, [bool], bool)

# floating point operators
pset.addPrimitive(operator.add, [float,float], float)
pset.addPrimitive(operator.sub, [float,float], float)
pset.addPrimitive(operator.mul, [float,float], float)
pset.addPrimitive(protectedDiv, [float,float], float)
pset.addPrimitive(operator.neg, [float], float)
# pset.addPrimitive(numpy.cos, 1) TODO - add?
# pset.addPrimitive(numpy.sin, 1) TODO - add?

# logic operators
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

toolbox.register("evaluate", evalSpambase)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_TREE_DEPTH))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=MAX_TREE_DEPTH))


def main():
    get_data_set('dataset/train.csv',700000)
    return
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

    eval_dataset_ValidateOrTest(best, 'dataset/validate.csv', 50000, True)
    eval_dataset_ValidateOrTest(best, 'dataset/test.csv', 50000, False)
    return pop, log, stats, hof


if __name__ == "__main__":
    main()
