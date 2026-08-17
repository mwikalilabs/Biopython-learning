#Two Seq objects can be concatenated by adding them:
from Bio.Seq import Seq
"""
seq1 = Seq("ACGT")
seq2 = Seq("AACCGG")
print(seq1 + seq2)#join the two together
"""
"""
#adding many sequences
list_of_seqs = [Seq("ACGT"), Seq("AACC"), Seq("GGTT")]
concatenated = Seq("")
for s in list_of_seqs:
    concatenated += s
print(concatenated)
"""
#join method
contigs = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
spacer = Seq("N" * 10)
print(spacer.join(contigs))
