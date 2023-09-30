import re


def computing_gc_content(data):
    return max(
        [(n, re.subn("[C,G]", "X", s)[1] / len(s) * 100)
         for n, s in re.findall(
             ">(Rosalind_[0-9]{4})*([A,C,G,T]+)",
             data.replace("\n", ""))], key=lambda s: s[1])


data = """
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""
print(computing_gc_content(data))
