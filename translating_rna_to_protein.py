from rna_codon_table import rna_codon_table


def translating_rna_to_protein(s):
    if s[0:3] != "AUG":
        raise Exception("Expected RNA string to begin with the codon \"AUG\".")

    protein = ""
    for i in range(0, len(s), 3):
        amino_acid = rna_codon_table[s[i:i + 3]]
        
        if amino_acid == "Stop":
            return protein

        protein += amino_acid

    raise Exception("Expected RNA string to end with a \"STOP\" codon.")


s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(translating_rna_to_protein(s))
