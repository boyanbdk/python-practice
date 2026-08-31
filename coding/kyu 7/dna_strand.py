def DNA_strand(dna):
    pairs = {"A":"T", "T":"A", "C":"G", "G":"C"}
    return "".join([pairs[ch] for ch in dna])