"""
from Bio.Seq import Seq
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(messenger_rna)

#translate this mRNA into the corresponding protein sequence

print(messenger_rna.translate)
"""

"""
can also translate directly from the coding strand DNA sequence:
"""

"""
from Bio.Seq import Seq
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)
print(coding_dna.translate)

print(coding_dna.translate(table="Vertebrate Mitochondrial"))

print(coding_dna.translate(table=2))

print(coding_dna.translate(to_stop=True))

print(coding_dna.translate(table=2))

print(coding_dna.translate(table=2, to_stop=True))
#specify the stop symbol if you dont like the default asterisk:
print(coding_dna.translate(table=2, stop_symbol="@"))


"""

from Bio.Seq import Seq
gene = Seq(
    "GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
    "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
    "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
    "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
    "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA"
)

print(gene.translate(table="Bacterial"))

print(gene.translate(table="Bacterial", to_stop=True))

print(gene.translate(table="Bacterial", cds=True))