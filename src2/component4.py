#мутація нуклеотидної основи 
    
def nuclMutation(inp_seq, position, new_nucl):
    mod_seq = ""
    mod_seq = inp_seq[:position-1] + new_nucl + inp_seq[position:]

    return f"Змутована послідовність: {mod_seq}."

inp_seq = input('Введіть послідовність: ')
position = int(input('Введіть місце основи: '))
new_nucl = input('Введіть основу на заміну: ')

mutation = nuclMutation(inp_seq, position, new_nucl)

print(mutation)