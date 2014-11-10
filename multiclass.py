#!/usr/bin/env python
from __future__ import division
import sys
import math
import random


# read data
def readData(fileName):
    fr = open(fileName, 'r')
    lines = fr.read().strip().splitlines()
    instances = []
    for line in lines:
        instance = line.split(', ')
        instances.append([float(x) for x in instance])
    fr.close()
    return instances


#forward to predict Y and store phi(nets)
def forward(parameters, instance, nodes):
    features = instance[1:]
    nets = []
    nets.append(features)  #initial input layer
    #initial hidden layer phi(nets) to zero
    for i in range(len(nodes)):
        numOfCurrentLayerNodes = nodes[i]
        nets.append([0 for k in xrange(numOfCurrentLayerNodes)])  #initial hidden layer outputs

    #nets.append([0])  #initial the phi(nets) of output Y
    Y = [0 for x in xrange(nodes[len(nodes)-1])]
    for i in range(len(parameters)):
        numOfNodesOfPre = len(parameters[i])
        numOfNodesOfCurrent = len(parameters[i][0])
        for j in range(numOfNodesOfCurrent):
            netJ = 0
            for k in range(numOfNodesOfPre):
                netJ = netJ + parameters[i][k][j] * nets[i][k]
            nets[i + 1][j] = 1.0 / (1 + math.exp(-1 * netJ))
            #if i == len(parameters) - 1:
    for j in xrange(len(Y)):
        if nets[len(nets) - 1][j] < 0.5:
            Y[j] = 0
        else:
            Y[j] = 1
    return [Y, nets]


#predict Y
def predict(parameters, instance, nodes):
    features = instance[1:]
    nets = []
    nets.append(features)  #initial input layer
    #initial hidden layer phi(nets) to zero
    for i in range(len(nodes)):
        numOfCurrentLayerNodes = nodes[i]
        nets.append([0 for k in xrange(numOfCurrentLayerNodes)])  #initial hidden layer outputs

    #nets.append([0])  #initial the phi(nets) of output Y
    Y = [0 for x in xrange(nodes[len(nodes)-1])]
    for i in range(len(parameters)):
        numOfNodesOfPre = len(parameters[i])
        numOfNodesOfCurrent = len(parameters[i][0])
        for j in range(numOfNodesOfCurrent):
            netJ = 0
            for k in range(numOfNodesOfPre):
                netJ = netJ + parameters[i][k][j] * nets[i][k]
            nets[i + 1][j] = 1.0 / (1 + math.exp(-1 * netJ))
            #if i == len(parameters) - 1:
    maxNet = 0
    for j in xrange(len(Y)):
        if nets[len(nets) - 1][j] > nets[len(nets)-1][maxNet]:
            maxNet = j
    Y[maxNet] = 1
    return Y


#get accuracy
def evaluate(parameters, instances, nodes):
    correct = 0
    numOfYs = nodes[len(nodes)-1]
    for instance in instances:
        label = [0 for x in xrange(numOfYs)]
        label[int(instance[0])-1] = 1
        Y = predict(parameters, instance, nodes)
        c = True;
        for i in range(len(Y)-1):
            if label[i] != Y[i]:
                c = False
        if c == True:
            correct = correct + 1
    return (1.0 * correct / len(instances))


#main function
cmdParameters = sys.argv
if (cmdParameters[1] == 'train'):
    alpha = 1
    instances = readData(cmdParameters[2])
    # initial arrays of parameters matrix, set all the parameters to 0
    numOfInputs = len(instances[0]) - 1
    #numOfNodesOfOutputLayer = int(cmdParameters[3])
    nodes = [int(x) for x in cmdParameters[3:]]
    parameters = []
    parameters.append(
        [[random.random() for k in xrange(nodes[0])] for j
         in xrange(numOfInputs)])

    for i in range(len(nodes) - 1):
        numOfCurrentLayerNodes = nodes[i]
        numOfNextLayerNodes = nodes[i + 1]
        parameters.append([[random.random() for k in
                            xrange(numOfNextLayerNodes)] for j in xrange(numOfCurrentLayerNodes)])

    #parameters.append(
    #    [[random.random() for k in xrange(1)] for j in
    #     xrange(nodes[len(nodes) - 1])])

    for instance in instances:
        numOfYs = nodes[len(nodes)-1]
        label = [0 for x in xrange(numOfYs)]
        label[int(instance[0])-1] = 1
        preSegma = []

        #forward to get predicted Y
        [Y, nets] = forward(parameters, instance, nodes)

        #backward propagation
        for i in reversed(range(len(nets))):
            if i > 0:
                numOfNodesOfCurrent = len(nets[i])
                numOfNodesOfLower = len(nets[i - 1])
                currentSegma = []
                if i == len(nets) - 1:
                    for j in range(numOfYs):
                        currentSegma.append((Y[j] - label[j]) * nets[i][j] * (1 - nets[i][j]))
                else:
                    numOfNodesOfUpper = len(nets[i + 1])
                    for j in range(numOfNodesOfCurrent):
                        tmp = 0
                        for k in range(numOfNodesOfUpper):
                            tmp = tmp + preSegma[k] * parameters[i][j][k]
                        segma = tmp * nets[i][j] * (1 - nets[i][j])
                        currentSegma.append(segma)
                for j in range(numOfNodesOfLower):
                    for k in range(numOfNodesOfCurrent):
                        parameters[i - 1][j][k] = parameters[i - 1][j][k] - alpha * currentSegma[k] * nets[i - 1][j]
                preSegma = currentSegma
    print 'accuracy = ' + str(evaluate(parameters, instances, nodes))
    parametersMatrix = '\n\n'.join('\n'.join(' '.join(str(x) for x in e) for e in matrix) for matrix in parameters)
    f = open('parameters', 'w')
    f.write(parametersMatrix)
    f.close()

if cmdParameters[1] == 'test':
    parametersFile = cmdParameters[2]
    fr = open(parametersFile, 'r')
    lines = fr.read().strip().splitlines()
    parameters = []
    node = []
    words = []
    for line in lines:
        #print line
        #print repr(line)
        if line in ['\n', '', ' ']:
            parameters.append(node)
            node = []
        else:
            words = line.split(' ')
            node.append([float(w) for w in words])
    parameters.append(node)
    #print parameters
    fr.close()
    nodes = []
    instances = readData(cmdParameters[3])
    for i in xrange(len(parameters)):
        nodes.append(len(parameters[i]))
    print 'accuracy = ' + str(evaluate(parameters, instances, nodes))



#pprint.pprint(parameters)
print '\n'




#pprint.pprint(nets[1][1]*parameters[1][1][0])
#print '\n'
#pprint.pprint(parameters )


