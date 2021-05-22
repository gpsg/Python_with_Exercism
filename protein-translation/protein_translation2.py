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
    answer = []
    for i in range(0, len(strand), 3):
        if codons[strand[i:i+3]] == "STOP":
            break
        answer.append(codons[strand[i:i+3]])
    return answer



"""
def proteins(strand):
    codons = {"AUG": "Methionine",
              "UUU": "Phenylalanine", "UUC": "Phenylalanine",
              "UUA": "Leucine", "UUG": "Leucine",
              "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
              "UAU": "Tyrosine", "UAC": "Tyrosine",
              "UGU": "Cysteine", "UGC": "Cysteine",
              "UGG": "Tryptophan",
              "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
              }
    i = 0
    answer = []
    while i < len(strand):
        letters = strand[i:i + 3]
        if codons[letters] == "STOP":
            i = len(strand)
        else:
            answer.append(codons[letters])
            i += 3
    return answer
"""


"""
stop = ["UAA", "UAG", "UGA"]
    for i in stop:
        temp = strand.find(i)
        if temp >= 0:
            strand = strand[:temp]
    answer = []
    for i in range(0, len( strand), 3):
        letters = strand[i:i+3]
        if letters in codons:
            answer.append(codons[letters])
    return answer
"""

if __name__ == "__main__":
    rna = "AUGUUUUCU"
    print(proteins(rna) == ["Methionine", "Phenylalanine", "Serine"])
    rna = "AUGUUUUCUUAAAUG"
    print(proteins(rna) == ["Methionine", "Phenylalanine", "Serine"])
    print(proteins("AUG"))


# exercism submit Exercism/python/protein-translation/protein_translation.py