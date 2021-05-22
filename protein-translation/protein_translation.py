def proteins(strand):
    codons = {"Methionine": "AUG",
              "Phenylalanine": ["UUU", "UUC"],
              "Leucine": ["UUA", "UUG"],
              "Serine": ["UCU", "UCC", "UCA", "UCG"],
              "Tyrosine": ["UAU", "UAC"],
              "Cysteine": ["UGU", "UGC"],
              "Tryptophan": "UGG",
              "STOP": ["UAA", "UAG", "UGA"]
              }
    if len(strand) < 1 or strand[:3] == "STOP":
        return ""
    else:
        dna = " ".join(codons[0] + proteins(strand[3:]))
    return list(dna)

