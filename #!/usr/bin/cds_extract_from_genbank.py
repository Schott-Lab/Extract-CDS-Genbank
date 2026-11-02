#!/usr/bin/env python3

# Extract CDS sequences from one or more GenBank files
# Removes identical CDS sequences
# By: Ryan K Schott w/ assistance from Copilot
# Usage:
#    python cds_extract_from_genbank.py *.gb

from Bio import SeqIO
import sys
import os

for infile in sys.argv[1:]:

    base = os.path.splitext(os.path.basename(infile))[0]
    outfile = f"{base}_out.fas"

    print(f"Processing {infile}")
    print(f"Writing {outfile}")

    seen = set()

    total_cds = 0
    unique_cds = 0
    duplicate_cds = 0

    with open(outfile, "w") as out:

        for rec in SeqIO.parse(infile, "genbank"):

            if not rec.features:
                continue

            for feature in rec.features:

                if feature.type != "CDS":
                    continue

                total_cds += 1

                seq = str(feature.location.extract(rec).seq)

                if seq in seen:
                    duplicate_cds += 1
                    continue

                seen.add(seq)
                unique_cds += 1

                header = rec.description

                # Clean up fasta headers
                header = header.replace("PREDICTED: ", "")
                header = header.replace("(", "")
                header = header.replace(")", "")
                header = header.replace(", mRNA", "")
                header = header.replace(", transcript variant", "")
                

                out.write(f">{header} {rec.name}\n")
                out.write(f"{seq}\n")

    print(f"  CDS features processed : {total_cds}")
    print(f"  Unique CDS retained    : {unique_cds}")
    print(f"  Duplicate CDS removed  : {duplicate_cds}")
