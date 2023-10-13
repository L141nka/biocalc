# обернена комплементарність
# def getComplementSeq(seqForComplement):
#     complementary = str()
#     for char in seqForComplement:
#         if char == "C":
#             char = "G"
#         elif char == "G":
#             char = "C"
#         elif char == "T":
#             char = "A"
#         elif char == "A":
#             char = "T"
#         complementary += char

def getReverseComplement(seq):
    from seq_complement import getComplementSeq
    result = getComplementSeq(seq)
    return print(result[::-1])

getReverseComplement(input("Seq: "))
