#дається фрагмент ДНК
#знайти потрібну ділянку в заданому фрагменті ДНК

seq = input("Введіть послідовність ДНК: ")
fragment = input("Введіть фрагмент ДНК, який ви хочете знайти в послідовності: ")

def fragmentFinder(seq, fragment):
    if fragment in seq:
        return(f"Фрагмент {fragment} знайдено")
    else:
        return(f"Фрагмент {fragment} не знайдено")

get_fragment = fragmentFinder(seq, fragment)

print(get_fragment)