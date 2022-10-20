from string_to_gene import Gene
from typing import List

table_of_codons = {
        ('A','T','A') :'I', ('A','T','C'):'I', ('A','T','T'):'I', ('A','T','G'):'M (START) ',
        ('A','C','A'):'T', ('A','C','C'):'T', ('A','C','G'):'T', ('A','C','T'):'T',
        ('A','A','C'):'N', ('A','A','T'):'N', ('A','A','A'):'K', ('A','A','G'):'K',
        ('A','G','C'):'S', ('A','G','T'):'S', ('A','G','A'):'R', ('A','G','G'):'R',
        ('C','T','A'):'L', ('C','T','C'):'L', ('C','T','G'):'L', ('C','T','T'):'L',
        ('C','C','A'):'P', ('C','C','C'):'P', ('C','C','G'):'P', ('C','C','T'):'P',
        ('C','A','C'):'H', ('C','A','T'):'H', ('C','A','A'):'Q', ('C','A','G'):'Q',
        ('C','G','A'):'R', ('C','G','C'):'R', ('C','G','G'):'R', ('C','G','T'):'R',
        ('G','T','A'):'V', ('G','T','C'):'V', ('G','T','G'):'V', ('G','T','T'):'V',
        ('G','C','A'):'A', ('G','C','C'):'A', ('G','C','G'):'A', ('G','C','T'):'A',
        ('G','A','C'):'D', ('G','A','T'):'D', ('G','A','A'):'E', ('G','A','G'):'E',
        ('G','G','A'):'G', ('G','G','C'):'G', ('G','G','G'):'G', ('G','G','T'):'G',
        ('T','C','A'):'S', ('T','C','C'):'S', ('T','C','G'):'S', ('T','C','T'):'S',
        ('T','T','C'):'F', ('T','T','T'):'F', ('T','T','A'):'L', ('T','T','G'):'L',
        ('T','A','C'):'Y', ('T','A','T'):'Y', ('T','A','A'):'STOP', ('T','A','G'):'STOP',
        ('T','G','C'):'C', ('T','G','T'):'C', ('T','G','A'):'STOP', ('T','G','G'):'W',
    }

def gene_to_amino_acids(gene: Gene) -> List:
    """
    That function takes a gene and decodes it to the list of aminoacids.
    """
    aminoacids = []
    for codon in gene:
        aminoacids.append(table_of_codons[codon])
    print(aminoacids)
    return aminoacids
