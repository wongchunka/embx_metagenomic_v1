cd /home/azureuser/development/omic/data_nonhuman

for f in *.fasta; do

/usr/bin/idba_ud -l "/home/azureuser/development/omic/data_nonhuman/$f" -o "/home/azureuser/development/omic/data_contig_idbaud/${f%.fasta}"

done

cd /home/azureuser/development/omic/data_contig_idbaud

for f in * ; do

mv /home/azureuser/development/omic/data_contig_idbaud/$f/contig.fa /home/azureuser/development/omic/data_contig_idbaud/$f.fa

done
