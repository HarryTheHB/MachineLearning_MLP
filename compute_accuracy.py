from __future__ import division
import argparse


parser = argparse.ArgumentParser(description='compute accuracy')
parser.add_argument('-t', '--test', help='test data file name', required=True)
parser.add_argument('-p', '--prediction', help='predict output', required=True)

args = parser.parse_args()


size = 0;
right = 0;
ft = open(args.test, 'r')
fp = open(args.prediction, 'r')

prediction = fp.read().strip().splitlines()
test = ft.read().strip().splitlines()

size = len(prediction)
if size != len(test):
	print "size dose not match"
	
test = [t.split(', ')[0] for t in test]

for t,p in zip(test, prediction):
	print str(t) + " : " + str(p)
	if t == p:
		right += 1

print "the accuracy is "+str(right/size)+", "+str(right)+"/"+str(size)
