#!/usr/bin/env python

def find_motif(dna, motif):
	indices = []
	for i in range(0, len(dna)):
		subseq = dna[i:i+len(motif)]
		if subseq == motif:
			indices += [i + 1]
	return indices

def main():
	with open('../data/dataset.txt') as dataset:
		dna = dataset.readline().strip()
		motif = dataset.readline().strip()

	for idx in find_motif(dna, motif):
		print(idx, end=" ")

if __name__ == '__main__':
	main()