def to_rna(dna_strand):
    rna = ''
    for x in dna_strand:
        rna += nucleotide_compliments[x]
    return rna

nucleotide_compliments = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}
