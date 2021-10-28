def protein_synthesis(dna):
    string = "".join(dna.split())
    seq = []
    prot = ["Met"]
    for i in string:
        if i =="A":
            seq.append("A")
        elif i == "T":
            seq.append("U")
        elif i == "C":
            seq.append("C")
        else:
            seq.append("G")
    print(seq)
    joined = ''.join(seq)
    print(joined)
    ind = joined.find("AUG")
    x = slice(ind + 3, -1)
    y = seq[x]
    print(y)
    z = ''.join(y)
    print(z)
    if z[0:3] == "CAA" or z[0:3] == "CAG":
        prot.append("Gln")
    elif z[0:3] == "GGU":
        prot.append("Gly")
    elif z[0:3] == "GCG":
        prot.append("Ala")
    elif z[0:3] == "UUU" or z[0:3] == "UUC":
        prot.append("Phe")
    elif z[0:3] == "UGG":
        prot.append("Trp")
    elif z[0:3] == "UAA" or z[0:3] == "UAG" or z[0:3] == "UGA":
        pass
    if z[3:6] == "CAA" or z[3:6] == "CAG":
        prot.append("Gln")
    elif z[3:6] == "GGU":
        prot.append("Gly")
    elif z[3:6] == "GCG":
        prot.append("Ala")
    elif z[3:6] == "UUU" or z[3:6] == "UUC":
        prot.append("Phe")
    elif z[3:6] == "UGG":
        prot.append("Trp")
    elif z[3:6] == "UAA" or z[3:6] == "UAG" or z[3:6] == "UGA":
        pass
    print(prot)





print(protein_synthesis("CAA ATG CAG GCG TAA"))