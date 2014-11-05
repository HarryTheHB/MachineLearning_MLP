#!/usr/bin/env python
import sys
import pprint
import math

#forward to predict Y and store phi(nets)
def forward(parameters, instance):
    features = instance[1:]
    nets = []
    nets.append(features)  #initial input layer
    #initial hidden layer phi(nets) to zero
    for i in range(len(nodes)):
        numOfCurrentLayerNodes = nodes[i]
        nets.append([0 for k in xrange(numOfCurrentLayerNodes)])  #initial hidden layer outputs

    nets.append([0])  #initial the phi(nets) of output Y
    Y = 0
    for i in range(len(parameters)):
        numOfNodesOfPre = len(parameters[i])
        numOfNodesOfCurrent = len(parameters[i][0])
        for j in range(numOfNodesOfCurrent):
            netJ = 0
            for k in range(numOfNodesOfPre):
                netJ = netJ + parameters[i][k][j] * nets[i][k]
            nets[i + 1][j] = 1 / (1 + math.exp(-1 * netJ))
        if i == len(parameters) - 1:
            if nets[i + 1][0] < 0.5:
                Y = 0
                pprint.pprint(Y)
        else:
            Y = 1
            pprint.pprint(Y)
    return [Y, nets]

#predict Y
def predict(parameters, instance):
    [Y, nets] = forward(parameters, instance)
    return Y

#get accuracy
def evaluate(parameters, instances):
    correct = 0
    for instance in instances:
        label = instance[0]
        Y = predict(parameters, instance)
        if Y == label:
            correct = correct + 1
    return (1.0*correct/len(instance))


#main function
cmdParameters = sys.argv
if (cmdParameters[1] == 'train'):
    alpha = 1
    # initial arrays of parameters matrix, set all the parameters to 0
    numOfInputs = 4
    nodes = [int(x) for x in cmdParameters[3:]]
    parameters = []
    parameters.append([[1 for k in xrange(nodes[0])] for j in xrange(numOfInputs)])

    for i in range(len(nodes) - 1):
        numOfCurrentLayerNodes = nodes[i]
        numOfNextLayerNodes = nodes[i + 1]
        parameters.append([[0 for k in xrange(numOfNextLayerNodes)] for j in xrange(numOfCurrentLayerNodes)])

    parameters.append([[1 for k in xrange(1)] for j in xrange(nodes[len(nodes) - 1])])

    #read instances
    fr = open(cmdParameters[2], 'r')
    lines = fr.read().strip().splitlines()
    for instance in lines:
        instance.split(', ')
        label = instance[0]
        preSegma = []

        #forward to get predicted Y
        [Y, nets] = forward(parameters, instance)
        print '\n'

        #backward propagation
        for i in reversed(range(len(nets))):
            if i > 0:
                numOfNodesOfCurrent = len(nets[i])
                numOfNodesOfLower = len(nets[i - 1])
                currentSegma = []
                if i == len(nets) - 1:
                    currentSegma = [(Y - label) * nets[i][0] * (1 - nets[i][0])]
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
    fr.close()
    parametersMatrix = '\n \n'.join('\n'.join(' '.join(str(x) for x in e) for e in matrix) for matrix in parameters)
    f = open('parameters', 'w')
    f.write(parametersMatrix)
    f.close()


if cmdParameters[1] == 'test':
    fileName = cmdParameters[2]

#pprint.pprint(parameters)
print '\n'




#pprint.pprint(nets[1][1]*parameters[1][1][0])
#print '\n'
#pprint.pprint(parameters )


