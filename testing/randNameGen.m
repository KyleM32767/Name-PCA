for i = 1:10

	% randomly generate a vector
	z = rand(1,324) * 2 - ones(1,324);

	% load the eigenvectors
	u = load('../training/eigenvectors/male.txt');

	% recover the actual vector
	x = z * u';

	% convert to text
	name = vector2text(x)
	
endfor