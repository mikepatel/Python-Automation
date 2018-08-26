# shutil module provides functions for copying files and entire folders, moving, renaming and deleting files

# create a regex that can identify American-style dates
# call os.listdir() to find all files in the working directory
# loop over each filename, using regex to check whether it has a date
# rename file with shutil.move()

#! python3
# American MM-DD-YYYY
# European DD-MM-YYYY

import shutil, os, re

# Create a regex that matches files with the American date format
#datePattern = re.compile(r"""^(1)
#	(2 (3) )-
#	(4 (5) )-
#	(6 (7) )
#	(8)$
#	""", re.VERBOSE)

datePattern = re.compile(r"""^(.*?) # all text before the date
	((0|1)?\d)- 					# month, 1 or 2 digits
	((0|1|2|3)?\d)-					# day, 1 or 2 digits
	((19|20)\d\d)					# year, four digits
	(.*?)$							# all text after the date
	""", re.VERBOSE)


# Loop over files in working directory
for amerFilename in os.listdir('.'):
	matchObject = datePattern.search(amerFilename)

	# Skip files without a date
	if matchObject == None:
		continue

	# Get different parts of filename
	# read the regex, each time see '(' then count with the numbers 1-8 representing groups in the regex
	beforePart = matchObject.group(1)
	monthPart = matchObject.group(2)
	dayPart = matchObject.group(4)
	yearPart = matchObject.group(6)
	afterPart = matchObject.group(8)

	# Form European-style filename
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# Get full, absolute file paths
	absWorkingDir = os.path.abspath('.')
	amerFilename = os.path.join(absWorkingDir, amerFilename) # os.path.join() = join 1+ paths intelligently
	euroFilename = os.path.join(absWorkingDir, euroFilename)

	# Rename files
	print('Renaming "%s" TO "%s"...' % (amerFilename, euroFilename))
	#shutil.move(amerFilename, euroFilename)