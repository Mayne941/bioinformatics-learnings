'''
Minimal example for plotting ASCII tree to terminal. 
Rich Mayne 2023
'''

from Bio import Phylo
import os

def plot_tree(treename):
    tree = Phylo.read(treename, "newick")
    tree.ladderize()  # Flip branches so deeper clades are displayed at top
    Phylo.draw_ascii(tree)

if __name__ == "__main__":
    fname = input("Please type your file name and extension, e.g.: mytree.nwk\n")
    if not fname.split(".")[-1] == "nwk":
        raise SystemExit("ERROR. Please ensure you've included the file extension")
    if not os.path.exists(fname):
        raise SystemExit(f"ERROR. File '{fname}' not found, please check spelling/directory")
    print("Thanks, processing...")
    plot_tree(fname)
    print(f"Successful! Closing.")