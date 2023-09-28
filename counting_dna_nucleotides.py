from itertools import groupby


def count_dna_nucleotides(data):
    return list(({ "A": 0, "C": 0, "G": 0, "T": 0 } | { 
        k: sum(1 for _ in g) for k, g in groupby(sorted(data)) }).values())


data = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
print(count_dna_nucleotides(data))
