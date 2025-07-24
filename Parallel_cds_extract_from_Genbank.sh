#!/bin/bash
#Usage: bash Parallel_cds_extract_from_Genbank.sh *.gb
echo "$0"
DIR="$(dirname "$0")"
echo "$DIR"
parallel "python \"$DIR\"/cds_extract_from_genbank.py {} | sed 's/).*@/) /;s/PREDICTED: //;s/(//;s/)//g;s/ /_/g' > {.}.fas" ::: $@