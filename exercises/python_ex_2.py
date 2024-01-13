import plotly.express as px

''' Bioinformatics Training 2: Second Python Exercise
Count and graph nucleotide frequencies.
N.b. this code is very inefficient!
'''

def better_nucl_freq(seqs):
    from collections import Counter
    for key, value in seqs.items():
        frequencies[key] = Counter(value)

## 1: 
def draw_graph(data):
    fig = px.bar(data, 
                 barmode="group", 
                 labels={"index": "Base", "value": "Frequency"}, 
                 title="Nucleotide frequencies")
    fig.write_image("mean_nucleotide_freqs.png")
## END 1 \

## 2:
def nucl_frequency(seqs):
    frequencies = {}
    for key, value in seqs.items():
        a, t, c, g = 0, 0, 0, 0
        for nucl in value:
            if nucl.lower() == "a":
                a += 1
            elif nucl.lower() == "t":
                t += 1
            elif nucl.lower() == "c":
                c += 1
            else:
                g += 1
        frequencies[key] = {"A": a, "T": t, "C": c, "G": g}
        print(f"Frequencies for sequence {key}: {frequencies[key]}")
        print(f"CG Ratio: {((c+g)/(a+t+c+g))*100}")
    return frequencies
## END 2 \

def sim_score(seqs):
    '''Assume seqs are same len and aligned'''
    just_seqs = []
    for _, v in seqs.items():
        just_seqs.append(v)
    
    seq_len = len(just_seqs[0])
    matching_nts = 0
    for idx in range(len(seq_len)):
        if just_seqs[0][idx] == just_seqs[1][idx]:
            matching_nts += 1

    print(f"Similarity (% matching nts): {(matching_nts/seq_len) * 100}")


## 3:
if __name__ == "__main__":
    seqs = {
        "HepC_AF009606_1a": "GCCAGCCCCCTGATGGGGGCGACACTCCACCATGAATCACTCCCCTGTGAGGAACTACTGTCTTCACGCAGAAAG",
        "HepC_D90208_1b":   "TTGGGGGCGACACTCCACCATAGATCACTCCCCTGTGAGGAACTACTGTCTTCACGCAGAAAGCGTCTAGCCATG"
        }
    frequencies = nucl_frequency(seqs)
    draw_graph(frequencies)
    sim_score(frequencies)
## END 3 \