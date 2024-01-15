from Bio import Entrez
import os

def DownloadGenBankFile(GenomeSeqDir, OutFile, SeqIDLists, email):
    if not os.path.exists(GenomeSeqDir):
        os.makedirs(GenomeSeqDir)

    Entrez.email = email
    try:
        handle = Entrez.efetch(db="nucleotide", id=", ".join([", ".join(x) for x in SeqIDLists]), rettype="gb", retmode="text")
    except Exception as e:
        raise SystemExit(f"Failed to pull Genbank Data from NCBI Entrez with exception: {e}"
                         f"This is usually a temporary problem due to NCBI server down time, try again in a few minutes!")

    with open(f"{GenomeSeqDir}/{OutFile}", "w") as GenomeSeqDir_handle:
        GenomeSeqDir_handle.write(handle.read())

    handle.close()

if __name__ == "__main__":
    DownloadGenBankFile("downloaded_seqs", "hcv_refseq_1a.fasta", ["AF009606_1a"], "test@provider.com")
