#!/bin/bash

cd /home/azureuser/development/omic/data_contig/

for f in *.fasta ; do

/home/azureuser/development/omic/cdhit/cdhit/cd-hit-est -i "/home/azureuser/development/omic/data_contig/$f" -o "/home/azureuser/development/omic/data_cdhit/$f" -c 0.95 -n 10 

done
