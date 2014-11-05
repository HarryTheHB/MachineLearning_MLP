import argparse

workclass = ["?", "Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"]
education = "?, Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool".split(', ')
marital_status = "?, Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse".split(', ')
occupation = "?, Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces".split(', ')
relationship = "?, Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried".split(', ')
race = "?, White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black".split(', ')
sex = "?, Female, Male".split(', ')
native_country = "?, United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands".split(', ')

parser = argparse.ArgumentParser(description='Process data')
parser.add_argument('-i', '--input', help='input file name', required=True)
parser.add_argument('-o', '--output', help='output file name', required=True)

args = parser.parse_args() 

fr = open(args.input, 'r')
fw = open(args.output, 'w')
lines = fr.read().strip().splitlines()


   
for line in lines:
	words = line.split(', ')
	num = len(words)
	
	idx = 7;

	words[1] = workclass.index(words[1])
	words[3] = education.index(words[3])
	words[5] = marital_status.index(words[5])
	words[6] = occupation.index(words[6])
	words[7] = relationship.index(words[7])
	words[8] = race.index(words[8])
	words[9] = sex.index(words[9])
	words[13] = native_country.index(words[13])

	if words[num-1] == "<=50K." or words[num-1] == "<=50K":
		words[num-1] = 0
	elif words[num-1] == ">50K." or words[num-1] == ">50K":
		words[num-1] = 1
	else:
		words[num-1] = -1
	
	feature = words[:idx] + words[idx+1:]
	label = words[idx]
	feature.insert(0, label)
	fw.write(', '.join(str(f) for f in feature)+"\n")

fr.close()
fw.close()