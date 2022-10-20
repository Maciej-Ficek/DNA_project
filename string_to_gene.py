#from enum import IntEnum
from typing import Tuple, List

#Nucleotide: IntEnum = IntEnum("Nucleotide", ('A', 'C', 'G', 'T'))
"""I should have used IntEnum data type from enum library,
but I had problems with it and therefore chose a simpler solution for the start.
In the future I will upgrade that code.
"""
Codon = Tuple[str, str, str]
Gene = List[Codon]

# You can use that str to test if You experiment with reading from files
#gene_str: str = "CGATCGTCAGCATCGATCGCTACGATCGATCGATCGATCGTACGATCAGCTAGCATCGACTAGCGCTAGCATCAGCAGCCGCTCACGATGCTACGATAAAAACGCTAGCTCG"

def string_to_gene(s: str) -> Gene:
    """
    That functions takes a string of ACTG letters and encodes them as a gene -
    list of three element codons.
    """
    gene: Gene = []
    print(s)
    for i in range(0, len(s)-3, 3):
        codon: Codon = (s[i], s[i+1], s[i+2])
        gene.append(codon)
        print(codon)
    return gene
