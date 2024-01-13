from Bio import Entrez
import os

def DownloadGenBankFile(GenomeSeqFile, OutFile, SeqIDLists, email):
    if not os.path.exists(GenomeSeqFile):
        os.makedirs(GenomeSeqFile)

    Entrez.email = email
    try:
        handle = Entrez.efetch(db="nucleotide", id=", ".join([", ".join(x) for x in SeqIDLists]), rettype="gb", retmode="text")
    except Exception as e:
        raise SystemExit(f"Failed to pull Genbank Data from NCBI Entrez with exception: {e}"
                         f"This is usually a temporary problem due to NCBI server down time, try again in a few minutes!")

    with open(f"{GenomeSeqFile}/{OutFile}", "w") as GenomeSeqFile_handle:
        GenomeSeqFile_handle.write(handle.read())

    handle.close()

if __name__ == "__main__":
    DownloadGenBankFile("downloaded_seqs", "hcv_refseq_1a.fasta", ["AF009606_1a"], "test@provider.com")
