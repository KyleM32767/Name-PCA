'''
	encodeNames.py

	Author: Kyle Mitard
	Created 15 March 2020
	Updated 23 March 2020

	Takes three lists of names and encodes them into one-hot vectors so they can be used for machine learning stuffs
'''

# Encodes a text file (located at names_raw/title.txt) of names with every name on a new line into a group of one-hot vectors. The encoded names
# are put in another text file at names_encoded/title.txt, so they can be imported into Octave/MATLAB
# 
# Param title = a string containing the name of the file
def encodeList(title):

	# indeces of this string are used when creating vectors
	# space is to represent the empty space after the end, since they are all padded out to the same length
	ALPHABET = 'abcdefghijklmnopqrstuvwxyz '

	# open the files containing the raw names and the encoded names
	file_raw = open('names_raw/' + title + '.txt', 'r').read().split('\n')
	file_encoded = open('names_encoded/' + title + '.txt', 'w')

	# determine the length of the longest name
	maxLen = 0
	for n in file_raw:
		if len(n) > maxLen:
			maxLen = len(n)

	for name_raw in file_raw:
		
		# initialize encoded name as empty
		name_encoded = ''
		
		# the names in the list are capitalized, so I must account for that
		name_raw = name_raw.lower()

		# pad out the raw name with spaces as needed to normalize length
		name_raw += ' ' * (maxLen - len(name_raw))
		
		for letter in name_raw:
			letterIndex = ALPHABET.find(letter)
			name_encoded += '-1 ' * letterIndex
			name_encoded += '1 '
			name_encoded += '-1 ' * (26 - letterIndex)

		file_encoded.write(name_encoded + '\n')

	file_encoded.close()

# encodeList('test')
encodeList('male')
encodeList('female')
# encodeList('last')
