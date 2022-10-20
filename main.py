import prepare_string as ps
import string_to_gene as stg
import gene_to_amino_acids as gtaa
import argparse
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Type an input file:')
    parser.add_argument('filename1', type = str, help = 'Name of an input file:', default = "dna1.txt")
    parser.add_argument('filename2', type = str, help = 'Name of an input file:', default = "dna2.txt")
    args = parser.parse_args()
    with open(args.filename1, 'r+', encoding ='utf-8') as dna1:
        Lines = dna1.readlines()
        for line in Lines:
            gtaa.gene_to_amino_acids(stg.string_to_gene(ps.prepare_string(line)))
    with open(args.filename2, 'r+', encoding ='utf-8') as dna2:
        Lines = dna2.readlines()
        for line in Lines:
            gtaa.gene_to_amino_acids(stg.string_to_gene(ps.prepare_string(line)))
    print(time.process_time())
