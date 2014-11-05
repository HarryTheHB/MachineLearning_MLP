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
	feature = words[:num-1]
	salary = words[num-1].strip()
	for f in feature:
		#print f
		if(f == '?'):
			continue

	feature[1] = workclass.index(feature[1])
	feature[3] = education.index(feature[3])
	feature[5] = marital_status.index(feature[5])
	feature[6] = occupation.index(feature[6])
	feature[7] = relationship.index(feature[7])
	feature[8] = race.index(feature[8])
	feature[9] = sex.index(feature[9])
	feature[13] = native_country.index(feature[13])

	if salary == "<=50K":
		label = 0
	elif salary == ">50K":
		label = 1
	else:
		label = -1


	feature.insert(0, label)
	fw.write(', '.join(str(f) for f in feature)+"\n")

fr.close()
fw.close()
