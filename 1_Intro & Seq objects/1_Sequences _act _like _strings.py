from Bio.Seq import Seq

#my_seq = Seq("GATCG")

#to iterate through a sequence, we can use the enumerate function to get both the index and the letter at that index
"""
for index, letter in enumerate(my_seq):
    #print("At index %i the letter is %s" % (index, letter))
    #print(f"At index {index} the letter is {letter}")
    #print("%i %s" % (index, letter))
    print(index,letter) 
"""
"""
#to get the length of a sequence, we can use the len function
print(len(my_seq))
"""
"""
#to get a letter at a specific index, we can use the indexing operator
print(my_seq[0])
print(my_seq[1])
print(my_seq[2])
print(my_seq[3])
print(my_seq[4])
"""
"""
#.count() method counts the number of occurrences of a letter in a sequence
print(my_seq.count("G"))

#"AAAA".count("AA")--not sure why , but it doesnt work

"""
"""
#count() for overllaping count
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(len(my_seq))
print(my_seq.count("G"))

#for index,letter in enumerate(my_seq):
    #print(index,letter)

print(my_seq.count("G"))
print(my_seq.count("C"))
#to calculate the GC content of a sequence, we can use the count method to count the number of G's and C's in the sequence, and then divide that by the length of the sequence
#to calculate GC content %
print(100 * (my_seq.count("G")+ my_seq.count("C")) / len(my_seq))
"""
#while the above count could to calculate a GC%,
#the Bio.SeqUtils module has several GC functions already built.
from Bio.SeqUtils import gc_fraction
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(gc_fraction(my_seq))