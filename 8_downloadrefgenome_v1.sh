echo $1 $2

if [ -n "$1" ]; then
grep -E "$1" /home/azureuser/development/omic/assembly_summary_refseq.txt
fi

if [ -n "$1" ] && [ -n "$2" ]; then
grep -E "$1" /home/azureuser/development/omic/assembly_summary_refseq.txt | cut -f 20 > /home/azureuser/development/omic/ftp_folder.txt
awk 'BEGIN{FS=OFS="/";filesuffix="genomic.fna.gz"}{ftpdir=$0;asm=$10;file=asm"_"filesuffix;print "wget "ftpdir,file" -O /home/azureuser/development/omic/data_refgen/temp.fna.gz\ngunzip /home/azureuser/development/omic/data_refgen/temp.fna.gz"}' /home/azureuser/development/omic/ftp_folder.txt > /home/azureuser/development/omic/download_fna_files.sh
source /home/azureuser/development/omic/download_fna_files.sh
mv /home/azureuser/development/omic/data_refgen/temp.fna "/home/azureuser/development/omic/data_refgen/$2.fna"
bowtie2-build "/home/azureuser/development/omic/data_refgen/$2.fna" "/home/azureuser/development/omic/data_refgen/$2"
fi
