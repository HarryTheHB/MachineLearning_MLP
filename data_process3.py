import argparse

parser = argparse.ArgumentParser(description='Process data')
parser.add_argument('-i', '--input', help='input file name', required=True)
parser.add_argument('-o', '--output', help='output file name', required=True)
parser.add_argument('-n', '--hidden', help='number of hidden variable', required=True)


args = parser.parse_args() 

fr = open(args.input, 'r')
fw = open(args.output, 'w')
lines = fr.read().strip().splitlines()

first = lines[0]
visible = first.split(', ')
fw.write(' '.join([str((len(visible)-1)), str(args.hidden), str(len(lines))])+"\n")
for line in lines:
	words = line.split(', ')
	num = len(words)

	
	feature = words[1:] 
	#feature = to binary

	fw.write(' '.join(feature)+"\n")

fr.close()
fw.close()