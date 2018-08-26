

import csv
import os

cwd = os.getcwd()
files = os.listdir(cwd)

for file in files:
	if file.endswith('.txt'):
		name, extension = os.path.splitext(file)
		with open(file, 'r') as inFile, open(name + '.csv', 'w') as outFile:
			for line in inFile:
				#print('\n' + str(line))
				outFile.write(line)
