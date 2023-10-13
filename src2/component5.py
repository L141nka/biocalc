#пошук мутантних нуклеотидів

def getMutatedNucl(seq1, seq2):
    mut_nucl = []
    if len(seq1) == len(seq2):
        for i in range(len(seq1)):
            if seq2[i] != seq1[i]:
                mut_nucl.append(seq2[i] + f', pos:{i+1}')
    else:
        mut_nucl = print("Error: Послідовності не однакової довжини")

    return mut_nucl

seq1 = input("Введіть першу послідовність: ")
seq2 = input("Введіть другу послідовність: ")

mutated_nucl_finder = getMutatedNucl(seq1, seq2)
print(mutated_nucl_finder)



