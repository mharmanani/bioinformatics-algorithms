#!/usr/bin/env python

CODON_TABLE = {
	'UUU':'F', 'CUU': 'L', 'AUU':'I', 'GUU': 'V',
	'UUC':'F', 'CUC': 'L', 'AUC':'I', 'GUC': 'V',
	'UUA':'L', 'CUA': 'L', 'AUA':'I', 'GUA': 'V',
	'UUG':'L', 'CUG': 'L', 'AUG':'M', 'GUG': 'V',
	'UCU':'S', 'CCU': 'P', 'ACU':'T', 'GCU': 'A',
	'UCC':'S', 'CCC': 'P', 'ACC':'T', 'GCC': 'A',
	'UCA':'S', 'CCA': 'P', 'ACA':'T', 'GCA': 'A',
	'UCG':'S', 'CCG': 'P', 'ACG':'T', 'GCG': 'A',
	'UAU':'Y', 'CAU': 'H', 'AAU':'N', 'GAU': 'D',
	'UAC':'Y',  'CAC': 'H', 'AAC':'N', 'GAC': 'D',
	'UAA':'Stop','CAA': 'Q', 'AAA':'K', 'GAA': 'E',
	'UAG':'Stop', 'CAG': 'Q', 'AAG':'K', 'GAG': 'E',
	'UGU':'C',  'CGU': 'R', 'AGU':'S', 'GGU': 'G',
	'UGC':'C',  'CGC': 'R', 'AGC':'S', 'GGC': 'G',
	'UGA':'Stop', 'CGA': 'R', 'AGA':'R', 'GGA': 'G',
	'UGG':'W', 'CGG': 'R', 'AGG':'R', 'GGG': 'G',
}

def rna_translate(rna):
	prot = ''
	for i in range(0, len(rna), 3):
		codon = rna[i:i+3]
		if CODON_TABLE[codon] == 'Stop':
			break # Stop translating
		else:
			prot += CODON_TABLE[codon] # Codon table lookup
	return prot

def main():
	with open('../data/dataset.txt') as dataset:
		rna = dataset.readline().strip() # Read RNA from file

	prot = rna_translate(rna)
	print(prot)

if __name__ == '__main__':
	main()