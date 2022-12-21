import sys
from Bio.SeqIO.FastaIO import SimpleFastaParser

print("Number of bases:",len(''.join( [ fsq for fid, fsq in SimpleFastaParser(open(sys.argv[1])) ] )))
