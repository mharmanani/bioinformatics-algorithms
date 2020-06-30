#!/usr/bin/env python
COMPLEMENTS = {
	'A':'T', 'C':'G',
	'G':'C', 'T':'A'
}

def find_reverse_complement(dna):
	# Match each base with its complement
	dna_c = ''.join([COMPLEMENTS[base] for base in dna])

	# Flip the string to get the reverse complement
	return dna_c[::-1]

def main():
    with open('../data/dataset.txt') as dataset:
        dna = dataset.read().strip()

    # Generate and print the reverse complement
    dna_c = find_reverse_complement(dna).strip()

    print(dna_c)

if __name__ == '__main__':
    main()