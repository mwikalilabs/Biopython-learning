from Bio.Seq import Seq
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

#print(coding_dna)
template_dna = coding_dna.reverse_complement()
#print(template_dna)

#transcribe the coding strand into the corresponding mRNA
#T is replaced with U
mrna = coding_dna.transcribe()
print(mrna)
"""
If you do want to do a true biological transcription 
starting with the template strand, then this becomes 
a two-step process
"""
print(template_dna.reverse_complement().transcribe())

"""
The Seq object also includes a back-transcription 
method for going from the mRNA to the coding strand
of the DNA. Again, this is a simple U > T substitution:
--basically from the transcribed coding dna strand(ss mRNA) to 
the original dna strand(crick strand)
"""
print(mrna.back_transcribe())