#!/bin/bash
sra_list=(SRR7908796 SRR7908795 SRR7908794 SRR7908793 SRR7908792)
for sra in ${sra_list[@]}
do
        echo "# Downloading $sra..."
        fastq-dump --outdir ~/development/omic/data_raw/ --gzip --skip-technical --readids --read-filter pass --dumpbase --clip $sra
done

