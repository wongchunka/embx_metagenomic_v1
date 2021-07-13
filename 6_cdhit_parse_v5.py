from Bio import SeqIO
import pandas as pd
import os
import glob
import multiprocessing

# Setting
cdhit_dir = "/home/azureuser/development/omic/data_cdhit/"
nonhuman2_dir = "/home/azureuser/development/omic/data_contig/"
output_dir = "/home/azureuser/development/omic/data_cdhitparse/"
cluster_cutoff = 1
fasta_size = 15 # number of sequences to be concurrently uploaded to blastx
  
# Multiprocessing
file_ls = glob.glob(cdhit_dir + "*.fasta.clstr")

def cdhitparse(path):
    basename = os.path.splitext(os.path.splitext(os.path.basename(path))[0])[0]
    cluster_f = os.path.join(cdhit_dir, basename + ".fasta.clstr")
    fasta_f = os.path.join(nonhuman2_dir, basename + ".fasta")
    print(fasta_f)
    with open(cluster_f) as f:
        cluster_ln = f.readlines()
    id_ls = []
    skip_ls = []
    len_ls = []
    count = 0
    for c in cluster_ln:
        if "Cluster" in c:
            if (count != 0):
                len_ls.append(count)
                count = 0
        else:
            if (count ==0):
                start = c.find("NODE_") + 5
                end = c.find("_leng")
                id_ls.append(c[start:end])
            else:
                start = c.find("NODE_") + 5
                end = c.find("_leng")
                skip_ls.append(c[start:end])
            count = count + 1
    if (count != 0):
        len_ls.append(count)
    cluster_df = pd.DataFrame({"id": id_ls, "len": len_ls})
    cluster_df = cluster_df.sort_values(by="len", ascending=False)
    cluster_df = cluster_df.loc[cluster_df['len'] > cluster_cutoff]
    cluster_ls = cluster_df['id'].tolist()
    fasta_ls = []
    for fasta_ln in SeqIO.parse(fasta_f, "fasta"):
        start_short = fasta_ln.id.find("NODE_") + 5
        end_short = fasta_ln.id.find("_leng")
        id_short = fasta_ln.id[start_short: end_short]
        if (id_short not in skip_ls):
            fasta_ls.append(fasta_ln)
    fasta_count = len(fasta_ls) // fasta_size + 1
    fasta_name = os.path.splitext(os.path.basename(fasta_f))[0]
    for n in range(0, fasta_count):
        if (n < fasta_count - 1):
            SeqIO.write(fasta_ls[fasta_size*n:fasta_size*(n+1)], os.path.join(output_dir, fasta_name + "_split15_" + str(n) + ".fasta"), "fasta")
        else:
            SeqIO.write(fasta_ls[fasta_size*n:], os.path.join(output_dir, fasta_name + "_split15_" + str(n) + ".fasta"), "fasta")

pool = multiprocessing.Pool()
result = pool.map(func=cdhitparse, iterable=file_ls)
pool.close()
pool.join()

