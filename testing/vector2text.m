#{
	vector2text.m
	
	Converts a vector generated via PCA to text by taking the largestvalues in each group of 27 and
	converting it to either a letter or space in accordance to the largest one (i.e. the one with
	the highest probability)
	
	Author: Kyle Mitard
	Created 25 March 2020
#}

function name = vector2text(x)
	
	% initialize name as empty
	name = '';
	
	% the letters in order (dash is used for spaces for clarity when testing)
	LETTERS = 'abcdefghijklmnopqrstuvwxyz-';
	
	% parse through every group of 27 in the vector, each of which represents a single letter
	for i = 1:27:(length(x))
		
		% get the index of the highest number within said group
		[m, index] = max( x(i:(i+26)) );
		
		% add the respective letter
		name = strcat(name, LETTERS(index));
		
	endfor
	
endfunction
