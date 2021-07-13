#!/bin/bash

cd /home/azureuser/development/omic/data_preqc/
for f in *.fastq.gz ; do
        echo $f
        # load only 500Mbp for indexing each time to decrease memory requirement
        /home/azureuser/development/omic/minimap2/minimap2-2.18_x64-linux/minimap2 -t 3 -I 500M --split-prefix splittemp -a /home/azureuser/development/omic/data_raw/hg38.fa.gz "/home/azureuser/development/omic/data_preqc/${f%%.*}.fastq.gz" | samtools fastq -n -f 4 - | gzip > "/home/azureuser/development/omic/data_nonhuman/${f%%.*}_nonhuman.fastq.gz"
done
