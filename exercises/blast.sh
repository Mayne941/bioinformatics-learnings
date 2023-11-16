# Create a new conda environment, activate, install blast
conda create --name learnings
conda activate learnings
conda install blast

# Make blast database of HCV reference genomes
makeblastdb -in data/hcv_refseqs.fasta -parse_seqids -title "hcv_db" -dbtype nucl

# Query unknown sequence against HCV reference db
blastn -query data/hcv_unknownseq.fasta -task blastn-short -db data/hcv_refseqs.fasta -outfmt "7 qseqid sseqid bitscore qcovs evalue pident" -max_target_seqs 5 -evalue 0.01