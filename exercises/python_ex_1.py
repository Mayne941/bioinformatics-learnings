## 1:
''' Bioinformatics Training 2: First Python Exercise
These code segments are for reading in two sequence profiles
then generating some descriptive statistics on them.
'''
## END 1 \

## 2:
profile_name = "BK014418" 
profile_seq = "TCAGAGTGATAACACAGATCTAGAGCAATAACAATAACTATGTCTTCGGTTTATTTCCACGTGTCTATAAGTGTGCTCGCAGCTCCTCTATGAACATG"
my_seq = [profile_name, profile_seq]
print("Block 2: ", profile_name, "\n", profile_seq, "\n", my_seq, "\n")
## END 1 \

## 3:
my_other_seq = ["BK014419", "CACGCCATATCAAACGTATATTCATTTTCTCTCTTTGTACTACTTTGATGAAACCTTGCCCAACCTATTTA"]
my_seqs = [my_seq, my_other_seq]
n_seqs = 0
for seq in my_seqs:
    n_seqs = n_seqs + 1
print(f"Block 3: Number of sequences: {n_seqs}\n")
## END 3 \

## 4:
lengths = []
for seq in my_seqs:
    seq_len = len(seq[1])
    print(f"Block 4: Seq: {seq[0]}, length: {seq_len}")
    lengths.append(seq_len)

sum_lens = 0
for length in lengths:
    sum_lens = sum_lens + length

mean_seq_len = sum_lens
print(f"Block 4: Average length of sequences: {mean_seq_len}\n")
## END 4 \

## 5:
print(f"Block 5: Average length of sequences: {sum(lengths)/len(my_seqs)}\n")
## END 5 \

## 6:
import numpy as np 
print(f"Block 6: Average length of sequences: {np.mean(lengths)}\n")
##

## Save as multi fasta!
with open("test.fasta", "w") as f:
    [f.write(f">{i[0]}\n{i[1]}\n") for i in my_seqs]