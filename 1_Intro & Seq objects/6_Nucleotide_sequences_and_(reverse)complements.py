#complement or reverse complement
from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq)

#complement
print(my_seq.complement)
#reverse compliment
print(my_seq.reverse_complement)

#can also reverse seq with slicing method using a negative stride
print(my_seq[::-1])












#***IUPAC ambiguity code

