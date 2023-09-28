

def complementing_dna_strand(data):
    mapping = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    return "".join([s.replace(s, mapping[s]) for s in data[::-1]])


data = "AAAACCCGGT"
print(complementing_dna_strand(data))
