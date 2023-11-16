# Install fasttree and mafft to conda env
conda install –y fasttree mafft

# Concatenate ref seqs with unknown, check file
cat data/hcv_refseqs.fasta data/hcv_unknownseq.fasta > data/all_seqs.fasta
cat data/all_seqs.fasta

# Call Mafft
mafft –-auto --thread 8 data/all_seqs.fasta > data/alignment.aln
cat data/alignment.aln

# Call FastTree
fasttree –nt -gamma data/alignment.aln > mytree.nwk
cat mytree.nwk

# Install Python library BioPython
pip install biopython 

# Call ASCII tree plotting Pyton function
python3 exercises/plot_tree.py
