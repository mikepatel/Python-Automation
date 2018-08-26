#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?		# area code which is optional, ? matches zero or one of the preceding group
	(\s|-|\.)?				# phone number separator, . matches any character except newline characters
	(\d{3})					# first 3 digits
	(\s|-|\.)				# phone number separator
	(\d{4})					# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension, * maches zero or more of the preceding group
	)''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+		# username, + matches one or more of the preceding group, lowercase, Uppercase, numbers, dot, underscore, %, plus or hyphen, created a character class
	@						# @ symbol
	[a-zA-Z0-9.-]+			# domain name
	(\.[a-zA-Z]{2,4})		# dot-something i.e. ".com"
	)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNumber = '-'.join([groups[1], groups[3], groups[5]])		# group 0 matches the entire regex
	if groups[8] != '':
		phoneNumber += ' x' + groups[8]
	matches.append(phoneNumber)

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found')