from Bio.Seq import Seq
my_seq = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(my_seq[4:12])#prints from index 4 to 11
#start:stop:stride/step
#positive stride
print(my_seq [0::3])#prints every 3rd letter starting from index 0,skipping 2 letters in between
print(my_seq[1::3])#prints every 3rd letter starting from index 1,skipping 2 letters in between
print(my_seq[2::3])#prints every 3rd letter starting from index 2
print(my_seq[::3])#prints every 3rd letter starting from index 0,skipping 2 letters in between
#negative stride
print(my_seq[::-1])#prints the sequence in reverse order skipping 0 letters in between
print(my_seq[::-2])#prints the sequence in reverse order skipping 1 letter in between
print(my_seq[::-3])#prints the sequence in reverse order skipping 2 letters in between