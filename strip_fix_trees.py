#!/usr/bin/python
from cStringIO import StringIO
from Bio import Phylo

def yield_trees(file_path):
    with open(file_path) as input_handle:
        for line in input_handle:
            current = line.strip()
            if current:
                string_handle = StringIO(current)
                yield Phylo.read(string_handle, "newick")


file_path = "test.tre"
output_path = 'parsed.tre'
tree_yielder = yield_trees(file_path)
outgroup = ['4776', '6139', '7128', 'OTO30611']

trees = []
for tree in tree_yielder:
    if tree.is_bifurcating():
        trees.append(
            tree.root_with_outgroup(*outgroup)
        )

with open(output_path, 'w+') as output_handle:
    Phylo.write(trees, output_handle, "newick")
