#upper and lower methods for changing the case
from Bio.Seq import Seq
dna_seq = Seq("acgtACGT")
print(dna_seq)
#upper
print(dna_seq.upper())
#lower
print(dna_seq.lower())

#useful for doing case insensitive matching
print("GTAC" in dna_seq)

print("GTAC" in dna_seq.upper())