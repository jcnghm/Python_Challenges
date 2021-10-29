def DNA_strand(dna):
    list = dna.split()
    print(list)
    seq = []
    for i in list[0]:
        if i == "A":
            seq.append("T")
        elif i == "T":
            seq.append("A")
        elif i == "C":
            seq.append("G")
        elif i == "G":
            seq.append("C")
    return ''.join(seq)


print(DNA_strand("AAAA"))