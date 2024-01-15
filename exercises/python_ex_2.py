import plotly.express as px

''' Bioinformatics Training 2: Second Python Exercise
Count and graph nucleotide frequencies.
N.b. this code is very inefficient!
'''

def better_nucl_freq(seqs):
    from collections import Counter
    for key, value in seqs.items():
        frequencies[key] = Counter(value)

## 3: 
def draw_graph(data):
    fig = px.bar(data, 
                 barmode="group", 
                 labels={"index": "Base", "value": "Frequency"}, 
                 title="Nucleotide frequencies")
    fig.write_image("mean_nucleotide_freqs.png")
## END 3 \

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
    return frequencies
## END 2 \
    
## 1:
if __name__ == "__main__":
    seqs = {
        "HepC_AF009606_1a": "GCCAGCCCCCTGATGGGGGCGACACTCCACCATGAATCACTCCCCTGTGAGGAACTACTGTCTTCACGCAGAAAG",
        "HepC_D90208_1b":   "TTGGGGGCGACACTCCACCATAGATCACTCCCCTGTGAGGAACTACTGTCTTCACGCAGAAAGCGTCTAGCCATG"
        }
    frequencies = nucl_frequency(seqs)
    draw_graph(frequencies)
## END 1 \