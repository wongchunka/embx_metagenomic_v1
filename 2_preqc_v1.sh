cd /home/azureuser/development/omic/data_raw/
for f in *.fastq.gz ; do
	echo $f
	java -jar /usr/share/java/trimmomatic-0.36.jar SE -phred33 "/home/azureuser/development/omic/data_raw/${f%}" "/home/azureuser/development/omic/data_preqc/${f%}" ILLUMINACLIP:TruSeq3-SE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

done
