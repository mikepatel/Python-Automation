#! python3
"""
Adds Wikipedia bullet points to the start of each line of text on the clipboard

Initially, have something on local clipboard via Copy
Then, run this script
Finally, when pasting, clipboard contents will be pasted with added bullet points

bullet points: asterisks
"""

import pyperclip

text = pyperclip.paste()

# separate lines and add stars
lines = text.split("\n")
for i in range(len(lines)): 
	lines[i] = "* " + lines[i]

text = "\n".join(lines)

pyperclip.copy(text)
