import argparse

parser = argparse.ArgumentParser(description='Process data')
parser.add_argument('-i', '--input', help='input file name', required=True)
parser.add_argument('-o', '--output', help='output file name', required=True)


args = parser.parse_args()

fr = open(args.input, 'r')
fw = open(args.output, 'w')

lines = fr.read().strip().splitlines()

for t in lines:
	words = t.split(', ')
	fw.write(words[0]+'\n')
	