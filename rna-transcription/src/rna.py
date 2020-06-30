#!/usr/bin/env python

def transcribe(dna):
	# Simply replace the thymine base with uracil
	return dna.replace('T', 'U')

def main():
	try:
	    with open('../data/dataset.txt') as dataset:
	        dna = dataset.read().strip()

	    # Transcribe the DNA into RNA
	    rna = transcribe(dna).strip()

	    # Print the RNA
	    print(rna)
	except:
		print('[ERR] No dataset found.')

if __name__ == '__main__':
    main()