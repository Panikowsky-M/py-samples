from enum import IntEnum
from typing import Tuple, List

Nucleotid: IntEnum = IntEnum('Nucleotid', ('A','C','G','T') )

Codon = Tuple[Nucleotid, Nucleotid, Nucleotid]

Gene = List[Codon]

gene_str: str = "ACGTTAGATTTAGTACCTA"

def strtogene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon: Codon = (Nucleotid[s[i]], Nucleotid[s[i + 1]],
                        Nucleotid[s[i + 2]])
        gene.append(codon)
    return gene

my_gene: Gene = strtogene(gene_str)

def lin_search(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
        return False

acg: Codon = (Nucleotid.A, Nucleotid.C, Nucleotid.G)
gat: Codon = (Nucleotid.G, Nucleotid.A, Nucleotid.T)
print(lin_search(my_gene, acg))
print(lin_search(my_gene, gat))
