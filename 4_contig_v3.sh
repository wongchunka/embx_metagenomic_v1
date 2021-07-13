#!/bin/bash
cd /home/azureuser/development/omic/data_nonhuman/
for f in *.fastq ; do  
python3 /home/azureuser/development/omic/spades/SPAdes-3.15.2-Linux/bin/spades.py --metaviral -s /home/azureuser/development/omic/data_nonhuman/$f -o "/home/azureuser/development/omic/data_contig/${f%.fastq}"
done


