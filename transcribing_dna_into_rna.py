

def transcribe_dna_to_rna(data):
    return data.replace("T", "U")


data = "GATGGAACTTGACTACGTAAATT"
print(transcribe_dna_to_rna(data))
