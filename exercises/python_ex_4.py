def read_fa(fpath):
    '''Read fasta file to list of lists in format [[>name, seq], [...]]'''
    seqs = []
    with open(fpath, "r") as f:
        for l in f:
            if l[0] == ">":
                seqs.append(f"?{l}")
            else:
                seqs.append(l.replace("\n", ""))

    seqs_split = [i.split("\n") for i in "".join(seqs).split("?")]
    return [i for i in seqs_split if not i == [""]]

if __name__ == "__main__":
    seqs = read_fa("data/influenza_a_h1n1_segments.fasta")
