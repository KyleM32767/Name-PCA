#{
	get_eigenvectors.m
	
	Author: Kyle Mitard
	Created 15 March 2020
	Updated 23 March 2020
	
	Gets eigenvectors for the three sets of names, encoded with one-hot vectors
#}

% load encoded names
names_male = dlmread('names_encoded/male.txt');
names_female = dlmread('names_encoded/female.txt');
% names_last = csvread('names_encoded/last.txt');

% get m (number of samples) and n (number of features)
[m_male, n_male] = size(names_male);
[m_female, n_female] = size(names_female);
% [m_last, n_last] = size(names_last);

% get covariance matrix
sigma_male = (1 / m_male) * names_male' * names_male;
sigma_female = (1 / m_female) * names_female' * names_female;
% sigma_last = (1 / m_last) * names_last' * names_last;

% do single value decomposition
[U_male, S_male, D_male] = svd(sigma_male);
[U_female, S_female, D_female] = svd(sigma_female);
% [U_last, S_last, D_last] = svd(sigma_last);

% save eigenvectors in a csv file
save 'eigenvectors/male.csv' U_male -ascii;
save 'eigenvectors/female.csv' U_female -ascii;
% save 'eigenvectors/last.txt' U_last -ascii;
