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

def sort(seqs):
    '''Rich's gnome sort!'''
    just_seqs = []
    whole_seq = ""
    for seq in seqs:
        just_seqs.append(seq[1])
        whole_seq = whole_seq + seq[1]
    print(f"Concatenated seq: {whole_seq}")

    while True:
        n_rearr = 0
        for i in range(len(just_seqs)):
            if i == max(range(len(just_seqs))):
                print("Hit end of queue, restarting...")
                continue
            if len(just_seqs[i]) > len(just_seqs[i+1]):
                new_a, new_b = just_seqs[i+1], just_seqs[i]
                just_seqs[i] = new_a
                just_seqs[i+1] = new_b
                n_rearr += 1
        if n_rearr == 0:
            break
    [print(len(i)) for i in just_seqs]
         

if __name__ == "__main__":
    seqs = read_fa("data/influenza_a_h1n1_segments.fasta")
    sort(seqs)