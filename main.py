from src import check_primers
from src import seq_complement 
from src import translation
from src import mutatuion_position


print("1. Check your primers (enter 1)")
print("2. Seq_complement (enter 2)")
print("3. Seq_reverse_complement (enter 3)")
print("4. Find single mutation position (enter 4)")
print("5. Translate the sequence (enter 5)")
print("6. Check genes expression (enter 6)")
print("7. Create PCR project (enter 7)")
print("8. :) (enter 8)")

numProgram = input("Choose your programme (enter number): ")

if numProgram == "1":
    seq_f = input("Введіть свою Forward послідовність: ").upper()
    seq_r = input("Введіть свою Reverse послідовність: ").upper()
    
    check_primers.checkPrimers(seq_f, seq_r)
elif numProgram == "2":
    res = seq_complement.getComplementSeq(input("Enter seq: ").upper())
    print(res)
elif numProgram == "3":
    res = seq_complement.getComplementSeq(input("Enter seq: ").upper())
    print(res[::-1])
elif numProgram == "4":
    seq1 = input("Введіть першу послідовність: ").upper()
    seq2 = input("Введіть другу послідовність: ").upper()
    res = mutatuion_position.getMutatedNucl(seq1, seq2)
elif numProgram == "5":
    # print('Щоб отримати мРНК натисніть 51')
    # print('Щоб отримати білок натисніть 52')
    # option = int(input("???: "))
    res = translation.proteinDB(input("Введіть будь-ласка свою ДНК послідовність:"))
else:
    print("Error. Try again")
