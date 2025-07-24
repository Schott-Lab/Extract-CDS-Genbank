#Extract CDS sequences from a Genbank format file
#Usage: python ./cds_extract_from_genbank.py <inputfile> <outputfile>
#By: Ryan K Schott

from Bio import SeqIO
import sys
import os

for rec in SeqIO.parse(sys.argv[1], "genbank"):
	if rec.features:
		for feature in rec.features:
			if feature.type == "CDS":
				print(">" + rec.description + " @" + rec.name + "\n" + feature.location.extract(rec).seq)