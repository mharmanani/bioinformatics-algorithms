#!/usr/bin/env python

def hamming(dna1, dna2):
	dist = 0
	for i in range(len(dna1)):
		if dna1[i] != dna2[i]:
			dist += 1
	return dist

def main():
	with open('../data/dataset.txt') as dataset:
		dna1 = dataset.readline().strip()
		dna2 = dataset.readline().strip()

	dist = hamming(dna1, dna2)
	print(dist)

if __name__ == '__main__':
	main()