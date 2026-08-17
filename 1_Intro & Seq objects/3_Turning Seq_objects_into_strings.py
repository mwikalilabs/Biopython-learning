from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(str(my_seq))#this prints the whole string

print(my_seq)

"""
using the Seq object directly with a %s placeholder when using 
the Python string formatting or interpolation operator (%):

The format method describes a neat way to get a FASTA formatted 
string from a SeqRecord object
"""
fasta_format_string = ">Name\n%s\n" % my_seq
print(fasta_format_string)