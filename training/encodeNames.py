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

	for name_raw in file_raw:
		name_encoded = ''
		
		for letter in name_raw:
			letterIndex = ALPHABET.find(letter)
			name_encoded += '0' * letterIndex
			name_encoded += '1'
			name_encoded += '0' * (25 - letterIndex)

		file_encoded.write(name_encoded + '\n')

	file_encoded.close()


encodeList('male')
encodeList('female')
# encodeList('last')