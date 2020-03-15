'''
	encodeNames.py

	Author: Kyle Mitard
	Created 15 March 2020

	Takes three lists of names and encodes them into one-hot vectors so they can be used for machine learning stuffs
'''

def encodeList(title):

	# indeces of this string are used when creating vectors
	ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

	# open the files containing the raw names and the encoded names
	file_raw = open('names_raw/' + title + '.txt', 'r').read().split('\n')
	file_encoded = open('names_encoded/' + title + '.txt', 'w')

	# determine the length of the longest name
	maxLen = 0
	for n in file_raw:
		if len(n) > maxLen:
			maxLen = len(n)

	for name_raw in file_raw:
		name_encoded = ''

		# pad out the raw name with spaces to normalize length
		name_raw += ' ' * (maxLen - len(name_raw))
		
		for letter in name_raw:
			letterIndex = ALPHABET.find(letter)
			if letterIndex != -1:
				name_encoded += '0 ' * letterIndex
				name_encoded += '1 '
			name_encoded += '0 ' * (25 - letterIndex)

		file_encoded.write(name_encoded + '\n')

	file_encoded.close()

# encodeList('test')
encodeList('male')
encodeList('female')
# encodeList('last')
